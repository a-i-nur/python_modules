"""Entry point for the ex2 ability system demo."""

from .EliteCard import EliteCard


def main() -> None:
    """Run the ex2 ability system demo."""
    print()
    print("=== DataDeck Ability System ===")
    print()

    elite = EliteCard(
        name="Arcane Warrior",
        cost=6,
        rarity="Legendary",
        attack_power=5,
        health=10,
        mana=8,
    )

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()

    print(f"Playing {elite.name} (Elite Card):")
    print(elite.play({}))
    print()

    print("Combat phase:")
    print(f"Attack result: {elite.attack('Enemy')}")
    print(f"Defense result: {elite.defend(5)}")
    print()

    print("Magic phase:")
    print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elite.channel_mana(3)}")
    print()

    print("Multiple interface implementation successful!")

    # print("\n=== TEST WITH GENERATOR ===\n")
    # from tools.card_generator import CardGenerator
    #
    # generator = CardGenerator()
    # data = generator.get_creature("Ice Wizard")
    # if data is not None:
    #     generated_elite = EliteCard(
    #         name=data["name"],
    #         cost=data["cost"],
    #         rarity=data["rarity"],
    #         attack_power=data["attack"],
    #         health=data["health"],
    #         mana=6,
    #     )
    #     print("Generator elite attack:")
    #     print(generated_elite.attack("Training Dummy"))


if __name__ == "__main__":
    main()
