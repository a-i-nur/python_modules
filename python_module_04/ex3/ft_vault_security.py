#!/usr/bin/env python3


def ft_vault_security() -> None:
    file_name = "classified_data.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()

    print("SECURE EXTRACTION:")
    with open(file_name, "r") as file:
        data = file.read()
        print(data)
        # data = file.read().splitlines()
        # for line in data:
        #     print(line)
    print()

    print("SECURE PRESERVATION:")
    with open("security_protocols.txt", "w") as file:
        file.write("[CLASSIFIED] New security protocols archived\n")
    print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion")
    print()

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
