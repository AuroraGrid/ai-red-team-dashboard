"""Small CLI dashboard for AI red-team scans and probabilistic forecasts.

Configuration is read from environment variables. Never commit API keys.
"""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
from typing import Final

from openai import AsyncOpenAI
from pyrit.executor.attack import PromptSendingAttack
from pyrit.output.attack_result.pretty import PrettyAttackResultMemoryPrinter
from pyrit.prompt_target import OpenAIChatTarget
from pyrit.setup import IN_MEMORY, initialize_pyrit_async

DEFAULT_BASE_URL: Final[str] = "https://api.groq.com/openai/v1"
DEFAULT_MODEL: Final[str] = "llama-3.3-70b-versatile"


def get_settings() -> tuple[str, str, str]:
    """Return API key, base URL, and model from environment variables."""
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Copy .env.example, export the variable, "
            "or configure it in your shell before running the dashboard."
        )

    base_url = os.getenv("GROQ_BASE_URL", DEFAULT_BASE_URL).strip().rstrip("/")
    model = os.getenv("GROQ_MODEL", DEFAULT_MODEL).strip()
    if not model:
        raise RuntimeError("GROQ_MODEL cannot be empty.")

    return api_key, base_url, model


def clean_input(value: str, *, label: str) -> str:
    """Normalize user input and reject empty values."""
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{label} cannot be empty.")
    return normalized


async def run_red_team_scan(objective_text: str) -> None:
    """Run a single PyRIT prompt-sending attack against the configured model."""
    objective = clean_input(objective_text, label="Red-team objective")
    api_key, base_url, model = get_settings()

    await initialize_pyrit_async(memory_db_type=IN_MEMORY)
    target = OpenAIChatTarget(
        model_name=model,
        endpoint=base_url,
        api_key=api_key,
    )

    print(f"\n[red-team] model={model}")
    print("[red-team] starting PyRIT scan...\n")

    attack = PromptSendingAttack(objective_target=target)
    result = await attack.execute_async(objective=objective)

    printer = PrettyAttackResultMemoryPrinter()
    await printer.write_async(result)


async def run_forecast_query(question_text: str) -> None:
    """Run a low-temperature probabilistic forecast query."""
    question = clean_input(question_text, label="Forecast question")
    api_key, base_url, model = get_settings()

    client = AsyncOpenAI(base_url=base_url, api_key=api_key)
    system_prompt = (
        "You are a quantitative forecasting analyst. Give a numeric probability, "
        "state the relevant base rate, explain the main drivers and constraints, "
        "identify the strongest counterargument, and list indicators that would "
        "materially change the forecast. Separate facts from inference."
    )

    print(f"\n[forecast] model={model}")
    print("[forecast] running analysis...\n")

    response = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content or "No text response returned."
    print("=" * 64)
    print("FORECAST ANALYSIS")
    print("=" * 64)
    print(content)
    print("=" * 64)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="AI red-team and forecasting command-line dashboard."
    )
    parser.add_argument(
        "--mode",
        choices=("red-team", "forecast"),
        help="Run directly instead of opening the interactive menu.",
    )
    parser.add_argument(
        "--prompt",
        help="Objective or question to run with --mode.",
    )
    return parser


def print_menu() -> None:
    print("\nAI RED-TEAM DASHBOARD")
    print("=" * 64)
    print("1  Red-team security scan (PyRIT)")
    print("2  Probabilistic forecast analysis")
    print("q  Quit")
    print("=" * 64)


async def interactive_main() -> None:
    print_menu()
    choice = input("Select mode: ").strip().lower()

    if choice in {"q", "quit", "exit"}:
        return
    if choice == "1":
        objective = input("Red-team objective: ")
        await run_red_team_scan(objective)
        return
    if choice == "2":
        question = input("Forecast question: ")
        await run_forecast_query(question)
        return

    raise ValueError("Invalid selection. Choose 1, 2, or q.")


async def async_main() -> None:
    args = build_parser().parse_args()

    if args.mode:
        if not args.prompt:
            raise ValueError("--prompt is required when --mode is provided.")
        if args.mode == "red-team":
            await run_red_team_scan(args.prompt)
        else:
            await run_forecast_query(args.prompt)
        return

    await interactive_main()


def main() -> int:
    try:
        asyncio.run(async_main())
        return 0
    except KeyboardInterrupt:
        print("\nCancelled.", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"\nError: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
