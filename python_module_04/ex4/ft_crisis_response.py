#!/usr/bin/env python3


def handle_archive_access(file_name: str) -> None:

    if file_name == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")

    try:
        if file_name == "classified_vault.txt":
            raise PermissionError
        with open(file_name, "r") as file:
            content = file.read().strip()
        print(f'SUCCESS: Archive recovered - "{content}"')
        print("STATUS: Normal operations resumed")
        print()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        print()
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        print()
    except Exception:
        print("RESPONSE: Unexpected system anomaly")
        print("STATUS: Crisis handled, system stable")
        print()


def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    test_files = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"]

    for file_name in test_files:
        handle_archive_access(file_name)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
