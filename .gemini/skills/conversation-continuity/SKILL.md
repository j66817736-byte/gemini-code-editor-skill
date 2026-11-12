---
name: conversation-continuity
description: Help maintain user-approved project context across chats and devices, including a phone-centered workflow. Use when the user asks to resume work, avoid repeating setup, or carry decisions and next steps between conversations.
---

# Conversation Continuity

Help the user continue project work across chats and devices without claiming access to conversations or storage that are not actually available. Treat current repository files and user-approved context as the source of truth.

## Start or resume work

1. Identify the current project and the user's immediate goal.
2. Look for the project's `PROJECT_CONTEXT.md` or another context file the user names. Read it before asking the user to repeat background.
3. Compare the handoff with current project files and instructions. Current files and the user's latest instructions take precedence over old notes.
4. If a necessary detail is missing, ask only the smallest relevant question. Do not invent decisions.
5. Never claim to have synchronized or reviewed chats, projects, accounts, or files that are not available in the current environment.

## Maintain a portable handoff

When the user asks to preserve context, or at the end of substantial work when appropriate, maintain a concise, dated `PROJECT_CONTEXT.md` containing only useful project information:

- Project purpose and status.
- Relevant paths and links.
- Decisions the user explicitly made.
- Work completed and checks actually run, distinguishing tested from untested.
- Constraints, preferences, next step, and unresolved questions.

Keep unrelated projects in separate handoff files. Prefer a format the user can access and carry from their phone. Update only the relevant project handoff. Ask before adding sensitive personal information or publishing it.

## Phone and cross-device synchronization

- A phone-centered workflow is a user requirement, not proof that this skill is installed or running on the phone. Confirm what app/environment is actually available before giving setup instructions.
- A handoff file can reduce repeated explanations only when the user makes it available in the next session. This skill does not itself run on Android, access a phone's storage, or sync across devices.
- Do not claim automatic synchronization of all conversations. Use only a specific, user-authorized export, file, or documented integration that is available. If chat-history access is unavailable, explain the limitation and offer a user-controlled handoff instead.
- For any future sync feature, minimize retained data, make sources and sync status visible, obtain permission before importing or sharing conversation content, and provide a way to review and remove stored context. Do not assume cloud sync works offline; describe what remains local and what requires a connection.

## Privacy and security

- Do not copy entire chat transcripts by default; keep only minimum necessary project context.
- Never put passwords, API keys, access tokens, private keys, recovery codes, or other secrets in handoff files, prompts committed to a repository, or version control.
- Inspect context for private information before committing or publishing it. Obtain explicit authorization before publishing private conversation details.
- Do not infer consent to synchronize information across accounts or external services from a request to maintain project continuity.

## Limits

A skill supplies instructions; it does not add phone support, permissions, storage, network access, chat-history access, or synchronization. Those require a compatible application and an explicitly configured, user-authorized integration. State these limits plainly and do not imply that a proposal has been tested unless it has.
