import sys
from forge.cli.commands import init


def run():
    if len(sys.argv) < 2:
        print("Usage: forge <command>")
        return

    command = sys.argv[1]

    if command == "init":
        init.run()
    else:
        print(f"Unknown command: {command}")
