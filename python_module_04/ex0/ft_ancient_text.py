#!/usr/bin/env python3


def ft_ancient_text_recovery() -> None:
    file_name = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print(f"Accessing Storage Vault: {file_name}")
    try:
        file = open(file_name, "r")
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        file_data = file.read()
        print(file_data)
        print()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        print("Data recovery complete. Storage unit disconnected.")
        file.close()


if __name__ == "__main__":
    ft_ancient_text_recovery()
