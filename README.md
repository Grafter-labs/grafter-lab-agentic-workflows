# Grafter agentic-workflow lab

These workflows demonstrate detector shapes with a local deterministic mock
agent. The mock only prints a `GRAFTER_MARKER`; it never contacts an AI
provider, executes generated text, changes git state, or calls GitHub APIs.

Runnable marker jobs use GitHub-hosted runners and read-only behavior. Detector
sink strings such as `actions/github-script` are inert metadata passed to the
mock. Tool execution, secret context, auto-apply, verdict authorization, and
write-shaped examples have job-level `if: ${{ false }}` guards.

`fixture-upstream.yml` exists only to establish the untrusted upstream side of
the `workflow_run` correlation. Do not add provider keys or enable write tools.

