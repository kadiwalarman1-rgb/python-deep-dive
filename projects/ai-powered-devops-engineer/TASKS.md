# Implementation Checklist

Status: [ ] not started, [-] in progress, [x] verified complete, [!] blocked.

## Foundation
- [x] Create project folder and initial architecture documents.
- [x] Define local-first and no-automatic-remediation boundaries.
- [ ] Install packages and execute tests in a Python environment.
- [ ] Verify application startup locally.

## Core functionality
- [x] Parse plain-text logs and JSON Lines.
- [x] Normalize timestamps and classify levels.
- [x] Calculate metrics and repeated-error findings.
- [x] Detect configurable error-count spikes.
- [x] Export JSON and Markdown reports.
- [ ] Expand edge-case tests and fixtures.
- [ ] Run tests and fix failures.

## Dashboard and AI
- [x] Build Streamlit workflow for sample data and uploads.
- [x] Add a clearly labeled offline demo diagnosis provider.
- [x] Add optional Bedrock adapter with explicit consent.
- [x] Add basic secret redaction before external AI calls.
- [ ] Verify Bedrock with configured account and model.
- [ ] Test invalid, timed-out, and unavailable provider behavior.

## Security and packaging
- [x] Add upload size limits and safe parsing.
- [x] Add ignore rules and environment example.
- [ ] Run Ruff, Bandit, and dependency audit.
- [ ] Build and run the Docker image.
- [ ] Review package versions and licensing.

## Future integrations
- [ ] Add optional Docker health monitoring.
- [ ] Add read-only CloudWatch Logs integration and narrow IAM policy.
- [ ] Review deployment options and costs before provisioning resources.

## Portfolio
- [x] Add README, plan, architecture, and threat model.
- [ ] Capture real screenshots after running the app.
- [ ] Record actual test results and coverage.
- [ ] Validate GitHub Actions remotely.
- [ ] Prepare final resume bullets after verification.

## Checkpoint
Initial files are on the feature branch. Runtime testing has not been executed through this GitHub connection. Next: install dependencies locally, run pytest and Ruff, fix issues, then continue monitoring integrations.
