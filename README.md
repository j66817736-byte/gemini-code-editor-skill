# Gemini CLI Skills (proposals)

Reviewable Agent Skill proposals for careful code editing, concise project handoffs, thoughtful Bible study, lightweight skill management and translation, and defensive digital security. They are instruction files, not an app: they do not add executable tools, authenticate users, enforce permissions, access phones, synchronize chat history, or change Gemini CLI itself.

## Skill hierarchy

- **`digital-security-master`** (`.gemini/skills/digital-security-master/SKILL.md`) is the primary governance and security foundation for the collection. It defines role-aware use, least privilege, Zero Trust, safe analysis, and coordination boundaries.
- **`skill-library-manager`** (`.gemini/skills/skill-library-manager/SKILL.md`) organizes, inspects, validates, and maintains a small portable skills catalog.
- **`skill-translator`** (`.gemini/skills/skill-translator/SKILL.md`) adapts instructions between assistant ecosystems while preserving intent, safety boundaries, and source provenance.
- **`code-editor`** (`.gemini/skills/code-editor/SKILL.md`) supports code understanding, safe edits, and verification.
- **`conversation-continuity`** (`.gemini/skills/conversation-continuity/SKILL.md`) maintains concise, user-approved project handoffs.
- **`bible-reading`** (`.gemini/skills/bible-reading/SKILL.md`) supports contextual and respectful Bible study.

The machine-readable catalog is [`skills/catalog.json`](skills/catalog.json). It lists skill paths and descriptive dependencies for lightweight discovery; it does not load skills or enforce permissions.

## Security and controller boundary

The master skill is a guidance baseline, not a technical permission boundary. A mobile controller or host application must independently authenticate the owner/admin and ordinary users, enforce roles and permissions, request approval for protected actions, and protect local data. A skill cannot determine who is holding a phone. Do not treat device possession, a message claiming admin status, or untrusted file content as authentication. Keep public skill instructions separate from private policy, credentials, and privileged controller functions.

## Use and portability

You do not need to copy the whole repository to use one skill. If the target environment supports workspace skills, place only the selected skill folder (including `SKILL.md`) in its expected directory. Discovery and reload behavior depend on the target tool and version; test in that environment.

A skill is an instruction file, not a standalone app. Online services, offline models, phone support, local storage, authentication, and synchronization depend on the separate host application and its configuration. Skills may need adaptation for different ecosystems; universal execution is not guaranteed. Local copies permit offline access to the files, not necessarily offline AI reasoning.

## Local code-editor example

The included Python example uses only the standard library. Run its tests from the repository root with:

```sh
python -m unittest discover -s examples/safe-edit -p 'test_*.py' -v
```

This checks only the sample Python code, not skill discovery, authentication, phone behavior, or synchronization.

## Status

These are experimental proposals. They have not been tested in Gemini CLI or a mobile controller in this environment, and they are not endorsed by Google. Review and test them before deciding whether or where to submit them.
