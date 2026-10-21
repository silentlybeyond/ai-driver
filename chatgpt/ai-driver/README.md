# AI Driver — ChatGPT source edition

This directory preserves the **ChatGPT-specific source** of AI Driver, alongside the separate Claude edition in this repository. It is a source snapshot based on private plugin version **0.1.12-poc13**, published here as inspectable source; it is **not** an OpenAI Plugin Directory listing or an OpenAI-approved public ChatGPT plugin.

## What it does

AI Driver helps the assistant pursue continuing goals within available tools and permissions: define completion criteria, plan work, delegate bounded tasks, verify outputs, preserve state, and resume unfinished projects. Human decisions and actual tool permissions remain authoritative.

## Use privately in ChatGPT (manual import, where supported)

GitHub source distribution is **not** an official OpenAI directory listing. To install for your own use, download a **purpose-built package** from this repository's `dist/` folder, not the GitHub-generated "Download ZIP" archive.

- **Personal Skill:** Download the [ChatGPT Skill import ZIP](../../dist/ai-driver-chatgpt-skill-v0.1.12-poc13.zip). If your account has the Skills feature, go to **Plugins → Skills → Create → Upload from your computer**, upload it, review the scan result and leave it unshared. OpenAI currently generally offers personal Skills for eligible Business, Enterprise, Healthcare and Edu accounts; availability varies by account and workspace.
- **Private plugin:** Download the [ChatGPT Plugin import ZIP](../../dist/ai-driver-chatgpt-plugin-v0.1.12-poc13.zip). If **Plugins → Add → Upload plugin** (or **Upload new or existing plugin**) is available and you have permission, upload the ZIP and keep it private. Do not submit or publish it to the public directory.

[日本語インストールガイド](INSTALL.ja.md) — package structure, step-by-step instructions, troubleshooting and limitations.

**Qualification status:** A purpose-equivalent PRIVATE plugin package was successfully imported using OpenAI Plugin Creator on October 21, 2026, and all 13 registered files were listed afterwards. Only the isolated test plugin identity differed in two manifest files. This verifies PRIVATE plugin creation in one authorized account—not automatic skill activation, runtime behavior, Skill-only ZIP import, or universal availability.

## ChatGPT Work qualification (2026-10-21)

**Qualification level: PASS as reported by a single user of the installed PRIVATE plugin, within the test scopes below.** The owner-provided Work execution reports were reviewed, but the maintainer could not independently access the original local evidence files for a separate byte-level examination or test replay. This is **not** platform-wide certification or an OpenAI endorsement.

| Test | Reported result | Scope |
| --- | --- | --- |
| W-01 | PASS | Private plugin was selected/identified in a Work session. |
| W-02 | PASS | Installed Skill and mandatory requirements/conflict references read with actual filesystem tools. |
| W-03 | PASS | The assistant preserved the parent goal, success criteria and Human-reserved publication rights while selecting the next action. |
| W-04 | PASS | A local isolated browser task-management app was implemented and tested: **8 Node unit assertions + 12 Edge headless browser assertions** reported PASS; reload and browser-restart persistence were included. An initial FAIL was preserved and the test harness repaired before successful rerun. |
| W-05 | PASS | In a **new Work session**, a saved handoff, application source and test JSON were read from a **supplied local filesystem location**. Goal, acceptance conditions, previous test results, failure history and Human authority were reconstructed without referring to the previous chat. |

**Important evidence limits:** W-05 read *saved* execution records; it did **not rerun** W-04 tests. The original Edge process-exit boundary, prior process logs and exact superseded harness code could not be independently re-established from saved artifacts. Read-time SHA-256 values do not prove the files have never changed. The real project path, test JSON, log output and personal filesystem identifiers are intentionally **not published**. Only the source edition of AI Driver and generic distribution packages appear in this repository.

This confirms **user-reported Work execution and locator-assisted, cross-session file-based continuity** under the tested environment. It does *not* establish automatic Skill activation, automatic project discovery, automatic memory transfer, cross-account availability, personal-Skill ZIP import, GitHub/ChatGPT Library integration within Work, or a formal OpenAI Work compatibility certification. Explicit Skill selection and actual tool permissions were required; the Work host identity was reported by the user, not independently attested by a host token in the evidence provided.

## Contents

- `plugin.json` and `.codex-plugin/plugin.json`: original ChatGPT-specific plugin manifests (pseudonymous publisher name).
- `skills/ai-driver/SKILL.md`: behavior contract for ongoing multi-step work.
- `skills/ai-driver/references/`: requirements, conflict rules, host state contract, ChatGPT Library adapter, privacy rules, and original Japanese requirements.
- `skills/ai-driver/templates/`: optional state snapshot template.
- `LICENSE`: MIT license.

## Important limitations

- This folder is **source code, not a hosted service**. Merely cloning the repository does not install it into ChatGPT or confer Plugin Directory distribution rights.
- The ChatGPT Library adapter is conditional: it uses only file tools actually available and authorized in the running account/session. No automatic cross-chat recall, tool invocation, or persistence is guaranteed.
- No credential, storage permission, public posting, destructive action, or final project approval is authorized just by reading these files.
- Do **not** place user project states, personal files, credentials, machine-specific paths, or private evaluation logs into this public repository.
- The source remains a previously developed ChatGPT adapter. The above user-reported W-01–W-05 Work tests support a **bounded execution/continuity qualification** for one private installation, but are not an independent replay, third-party account test, automatic-invocation qualification or official Directory review.

For the published Claude edition and overall project background, see the repository root `README.md`.
