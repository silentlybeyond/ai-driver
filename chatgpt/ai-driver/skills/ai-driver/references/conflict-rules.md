# Conflict-resolution rules — v0.1.0-rc6 review candidate

## Previously approved C-01–C-15

| Rule | Resolution |
|---|---|
| C-01 | Preserve parent success conditions; permit authorized changes to lower-level means. |
| C-02 | Superseded/cancelled work is not completed work. |
| C-03 | Discretion exists only at levels explicitly delegated. |
| C-04 | Intermediate-purpose drivers do not create unnecessary subtasks. |
| C-05 | Individual task PASS does not conclude the delegated intermediate objective. |
| C-06 | Subordinate driver makes authorized decisions; do not bounce options upward unnecessarily. |
| C-07 | No repeated approvals for routine steps already delegated. |
| C-08 | Material parent-purpose/risk problems require appropriate escalation; no unauthorized major repair. |
| C-09 | End delegated responsibility when the intermediate objective's conditions and evidence are met. |
| C-10 | Material decisions, changes and completion must be recorded for continuity. |
| C-11 | Do not infer unstated delegation or independently grant additional authority. |
| C-12 | An agent cannot re-delegate tools/permissions it does not have or cannot re-delegate. |
| C-13 | Separate current valid tasks from superseded historical records. |
| C-14 | Request specific unavailable essential information; do not silently fill gaps. |
| C-15 | Record reasons, evidence, alternatives and risks for material autonomous decisions. |

## Derived cross-requirement resolutions C-16–C-23

These implement the consolidated requirements' implications; earlier review proposed them as a set. Final public release approval should explicitly confirm the whole candidate including these interpretations.

| Rule | Resolution |
|---|---|
| C-16 | Independently evaluate child and parent completion conditions. |
| C-17 | For established top-level completion, `NEXT_ACTION = NONE` is valid. |
| C-18 | A Human question is answered; it alone creates no new permission. |
| C-19 | Request material missing information rather than guessing. |
| C-20 | Carry verified completion into new sessions; do not casually reopen it. |
| C-21 | Material counterevidence after completion is escalated, not silently overwritten. |
| C-22 | Distinguish `READY_TO_DISPATCH`, `DISPATCHED`, `ACKNOWLEDGED`, `EXECUTED`. |
| C-23 | Treat incidental improvement as R-10; material higher-purpose danger as R-06. |

## Approved supplemental interpretations

- **No executable action:** Disclose accountable owner, wait/blocker reason, resume condition and needed next decision or information, without inventing work or approvals.
- **No obligatory central owner:** Concurrent updates must not destroy valid state. Keep conflicting changes separately with origin/base version/evidence. Authorized non-conflicting changes may be reconciled. Unresolved material conflicts in purposes, Human decisions, authority and completion are escalated to an appropriate Human; unrelated safe tasks may proceed.
