"""Compatibility entry point for running only the PyRIT red-team scan."""

from __future__ import annotations

import argparse
import asyncio

from master_dashboard import run_red_team_scan


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a single PyRIT red-team scan.")
    parser.add_argument("objective", help="Red-team objective to test against the configured model.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    asyncio.run(run_red_team_scan(args.objective))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
