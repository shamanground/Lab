@"
# =========================================================
# Experiment 2 — Axis Existence
# Execution Order Script (MANUAL EXECUTION)
# =========================================================
# This script enforces run order and logging discipline.
# It does NOT execute the model.
# =========================================================

Write-Host ""
Write-Host "=== EXPERIMENT 2: EXECUTION ORDER ==="
Write-Host ""

$runs = @(
    "claim01_baseline",
    "claim01_control",
    "claim01_primary",
    "claim02_baseline",
    "claim02_control",
    "claim02_primary",
    "claim03_baseline",
    "claim03_control",
    "claim03_primary",
    "claim04_baseline",
    "claim04_control",
    "claim04_primary",
    "claim05_baseline",
    "claim05_control",
    "claim05_primary"
)

$counter = 1

foreach ($run in $runs) {
    Write-Host ""
    Write-Host "----------------------------------------"
    Write-Host "RUN $counter / 15"
    Write-Host "Run ID: $run"
    Write-Host "----------------------------------------"
    Write-Host "1. Assemble prompt manually"
    Write-Host "2. Execute single-turn response"
    Write-Host "3. Save raw output to:"
    Write-Host "   runs\raw\$run.txt"
    Write-Host "4. Do NOT retry"
    Write-Host "5. Press ENTER to continue"
    Read-Host
    $counter++
}

Write-Host ""
Write-Host "=== EXECUTION COMPLETE ==="
Write-Host "Proceed to structural coding only."
Write-Host ""
"@ | Set-Content run_order.ps1
