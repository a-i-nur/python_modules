#!/usr/bin/env python3

import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")

    argv = sys.argv
    prog_name = argv[0]
    len_args = len(argv)

    if len_args == 1:
        print("No arguments provided")
        print(f"Program name: {prog_name}")
    else:
        args = argv[1:]
        print(f"Program name: {prog_name}")
        print(f"Arguments received: {len(args)}")
        i = 1
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {len_args}")


if __name__ == "__main__":
    ft_command_quest()
