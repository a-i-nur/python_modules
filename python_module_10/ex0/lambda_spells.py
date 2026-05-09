def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages),
            2,
        ),
    }


def main():
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Ice Wand", "power": 67, "type": "weapon"},
    ]

    mages = [
        {"name": "Alex", "power": 80, "element": "fire"},
        {"name": "Jordan", "power": 55, "element": "ice"},
        {"name": "Riley", "power": 95, "element": "lightning"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before "
        f"{sorted_artifacts[-1]['name']} "
        f"({sorted_artifacts[-1]['power']} power)"
    )

    print("\nTesting power filter...")
    print(power_filter(mages, 70))

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
