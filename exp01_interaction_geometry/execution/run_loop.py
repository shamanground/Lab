import json
import os
import datetime
from pathlib import Path
from openai import OpenAI
from openai import RateLimitError
import yaml


# ---------- LOAD CONFIG ----------
BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_PATH = BASE_DIR / "config" / "experiment.yaml"

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

# ---------- LOAD PROMPTS ----------
PROMPTS_DIR = BASE_DIR / "prompts"

with open(PROMPTS_DIR / "system.txt", "r") as f:
    SYSTEM_PROMPT = f.read().strip()

with open(PROMPTS_DIR / "turn1.txt", "r") as f:
    TURN1_PROMPT = f.read().strip()

with open(PROMPTS_DIR / "loop.txt", "r") as f:
    LOOP_PROMPT = f.read().strip()

with open(PROMPTS_DIR / "perturb.txt", "r") as f:
    PERTURB_PROMPT = f.read().strip()

# ---------- SETUP ----------
client = OpenAI()

OUTPUT_DIR = BASE_DIR / config["log_dir_raw"]
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

timestamp = datetime.datetime.utcnow().isoformat()

messages = [
    {
        "role": "system",
        "content": [{"type": "input_text", "text": SYSTEM_PROMPT}],
    },
    {
        "role": "user",
        "content": [{"type": "input_text", "text": TURN1_PROMPT}],
    },
]

turn_logs = []

# ---------- INITIAL TURN ----------
response = client.responses.create(
    model=config["model"],
    input=messages,
    temperature=config["temperature"],
    top_p=config["top_p"],
    max_output_tokens=config["max_tokens"],
    
)

assistant_text = response.output_text

messages.append({
    "role": "assistant",
    "content": [{"type": "output_text", "text": assistant_text}],
})


turn_logs.append({
    "turn": 1,
    "user": TURN1_PROMPT,
    "assistant": assistant_text,
})

# ---------- LOOP ----------
failure = None

try:
    for t in range(2, config["max_loop_turns"] + 1):

        if t == config["perturb_turn"]:
            user_prompt = PERTURB_PROMPT
            condition = "perturb"
        else:
            user_prompt = LOOP_PROMPT
            condition = "loop"

        messages.append({
            "role": "user",
            "content": [{"type": "input_text", "text": user_prompt}],
        })

        response = client.responses.create(
            model=config["model"],
            input=messages,
            temperature=config["temperature"],
            top_p=config["top_p"],
            max_output_tokens=config["max_tokens"],
        )

        assistant_text = response.output_text

        messages.append({
            "role": "assistant",
            "content": [{"type": "output_text", "text": assistant_text}],
        })

        turn_logs.append({
            "turn": t,
            "condition": condition,
            "user": user_prompt,
            "assistant": assistant_text,
        })

except RateLimitError as e:
    failure = {
        "type": "TPM_RATE_LIMIT",
        "turn": t,
        "error": str(e),
    }


# ---------- LOG ----------
log = {
    "experiment_id": config["experiment_id"],
    "condition": "loop",
    "timestamp": timestamp,
    "model": config["model"],
    "max_turns": config["max_loop_turns"],
    "perturb_turn": config["perturb_turn"],
    "system_prompt": SYSTEM_PROMPT,
    "turns": turn_logs,
    "failure": failure,
}

with open(OUTPUT_DIR / "loop.json", "w") as f:
    json.dump(log, f, indent=2)

print("Loop execution complete. Logged to logs/raw/loop.json")
