#!/usr/bin/env python3

import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    # alternatively, we could read from stdin directly:
    # status_report = sys.stdin.readline()
    print()

    print(
        f"[STANDARD] Archive status from "
        f"{archivist_id}: {status_report}", file=sys.stdout)
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr)
    # alternatively, we could write to stderr directly:
    # sys.stderr.write(
    #    "[ALERT] System diagnostic: Communication channels verified\n")
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print()

    print("Three-channel communication test successful.")
    # alternatively, we could write to stdout directly:
    # sys.stdout.write("Three-channel communication test successful.\n")


if __name__ == "__main__":
    ft_stream_management()
