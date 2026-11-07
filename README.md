# Gemini CLI Code Editor Skill (proposal)

A small, reviewable Agent Skill proposal for Gemini CLI. It guides Gemini to understand existing code and data flow before making focused changes, protect behavior-sensitive values (including decimals, units, and thresholds), run relevant checks, and report limitations honestly.

This skill is **not** a skill-creation skill, does not add executable tools or permissions, and does not change Gemini CLI itself. It relies on tools already available in the user's Gemini CLI environment. The project owner can test it in a separate project and decide whether to keep, revise, or remove it.

## Try it without Android

You do **not** need an Android device or SDK to check whether Gemini CLI discovers and follows this skill on a small code-editing task. The included Python example uses only the standard library, so running its tests does not require network access, API keys, or third-party packages.

1. Clone or download this repository into an environment where Gemini CLI is installed. Open this repository as the Gemini CLI workspace so it can discover `.gemini/skills/code-editor/SKILL.md`.
2. Ask Gemini CLI to explain `examples/safe-edit/converter.py` and its tests without editing. Check whether it traces the code and identifies the conversion factor.
3. Then ask it to add an inverse conversion function while preserving the existing conversion factor exactly and adding tests. Review the diff yourself.
4. From the repository root, run:

   ```sh
   python -m unittest discover -s examples/safe-edit -p 'test_*.py' -v
   ```

5. Compare the output, tests, and diff with what you expected. Revert the example changes after the trial if you want to keep this repository unchanged.

The local Python tests need no internet or API keys. **Gemini CLI itself still needs to be installed and authenticated** to use Gemini; this repository does not include credentials. Never put API keys, tokens, or passwords in the skill, example files, prompts committed to the repository, or Git history. Do not assume the Gemini mobile app or a phone browser loads CLI skills.

If Gemini CLI is unavailable, you can still run the Python tests, but that only checks the sample code; it does not test skill discovery or Gemini's behavior. No Android app is built or tested by this example.

## Try it on an Android project later

Once you have access to that app's source code and a Gemini CLI environment, use a small, isolated change first. The skill can help inspect and edit code without an Android device, but validating builds, device compatibility, offline operation, voice input, accessibility, battery, or thermal behavior may require the project's Android build environment and/or a real device. Record exactly which checks you were able to run.

## Suggested trial report

Record the Gemini CLI version, project/language, prompt, whether the skill was discovered, files changed, tests actually run and their results, any incorrect assumptions, and whether the skill's safeguards were followed. Share only information you are authorized to disclose; redact secrets and personal data.

## Status and attribution

This is an experimental proposal created from the project owner's ideas in collaboration with GitHub Copilot. It has not been submitted to or endorsed by Google, and it has not been tested in Gemini CLI in this environment. No changes have been made to Google's Gemini CLI repository. The project owner should review and test it before deciding whether or where to submit it.
