import json
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

with open(PROMPTS_DIR / "perturb.txt", "r") as f:
    PERTURB_PROMPT = f.read().strip()

# ---------- LOAD LOOP TRANSCRIPT ----------
RAW_DIR = BASE_DIR / config["log_dir_raw"]
LOOP_PATH = RAW_DIR / "loop.json"

if not LOOP_PATH.exists():
    raise FileNotFoundError("loop.json not found. Run run_loop.py first.")

with open(LOOP_PATH, "r") as f:
    loop_log = json.load(f)

# ---------- BUILD REPLAY INPUT ----------
replay_text = []
for turn in loop_log["turns"]:
    replay_text.append(f"User:\n{turn['user']}\n")
    replay_text.append(f"Assistant:\n{turn['assistant']}\n")

replay_block = "\n".join(replay_text)

# ---------- SETUP ----------
client = OpenAI()
timestamp = datetime.datetime.utcnow().isoformat()

# ---------- RUN REPLAY ----------
response = client.responses.create(
    model=config["model"],
    input=[
        {
            "role": "system",
            "content": [{"type": "input_text", "text": SYSTEM_PROMPT}],
        },
        {
            "role": "user",
            "content": [{"type": "input_text", "text": replay_block + "\n\n" + PERTURB_PROMPT}],
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
    "condition": "replay",
    "timestamp": timestamp,
    "model": config["model"],
    "source": "loop.json",
    "system_prompt": SYSTEM_PROMPT,
    "replay_input": replay_block,
    "perturbation": PERTURB_PROMPT,
    "assistant": output_text,
}

with open(RAW_DIR / "replay.json", "w") as f:
    json.dump(log, f, indent=2)

print("Replay execution complete. Logged to logs/raw/replay.json")
