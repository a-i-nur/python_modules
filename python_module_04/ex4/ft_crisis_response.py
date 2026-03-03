#!/usr/bin/env python3

from pathlib import Path


def ft_crisis_response() -> None:
    base_dir = Path(__file__).resolve().parent

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    # List of test files to access
    test_files = ["lost_archive.txt", "classified_vault.txt", "standard_archive.txt"]

    for file_name in test_files:
        file_path = base_dir / file_name
        if file_name == "standard_archive.txt":
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{file_name}'...")

        try:
            with open(file_path, "r") as file:
                content = file.read().strip()
                print(f"SUCCESS: Archive recovered - \"{content}\"")
                print("STATUS: Normal operations resumed")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        except Exception:
            print("RESPONSE: Unexpected system anomaly")
            print("STATUS: Crisis handled, system stable")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()

# Exercise 4: Crisis Response
# Subject requires: use with + try/except to handle file access failures.
# Authorized: open(), read(), write(), print(). Python 3.10+.
# Must handle FileNotFoundError, PermissionError, and other exceptions.
#
# Expected output format (must preserve these lines; file names vary):
# === CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===
# CRISIS ALERT: Attempting access to 'lost_archive.txt'...
# RESPONSE: Archive not found in storage matrix
# STATUS: Crisis handled, system stable
# CRISIS ALERT: Attempting access to 'classified_vault.txt'...
# RESPONSE: Security protocols deny access
# STATUS: Crisis handled, security maintained
# ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...
# SUCCESS: Archive recovered - "Knowledge preserved for humanity"
# STATUS: Normal operations resumed
# All crisis scenarios handled successfully. Archives secure.
#
# TODO:
# 1) Implement a function that attempts to open a file and read its content.
# 2) Wrap access in try/except and handle FileNotFoundError and PermissionError.
# 3) Handle any other Exception with a generic message.
# 4) Print the required crisis logs for each test file.
# 5) Ensure files are always closed by using "with".
# Note: Add type hints for any functions you create.
