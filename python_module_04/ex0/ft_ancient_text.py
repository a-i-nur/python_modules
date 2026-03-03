#!/usr/bin/env python3

from pathlib import Path


def ft_ancient_text_recovery() -> None:
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open(file_path, "r")
        print("Connection established...")
        print("RECOVERED DATA:")
        data = file.read().splitlines()
        for line in data:
            print(line)
        print("Data recovery complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    ft_ancient_text_recovery()


# Exercise 0: Ancient Text Recovery
# Subject requires: read "ancient_fragment.txt" and print the recovery log.
# Authorized: open(), read(), close(), print(). Python 3.10+.
# If file missing, print exactly:
# ERROR: Storage vault not found. Run data generator first.
#
# Expected output format (must preserve these lines):
# === CYBER ARCHIVES - DATA RECOVERY SYSTEM ===
# Accessing Storage Vault: ancient_fragment.txt
# Connection established...
# RECOVERED DATA:
# [FRAGMENT 001] Digital preservation protocols established 2087
# [FRAGMENT 002] Knowledge must survive the entropy wars
# [FRAGMENT 003] Every byte saved is a victory against oblivion
# Data recovery complete. Storage unit disconnected.
#
# TODO:
# 1) Open the file in read mode ("r").
# 2) Read all contents from the file.
# 3) Print the header and status lines exactly as required.
# 4) Print the recovered data lines in the required order.
# 5) Close the file handle explicitly (no with in this exercise).
# 6) Handle missing file with the exact error message above.
# Note: Add type hints for any functions you create.
