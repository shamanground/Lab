#!/usr/bin/env bash
set -euo pipefail

# ============================================
# Experiment 2 — Axis Existence
# Bash Execution Script (FINAL, JSON-SAFE)
# ============================================

ROOT_DIR="$(pwd)"
RAW_DIR="$ROOT_DIR/runs/raw"
LOG_DIR="$ROOT_DIR/logs"
LOG_FILE="$LOG_DIR/execution_log.jsonl"

mkdir -p "$RAW_DIR"
mkdir -p "$LOG_DIR"
: > "$LOG_FILE"

# Load environment
set -a
source .env
set +a

MODEL="gpt-4.1"
MAX_TOKENS=120
TEMPERATURE=0.0
TOP_P=1.0
FREQ_PENALTY=0.0
PRES_PENALTY=0.0

SYSTEM_PROMPT="$(cat config/system_prompt.txt)"

declare -a RUNS=(
  "claim01_baseline" "claim01_control" "claim01_primary"
  "claim02_baseline" "claim02_control" "claim02_primary"
  "claim03_baseline" "claim03_control" "claim03_primary"
  "claim04_baseline" "claim04_control" "claim04_primary"
  "claim05_baseline" "claim05_control" "claim05_primary"
)

get_claim_text () {
  local claim_num="$1"
  cat "prompts/claims/claim_${claim_num}.txt"
}

get_constraint_text () {
  local type="$1"
  if [[ "$type" == "control" ]]; then
    echo "Produce an answer under 120 tokens. Do not introduce contradictions."
  elif [[ "$type" == "primary" ]]; then
    echo "Produce an answer that contains an explicit internal contradiction. Do not acknowledge, resolve, or explain the contradiction. Limit the response to 120 tokens."
  else
    echo ""
  fi
}

for RUN_ID in "${RUNS[@]}"; do
  TS_START="$(date -Iseconds)"

  CLAIM_NUM="$(echo "$RUN_ID" | cut -c6-7)"
  MODE="$(echo "$RUN_ID" | cut -d_ -f2)"

  CLAIM_TEXT="$(get_claim_text "$CLAIM_NUM")"
  CONSTRAINT_TEXT="$(get_constraint_text "$MODE")"

  if [[ "$MODE" == "baseline" ]]; then
    USER_PROMPT="$CLAIM_TEXT"
  else
    USER_PROMPT="$CLAIM_TEXT"$'\n\n'"$CONSTRAINT_TEXT"
  fi

  RESPONSE_JSON="$LOG_DIR/${RUN_ID}_response.json"
  RAW_TXT="$RAW_DIR/${RUN_ID}.txt"

  # ---- BUILD JSON SAFELY (CRITICAL FIX) ----
  PAYLOAD=$(jq -n \
    --arg model "$MODEL" \
    --arg system "$SYSTEM_PROMPT" \
    --arg user "$USER_PROMPT" \
    --argjson temperature "$TEMPERATURE" \
    --argjson max_tokens "$MAX_TOKENS" \
    --argjson top_p "$TOP_P" \
    --argjson frequency_penalty "$FREQ_PENALTY" \
    --argjson presence_penalty "$PRES_PENALTY" \
    '{
      model: $model,
      temperature: $temperature,
      max_tokens: $max_tokens,
      top_p: $top_p,
      frequency_penalty: $frequency_penalty,
      presence_penalty: $presence_penalty,
      messages: [
        { role: "system", content: $system },
        { role: "user", content: $user }
      ]
    }'
  )

  curl https://api.openai.com/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d "$PAYLOAD" \
    > "$RESPONSE_JSON"

  # ---- EXTRACTION (CONTENT OR REFUSAL) ----
  CONTENT=$(jq -r '.choices[0].message.content // empty' "$RESPONSE_JSON")
  REFUSAL=$(jq -r '.choices[0].message.refusal // empty' "$RESPONSE_JSON")

  TS_END="$(date -Iseconds)"

  if [[ -n "$CONTENT" ]]; then
    echo "$CONTENT" > "$RAW_TXT"
    STATUS="completed"
    REASON="content"
  elif [[ -n "$REFUSAL" ]]; then
    echo "REFUSAL: $REFUSAL" > "$RAW_TXT"
    STATUS="inconclusive"
    REASON="refusal"
  else
    echo "EMPTY_ASSISTANT_MESSAGE" > "$RAW_TXT"
    STATUS="inconclusive"
    REASON="empty_message"
  fi

  echo "{\"run_id\":\"$RUN_ID\",\"start\":\"$TS_START\",\"end\":\"$TS_END\",\"status\":\"$STATUS\",\"reason\":\"$REASON\"}" >> "$LOG_FILE"
done

echo "Execution complete. Outputs in runs/raw/"
