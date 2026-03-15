#!/usr/bin/env python3


def ft_archive_creation() -> None:
    entries = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee",
    ]

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("Initializing new storage unit: new_discovery.txt")
    file = open("new_discovery.txt", "w")
    print("Storage unit created successfully...")
    print("Inscribing preservation data...")
    for index, entry in enumerate(entries, 1):
        line = f"[ENTRY {index:03d}] {entry}"
        file.write(line + "\n")
        print(line)
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
    file.close()


if __name__ == "__main__":
    ft_archive_creation()
