#!/usr/bin/env python3

from pathlib import Path


def ft_archive_creation() -> None:
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "new_discovery.txt"

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("Initializing new storage unit: new_discovery.txt")
    file = open(file_path, "w")
    print("Storage unit created successfully...")
    print("Inscribing preservation data...")
    file.write("New quantum algorithm discovered\n")
    file.write("Efficiency increased by 347%\n")
    file.write("Archived by Data Archivist trainee\n")
    print("[ENTRY 001] New quantum algorithm discovered")
    print("[ENTRY 002] Efficiency increased by 347%")
    print("[ENTRY 003] Archived by Data Archivist trainee")
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
    file.close()


if __name__ == "__main__":
    ft_archive_creation()


# Exercise 1: Archive Creation
# Subject requires: create/overwrite "new_discovery.txt" and write three entries.
# Authorized: open(), write(), close(), print(). Python 3.10+.
#
# Required file content (order matters):
# 1) New quantum algorithm discovered
# 2) Efficiency increased by 347%
# 3) Archived by Data Archivist trainee
#
# Expected output format (must preserve these lines):
# === CYBER ARCHIVES - PRESERVATION SYSTEM ===
# Initializing new storage unit: new_discovery.txt
# Storage unit created successfully...
# Inscribing preservation data...
# [ENTRY 001] New quantum algorithm discovered
# [ENTRY 002] Efficiency increased by 347%
# [ENTRY 003] Archived by Data Archivist trainee
# Data inscription complete. Storage unit sealed.
# Archive 'new_discovery.txt' ready for long-term preservation.
#
# TODO:
# 1) Open the file in write mode ("w").
# 2) Write the three required lines in the correct order, with newlines.
# 3) Print the required log lines exactly as above.
# 4) Close the file handle explicitly (no with in this exercise).
# Note: Add type hints for any functions you create.
