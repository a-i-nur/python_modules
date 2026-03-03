#!/usr/bin/env python3
"""
Exercise 0: Command Quest.

Collection theory: `sys.argv` is a list, an ordered, mutable sequence.
Lists preserve insertion order and allow indexing, slicing, and iteration,
which makes them ideal for processing command-line arguments.
"""

import sys


def ft_command_quest() -> None:
    """Print basic `sys.argv` analytics using list operations."""
    print("=== Command Quest ===")

    argv = sys.argv
    prog_name = argv[0]
    len_argv = len(argv)

    if len_argv == 1:
        print("No arguments provided")

    print(f"Program name: {prog_name}")

    if len_argv > 1:
        args = argv[1:]
        print(f"Arguments received: {len(args)}")
        i = 1
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {len_argv}")


if __name__ == "__main__":
    ft_command_quest()
