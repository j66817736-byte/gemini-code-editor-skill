# Gemini CLI Skills (proposals)

Reviewable Agent Skill proposals for Gemini CLI. They provide instructions for careful code editing, concise project handoffs, and thoughtful Bible study. They do not add executable tools, permissions, phone support, chat-history access, or synchronization, and they do not change Gemini CLI itself.

## Included skills

- **`code-editor`** (`.gemini/skills/code-editor/SKILL.md`): understand and safely modify existing code, verify changes, and avoid unauthorized branch or publishing actions.
- **`conversation-continuity`** (`.gemini/skills/conversation-continuity/SKILL.md`): maintain a concise, user-approved project handoff to reduce repeated explanations across chats and devices.
- **`bible-reading`** (`.gemini/skills/bible-reading/SKILL.md`): help study and summarize Bible passages with context, respect, and interpretive care.

## Use only the skill you need

You do not need to copy the whole repository just to use one skill. If your Gemini CLI version supports workspace skills, place only that skill's folder (including its `SKILL.md`) in the target project's `.gemini/skills/` directory. For example, copy `.gemini/skills/bible-reading/` when you only want the Bible-reading skill. Skill discovery and reload behavior depend on your installed Gemini CLI version; consult its documentation if the skill is not detected.

A skill is an instruction file, not a standalone app. Gemini CLI must be installed and authenticated in the environment where you use it. These files do not automatically run in the Gemini mobile app or synchronize chats.

## Conversation summaries

The continuity skill can help create a short, user-approved handoff file so you do not have to repeat project background. It cannot access or synchronize all past conversations automatically. Keep only the necessary context, separate unrelated projects, and never store credentials or secrets. You choose which summary to carry into another chat or device.

## Local code-editor example

The included Python example uses only the standard library. Run its tests from the repository root with:

```sh
python -m unittest discover -s examples/safe-edit -p 'test_*.py' -v
```

This checks only the sample Python code, not Gemini skill discovery or phone behavior. The tests do not require network access, API keys, or third-party packages.

## Status

These are experimental proposals. They have not been tested in Gemini CLI in this environment or endorsed by Google. Review and test them before deciding whether or where to submit them.
