"""Shared test utilities."""

import subprocess


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Run the assert-no-inline-lint-disables CLI as a user would."""
    return subprocess.run(
        ["assert-no-inline-lint-disables", *args],
        capture_output=True,
        text=True,
        check=False,
    )
