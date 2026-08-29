"""Deterministic local stand-in for agentic workflow detector fixtures."""
from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True)
    parser.add_argument("--prompt", default="")
    parser.add_argument("--prompt-file", default="")
    parser.add_argument("--mcp-config", default="")
    parser.add_argument("--output", default="")
    parser.add_argument("--verdict", default="")
    parser.add_argument("--yes", action="store_true")
    args, _ = parser.parse_known_args()
    print(f"GRAFTER_MARKER_{args.scenario.upper().replace('-', '_')}")


if __name__ == "__main__":
    main()

