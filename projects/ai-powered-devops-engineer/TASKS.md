# Implementation Checklist

Status: [ ] not implemented, [-] implemented but verification pending, [x] implemented and verified, [!] blocked.

## Foundation
- [-] Create project folder and initial architecture documents.
- [-] Define local-first and no-automatic-remediation boundaries.
- [ ] Install packages and execute tests in a Python environment.
- [ ] Verify application startup locally.

## Core functionality
- [-] Parse plain-text logs and JSON Lines.
- [-] Normalize timestamps and classify levels.
- [-] Calculate metrics and repeated-error findings.
- [-] Detect configurable error-count spikes.
- [-] Export JSON and Markdown reports.
- [ ] Expand edge-case tests and fixtures.
- [ ] Run tests and fix failures.

## Dashboard and AI
- [-] Build Streamlit workflow for sample data and uploads.
- [-] Add a clearly labeled offline demo diagnosis provider.
- [-] Add optional Bedrock adapter with explicit consent.
- [-] Add basic secret redaction before external AI calls.
- [ ] Verify Bedrock with configured account and model.
- [ ] Test invalid, timed-out, and unavailable provider behavior.

## Security and packaging
- [-] Add upload size limits and safe parsing.
- [-] Add ignore rules and environment example.
- [ ] Run Ruff, Bandit, and dependency audit.
- [ ] Build and run the Docker image.
- [ ] Review package versions and licensing.

## Future integrations
- [-] Add optional Docker health/status reader and consent-gated dashboard UI; runtime verification pending.
- [-] Add read-only CloudWatch Logs reader, dashboard UI, and narrow policy template; runtime verification pending.
- [ ] Review deployment options and costs before provisioning resources.

## Portfolio
- [-] Add README, plan, architecture, and threat model.
- [ ] Capture real screenshots after running the app.
- [ ] Record actual test results and coverage.
- [ ] Validate GitHub Actions remotely.
- [ ] Prepare final resume bullets after verification.

## Checkpoint
Initial files are on the feature branch. Runtime testing has not been executed through this GitHub connection. Next: install dependencies locally, run pytest and Ruff, fix issues, then continue monitoring integrations.
