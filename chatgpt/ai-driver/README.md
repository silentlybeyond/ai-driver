# AI Driver — ChatGPT source edition

This directory preserves the **ChatGPT-specific source** of AI Driver, alongside the separate Claude edition in this repository. It is a source snapshot based on private plugin version **0.1.12-poc13**, prepared as a public candidate; it is **not** an OpenAI Plugin Directory listing or an approved public ChatGPT plugin.

## What it does

AI Driver helps the assistant pursue continuing goals within available tools and permissions: define completion criteria, plan work, delegate bounded tasks, verify outputs, preserve state, and resume unfinished projects. Human decisions and actual tool permissions remain authoritative.

## Use privately in ChatGPT (manual import, where supported)

GitHub source distribution is **not** an official OpenAI directory listing. To install for your own use, download a **purpose-built package** from this repository's `dist/` folder, not the GitHub-generated "Download ZIP" archive.

- **Personal Skill:** Download the [ChatGPT Skill import ZIP](../../dist/ai-driver-chatgpt-skill-v0.1.12-poc13.zip). If your account has the Skills feature, go to **Plugins → Skills → Create → Upload from your computer**, upload it, review the scan result and leave it unshared. OpenAI currently generally offers personal Skills for eligible Business, Enterprise, Healthcare and Edu accounts; availability varies by account and workspace.
- **Private plugin:** Download the [ChatGPT Plugin import ZIP](../../dist/ai-driver-chatgpt-plugin-v0.1.12-poc13.zip). If **Plugins → Add → Upload plugin** (or **Upload new or existing plugin**) is available and you have permission, upload the ZIP and keep it private. Do not submit or publish it to the public directory.

[日本語インストールガイド](INSTALL.ja.md) — package structure, step-by-step instructions, troubleshooting and limitations.

**Qualification status:** A purpose-equivalent PRIVATE plugin package was successfully imported using OpenAI Plugin Creator on October 21, 2026, and all 13 registered files were listed afterwards. Only the isolated test plugin identity differed in two manifest files. This verifies PRIVATE plugin creation in one authorized account—not automatic skill activation, runtime behavior, Skill-only ZIP import, or universal availability.

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
- The source is a previously developed ChatGPT adapter; public host execution and directory distribution were **not requalified by this archival candidate**.

For the published Claude edition and overall project background, see the repository root `README.md`.
