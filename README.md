# Grafter agentic-workflow lab

These workflows demonstrate detector shapes with a local deterministic mock
agent. The mock only prints a `GRAFTER_MARKER`; it never contacts an AI
provider, executes generated text, changes git state, or calls GitHub APIs.

All event-driven detector fixtures have job-level `if: ${{ false }}` guards.
Detector sink strings such as `actions/github-script` are inert metadata passed
to the mock. `safe-marker-demo.yml` is the only runnable workflow; it uses
manual dispatch, fixed trusted input, a GitHub-hosted runner, and read-only
permissions.

`fixture-upstream.yml` exists only to establish the untrusted upstream side of
the `workflow_run` correlation. Do not add provider keys or enable write tools.
