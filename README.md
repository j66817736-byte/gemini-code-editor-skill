# Gemini CLI Code Editor Skills (proposals)

Reviewable Agent Skill proposals for Gemini CLI. They guide the agent to understand existing code and data flow before focused changes, protect behavior-sensitive values, run relevant checks, preserve approved project context across sessions, and report limitations honestly.

These skills provide instructions only. They do not add executable tools, permissions, phone support, chat-history access, or synchronization, and they do not change Gemini CLI itself. They rely on tools available in the user's Gemini CLI environment. The project owner can review and test them before deciding whether to keep, revise, or submit them.

## Included skills

- **`code-editor`** (`.gemini/skills/code-editor/SKILL.md`): understand and safely modify existing code, verify changes, and avoid unauthorized branch or publishing actions.
- **`conversation-continuity`** (`.gemini/skills/conversation-continuity/SKILL.md`): maintain a concise, user-approved `PROJECT_CONTEXT.md` handoff to reduce repeated explanations across chats and devices.

## Phone and conversation continuity

The continuity skill does **not** automatically access or synchronize all conversations, and it does not install or run itself on a phone. It can help maintain a short handoff file that you choose to make available in the next session. A phone-centered workflow and syncing selected context across devices would require a compatible app or documented integration, user-granted access, and separate testing. Do not treat a repository stored in cloud storage as proof that chat history is synchronized or that the skills execute there.

Use separate context files for unrelated projects. Keep only necessary project notes, exclude secrets, and review content before sharing or publishing it. Offline availability depends on the storage app and its sync setup; cloud synchronization may require internet.

## Local code-editor example

The included Python example uses only the standard library. Its tests can be run from the repository root with:

```sh
python -m unittest discover -s examples/safe-edit -p 'test_*.py' -v
```

This does not require network access, API keys, or third-party test packages. To test the skills themselves, use a compatible Gemini CLI installation, open this repository as its workspace, and verify skill discovery and behavior. Gemini CLI still requires its own installation and authentication. Do not put credentials in the repository. Do not assume the Gemini mobile app or a phone browser loads CLI skills.

The sample test only checks the Python example; it does not test Gemini skill discovery, Android behavior, phone storage, or synchronization. No Android app has been built or tested here.

## Status and attribution

These are experimental proposals created from the project owner's ideas in collaboration with GitHub Copilot. They have not been submitted to or endorsed by Google, and they have not been tested in Gemini CLI in this environment. No changes have been made to Google's Gemini CLI repository. Review and test them before deciding whether or where to submit them.
