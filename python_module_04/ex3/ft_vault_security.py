#!/usr/bin/env python3


def ft_vault_security() -> None:
    base_dir = __file__.rsplit("/", 1)[0]
    source_file = f"{base_dir}/classified_data.txt"
    destination_file = f"{base_dir}/security_protocols.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    with open(source_file, "r") as file:
        data = file.read().splitlines()
        print("SECURE EXTRACTION:")
        for line in data:
            print(f"[CLASSIFIED] {line}")
    with open(destination_file, "w") as file:
        file.write("New security protocols archived\n")
    print("SECURE PRESERVATION:")
    print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
