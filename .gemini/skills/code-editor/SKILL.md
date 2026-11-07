---
name: code-editor
description: Understand, explain, write, and safely modify code by tracing its architecture and data flow. Use when investigating, implementing, debugging, or optimizing changes in an existing codebase.
---

# Code Editor

Understand the existing code before changing it. Trace the relevant data flow, explain the reasoning, and make the smallest change that fulfills the request. Do not create or modify skills unless the user specifically asks.

## Workflow

1. **Confirm the goal and project.**
   - Inspect the available repository and identify its language, platform, and relevant components.
   - Establish what behavior should change and what must remain unchanged.
   - If the requested project or files are unavailable, say so; do not claim to have changed or tested them.

2. **Trace the behavior.**
   - Follow relevant data from input through validation, transformation, processing, storage, and output.
   - Inspect callers, types, configuration, related tests, and existing safeguards.
   - Separate necessary data and work from duplicated or optional processing; do not discard information without evidence.
   - Explain the important parts of the flow and the reasoning behind a proposed change in clear language.

3. **Protect exact values and behavior.**
   - Treat numeric literals, decimal points, units, thresholds, rounding, signs, indexes, and conditions as behavior-sensitive.
   - Do not alter them unless the request requires it and the code or tests support the change.
   - When a value or intended behavior is ambiguous, ask before changing it.
   - Compare existing and proposed behavior, including relevant boundary cases, before editing.

4. **Make the smallest appropriate change.**
   - Follow established project patterns and reuse existing components.
   - Avoid unrelated refactors, dependencies, and new abstractions.
   - Preserve required data, ordering, privacy, compatibility, and security checks.
   - Do not claim a performance improvement without evidence from the code or measurements.

5. **Keep repository actions under user control.**
   - Work on the current branch by default. Do not create or switch branches, open pull requests, publish releases, deploy, or submit changes externally unless the user explicitly authorizes that action.
   - Before making a broad or potentially destructive change, explain the scope and ask for confirmation.
   - Never treat permission to edit code as permission to publish, deploy, or contact third parties.

6. **Verify the change.**
   - Add or update focused tests for the requested behavior and likely regressions.
   - Run relevant tests and checks available in the repository.
   - Review the complete diff for unintended edits, especially changed constants, configuration, and unrelated files.
   - If a check cannot be run, state that clearly and do not imply it passed.

7. **Respect the target environment.**
   - For Android, work with the app’s actual architecture; do not treat Termux or an emulator as a substitute for the target app or device.
   - Verify offline, voice, accessibility, and device-specific behavior rather than assuming it works.
   - Consider CPU, memory, battery, and thermal impact; avoid unnecessary polling and background work.

8. **Report clearly.**
   - Summarize what changed, why it is safe, and how the data-flow analysis informed it.
   - List the tests and checks actually run and any remaining limitations.
