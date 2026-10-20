# AI Driver — public/export path privacy

This public/export privacy rule preserves a Human-established constraint. This document is **not** permission to publish, and does not add a new formal product success criterion.

## Rules

- Publicly distributed or externally exported AI Driver artifacts must not contain identifying absolute home-account paths. Apply to prose/docs, code examples, archives (file contents, entries and nested archives), structured JSON/YAML, build/CI logs, errors, review evidence, screenshots and exposed metadata.
- Show `<USER_HOME>/project/...` in public documentation. For Windows CMD use `%USERPROFILE%`; for PowerShell use `$HOME` or `$env:USERPROFILE`; for Unix shells use `$HOME` or `~` appropriately. Use proper programmatic home APIs when available. Resolve runtime paths; never execute a documentation placeholder verbatim.
- Restricted primary audit evidence is not rewritten just to sanitize; create a separately identified sanitized derivative with provenance and validation. Do not export raw private files merely because a scan passes.
- Detect risky personal-home absolute paths before public release or external export; ensure tool-produced scan reports do not print the secrets that triggered detection. Include filenames and ZIP members/nested content. Unsupported files or metadata, raster images/screenshots, PDFs and non-text encodings require separate inspection. Do not infer safe/public from absence of detections in a limited scanner.
- Release decision states: `BLOCK` for actual matches, `REVIEW_REQUIRED` for uninspected/unsupported content, and candidate `PASS` only for material explicitly within qualified scanner scope and required other reviews. If any BLOCK/REVIEW remains unresolved, stop the **affected external publication/export operation only**; continue unrelated authorized private engineering. Even `PASS` never permits publishing without separate explicit Human approval and required checks.
- An optional local prototype scanner is only a **development test**: it is not embedded in the host's release pipeline, an OS-wide monitor, or an automatic blocker. Only run a verifier with actual supported authorized tools and retain test evidence. If the verifier cannot run and be checked, return `NOT_ESTABLISHED`, not `PASS`.

## Pre-release handoff fields

`DECISION_ID`, `SOURCE_KIND`, `PUBLIC_CANDIDATE`, `SCAN_TARGET_SCOPE`, `SCAN_TOOL_VERSION`, `SCAN_RESULT`, `UNREVIEWED_CONTENT`, `REDACTED_DERIVATIVE`, `ORIGINAL_EVIDENCE_RETAINED`, `HUMAN_PUBLICATION_AUTHORIZATION`, `NEXT_OWNER/ACTION`. These are **guidance for release evidence**, not required fields for ordinary private state or generic tasks. Do not write private path values into handoffs.
