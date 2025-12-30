import json
import os
from pathlib import Path
from openai import OpenAI
import yaml
import datetime

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

# ---------- SETUP ----------
client = OpenAI()

OUTPUT_DIR = BASE_DIR / config["log_dir_raw"]
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

timestamp = datetime.datetime.utcnow().isoformat()

# ---------- RUN SINGLE-SHOT ----------
response = client.responses.create(
    model=config["model"],
    input=[
        {
            "role": "system",
            "content": [{"type": "input_text", "text": SYSTEM_PROMPT}],
        },
        {
            "role": "user",
            "content": [{"type": "input_text", "text": TURN1_PROMPT}],
        },
    ],
    temperature=config["temperature"],
    top_p=config["top_p"],
    max_output_tokens=config["max_tokens"],
    
)

output_text = response.output_text

# ---------- LOG ----------
log = {
    "experiment_id": config["experiment_id"],
    "condition": "single",
    "timestamp": timestamp,
    "model": config["model"],
    "system_prompt": SYSTEM_PROMPT,
    "turns": [
        {
            "turn": 1,
            "user": TURN1_PROMPT,
            "assistant": output_text,
        }
    ],
}

with open(OUTPUT_DIR / "single.json", "w") as f:
    json.dump(log, f, indent=2)

print("Single-shot execution complete. Logged to logs/raw/single.json")
