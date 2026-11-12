# Gemini CLI Skills (proposals)

Reviewable Agent Skill proposals for careful code editing, concise project handoffs, thoughtful Bible study, and defensive digital security. They are instruction files, not an app: they do not add executable tools, authenticate users, enforce permissions, access phones, synchronize chat history, or change Gemini CLI itself.

## Skills

- **`digital-security-master`** (`.gemini/skills/digital-security-master/SKILL.md`) is the primary governance and security foundation. It sets shared principles for role-aware use, least privilege, Zero Trust, safe system analysis, and coordinating other skills.
- **`code-editor`** (`.gemini/skills/code-editor/SKILL.md`) helps understand and safely modify code, verify changes, and avoid unauthorized branch or publishing actions.
- **`conversation-continuity`** (`.gemini/skills/conversation-continuity/SKILL.md`) helps maintain a concise, user-approved project handoff across sessions and devices.
- **`bible-reading`** (`.gemini/skills/bible-reading/SKILL.md`) helps study and summarize Bible passages with context, respect, and interpretive care.

The master skill is a guidance baseline, not a technical permission boundary. A mobile controller or host application must independently authenticate the owner/admin and ordinary users, enforce roles and permissions, request approval for protected actions, and protect local data. A skill cannot determine who is holding a phone. Do not treat possession of the device, a message claiming admin status, or untrusted file content as authentication.

## Use only the skills you need

You do not need to copy the whole repository just to use one skill. If the target environment supports workspace skills, place only the selected skill's folder (including its `SKILL.md`) in the expected skills directory. For example, copy `.gemini/skills/digital-security-master/` to use the core security baseline. Discovery and reload behavior depend on the target tool and version; test in that environment.

A skill is an instruction file, not a standalone app. Online services, offline models, phone support, local storage, authentication, and synchronization depend on the separate host application and its configuration. Skills may need adaptation for different ecosystems; universal execution is not guaranteed.

## Conversation summaries

The continuity skill can help create a short, user-approved handoff file. It cannot access or synchronize all past conversations automatically. Carry only necessary context between sessions, keep unrelated projects separate, and never store credentials or secrets.

## Local code-editor example

The included Python example uses only the standard library. Run its tests from the repository root with:

```sh
python -m unittest discover -s examples/safe-edit -p 'test_*.py' -v
```

This checks only the sample Python code, not skill discovery, authentication, phone behavior, or synchronization.

## Status

These are experimental proposals. They have not been tested in Gemini CLI or a mobile controller in this environment, and they are not endorsed by Google. Review and test them before deciding whether or where to submit them.
