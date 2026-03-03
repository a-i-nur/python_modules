#!/usr/bin/env python3

from pathlib import Path


def ft_vault_security() -> None:
    base_dir = Path(__file__).resolve().parent
    source_file = base_dir / "classified_data.txt"
    destination_file = base_dir / "security_protocols.txt"

    # Step 1: Print the header and initiation message
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")

    # Step 2: Establish connection and read data safely
    print("Vault connection established with failsafe protocols")
    with open(source_file, "r") as file:
        data = file.read().splitlines()

    # Step 3: Print the secure extraction block
    print("SECURE EXTRACTION:")
    for line in data:
        print(f"[CLASSIFIED] {line}")

    # Step 4: Write new security protocols safely
    with open(destination_file, "w") as file:
        file.write("New security protocols archived\n")

    # Step 5: Print the secure preservation block and finalize
    print("SECURE PRESERVATION:")
    print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()


# Exercise 3: Vault Security
# Subject requires: use the with statement for safe read and write operations.
# Authorized: open(), read(), write(), print(). Python 3.10+.
# Must use context managers (with) for all file operations.
#
# Expected output format (must preserve these lines):
# === CYBER ARCHIVES - VAULT SECURITY SYSTEM ===
# Initiating secure vault access...
# Vault connection established with failsafe protocols
# SECURE EXTRACTION:
# [CLASSIFIED] Quantum encryption keys recovered
# [CLASSIFIED] Archive integrity: 100%
# SECURE PRESERVATION:
# [CLASSIFIED] New security protocols archived
# Vault automatically sealed upon completion
# All vault operations completed with maximum security.
#
# TODO:
# 1) Open a source file with "with" and read its content.
# 2) Print the secure extraction block.
# 3) Open/create a destination file with "with" and write the required line.
# 4) Print the secure preservation block.
# 5) Ensure output matches the subject format.
# Note: Add type hints for any functions you create.
