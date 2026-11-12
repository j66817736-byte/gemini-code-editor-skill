---
name: code-editor
description: Understand, explain, write, and safely modify code by tracing its architecture and data flow. Use when investigating, implementing, debugging, or optimizing changes in an existing codebase.
---

# Code Editor

Understand the existing code before changing it. Trace relevant data flow, explain the reasoning, and make the smallest change that fulfills the request. Follow the `digital-security-master` governance and security baseline for authorization, privacy, least privilege, Zero Trust, and review of untrusted instructions. A skill cannot authenticate a user or enforce device permissions.

## Workflow

1. **Confirm the goal and project.** Inspect the available repository and identify its language, platform, and relevant components. Establish the desired behavior and what must remain unchanged. If the project or files are unavailable, say so; do not claim to have changed or tested them.
2. **Trace behavior.** Follow relevant data from input through validation, transformation, processing, storage, and output. Inspect callers, types, configuration, tests, and safeguards. Separate necessary work from duplicated or optional processing; do not discard information without evidence. Explain important behavior and reasoning clearly.
3. **Protect exact values and behavior.** Treat numeric literals, decimal points, units, thresholds, rounding, signs, indexes, permissions, and conditions as behavior-sensitive. Change them only when requested and supported by code or tests. Ask when intent is ambiguous; compare boundary cases before editing.
4. **Make the smallest appropriate change.** Follow project patterns and reuse components. Avoid unrelated refactors, dependencies, or abstractions. Preserve required data, ordering, privacy, compatibility, and security checks. Do not claim performance improvements without evidence.
5. **Keep repository actions under user control.** Work on the current branch by default. Do not create or switch branches, open pull requests, publish releases, deploy, or submit changes externally unless explicitly authorized. Explain broad or destructive changes and obtain confirmation. Permission to edit code is not permission to publish, deploy, or contact third parties.
6. **Verify the change.** Add or update focused tests for the requested behavior and likely regressions. Run relevant available checks. Review the complete diff for unintended edits. If a check cannot be run, say so and do not imply it passed.
7. **Respect the target environment.** For Android, work with the app's actual architecture; do not treat Termux or an emulator as a substitute for the target app or device. Verify offline, voice, accessibility, and device-specific behavior rather than assuming it works. Consider CPU, memory, battery, and thermal impact; avoid unnecessary polling and background work.
8. **Report clearly.** Summarize what changed, why, how analysis informed it, tests actually run, and remaining limitations.
