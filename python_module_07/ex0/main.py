"""ex0/main.py

Exercise 0 demo entry point.
Run with: python3 -m ex0.main
"""

from .CreatureCard import CreatureCard


def main() -> None:
    """Run the Exercise 0 demo."""
    print()
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()

    dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5,
    )

    print("CreatureCard Info:")
    print(dragon.get_card_info())
    print()

    mana = 6
    print(f"Playing {dragon.name} with {mana} mana available:")
    print(f"Playable: {dragon.is_playable(mana)}")
    print(f"Play result: {dragon.play({})}")
    print()

    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target('Goblin Warrior')}")
    # A string target is enough for the Exercise 0 demo.
    print()

    mana = 3
    print(f"Testing insufficient mana ({mana} available):")
    print(f"Playable: {dragon.is_playable(mana)}")
    print()

    print("Abstract pattern successfully demonstrated!")

    # Generator-based local test snippet.
    # print("\n=== TEST WITH GENERATOR ===\n")
    # from tools.card_generator import CardGenerator
    # generator = CardGenerator()
    # data = generator.get_creature("Fire Dragon")
    # if data is not None:
    #     generated_creature = CreatureCard(
    #         name=data["name"],
    #         cost=data["cost"],
    #         rarity=data["rarity"],
    #         attack=data["attack"],
    #         health=data["health"],
    #     )
    #     print("Generator creature info:")
    #     print(generated_creature.get_card_info())


if __name__ == "__main__":
    main()
