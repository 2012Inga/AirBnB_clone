#!/usr/bin/python3

import sys


class Console:
    def __init__(self):
        self.prompt = '(hbnb) '

    def help(self):
        print("\nDocumented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit")

    def run_interactive_mode(self):
        print("Welcome to interactive mode!")
        while True:
            try:
                user_input = input(self.prompt).strip()
                if user_input == 'help':
                    self.help()
                elif user_input == 'quit':
                    break
            except EOFError:
                print("\nExiting interactive mode.")
                break

    def run_non_interactive_mode(self):
        print("Running in non-interactive mode...")
        lines = sys.stdin.readlines()
        for line in lines:
            user_input = line.strip()
            if user_input == 'help':
                self.help()


if __name__ == "__main__":
    console = Console()

    # Check if there are command-line arguments
    if len(sys.argv) > 1:
        # If there are arguments, assume non-interactive mode
        console.run_non_interactive_mode()
    else:
        # Otherwise, run interactive mode
        console.run_interactive_mode()
