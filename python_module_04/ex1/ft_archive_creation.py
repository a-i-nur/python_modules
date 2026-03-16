#!/usr/bin/env python3


def ft_archive_creation() -> None:
    file_name = "new_discovery.txt"
    entries = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee"]
    index = 1

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()

    try:
        print(f"Initializing new storage unit: {file_name}")
        file = open(file_name, "w")
    except Exception as e:
        print(f"ERROR: {e}")
        return
    else:
        print("Storage unit created successfully...")
        print()
        print("Inscribing preservation data...")
        for entry in entries:
            line = f"[ENTRY {index:03d}] {entry}"
            file.write(line + "\n")
            print(line)
            index += 1
        print()
    finally:
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")
        file.close()


if __name__ == "__main__":
    ft_archive_creation()
