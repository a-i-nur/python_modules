#!/usr/bin/env python3


def ft_ancient_text_recovery() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
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
