# Gemini CLI Code Editor Skill (proposal)

A small, reviewable Agent Skill proposal for Gemini CLI. It guides Gemini to understand existing code and data flow before making focused changes, protect behavior-sensitive values (including decimals, units, and thresholds), run relevant checks, and report limitations honestly.

This skill is **not** a skill-creation skill, does not add executable tools or permissions, and does not change Gemini CLI itself. It relies on tools already available in the user's Gemini CLI environment. The project owner can test it in a separate project and decide whether to keep, revise, or remove it.

## Try it locally

From the root of a project where Gemini CLI is installed, copy the skill folder into that project's workspace skills directory:

```sh
mkdir -p .gemini/skills
cp -R /path/to/gemini-code-editor-skill/.gemini/skills/code-editor .gemini/skills/
```

Start Gemini CLI in that project and ask it to explain a small, well-understood code path first. Then try a low-risk change with existing tests. Review the diff and run the project's normal checks yourself. Do not use a production repository or sensitive data for an initial trial.

If Gemini CLI does not discover the skill, consult the documentation for the installed CLI version for supported skill discovery and reload behavior. Do not assume the skill grants access to tools, devices, credentials, or permissions that the environment has not provided.

## Suggested trial report

Record the Gemini CLI version, project/language, prompt, whether the skill was discovered, files changed, tests actually run and their results, any incorrect assumptions, and whether the skill's safeguards were followed. Share only information you are authorized to disclose.

## Status and attribution

This is an experimental proposal created from the project owner's ideas in collaboration with GitHub Copilot. It has not been submitted to or endorsed by Google, and it has not been tested in Gemini CLI in this environment. No changes have been made to Google's Gemini CLI repository. The project owner should review and test it before deciding whether or where to submit it.
