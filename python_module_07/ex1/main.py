"""Entry point for the ex1 deck builder demo."""

from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck
from .SpellCard import SpellCard


def main() -> None:
    """Run the ex1 deck builder demo."""
    print()
    print("=== DataDeck Deck Builder ===")
    print()

    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(
        CreatureCard(
            name="Fire Dragon",
            cost=5,
            rarity="Legendary",
            attack=7,
            health=5,
        )
    )
    deck.add_card(
        ArtifactCard(
            name="Mana Crystal",
            cost=2,
            rarity="Rare",
            durability=3,
            effect="+1 mana per turn",
        )
    )
    deck.add_card(
        SpellCard(
            name="Lightning Bolt",
            cost=3,
            rarity="Common",
            effect_type="damage",
        )
    )

    print(f"Deck stats: {deck.get_deck_stats()}")
    print()

    deck.shuffle()
    print("Drawing and playing cards:")
    print()
    try:
        while True:
            card = deck.draw_card()
            print(f"Drew: {card.name} ({card.get_card_info()['type']})")
            print(f"Play result: {card.play({})}")
            print()
    except IndexError:
        pass

    print("Polymorphism in action: Same interface, different card behaviors!")

    # print("\n=== TEST WITH GENERATOR ===\n")
    # from tools.card_generator import CardGenerator
    #
    # generator = CardGenerator()
    # creature_data = generator.get_creature("Fire Dragon")
    # spell_data = generator.get_spell("Lightning Bolt")
    # artifact_data = generator.get_artifact("Mana Crystal")
    # test_deck = Deck()
    # if creature_data is not None:
    #     test_deck.add_card(
    #         CreatureCard(
    #             creature_data["name"],
    #             creature_data["cost"],
    #             creature_data["rarity"],
    #             creature_data["attack"],
    #             creature_data["health"],
    #         )
    #     )
    # if spell_data is not None:
    #     test_deck.add_card(
    #         SpellCard(
    #             spell_data["name"],
    #             spell_data["cost"],
    #             spell_data["rarity"],
    #             spell_data["effect_type"],
    #         )
    #     )
    # if artifact_data is not None:
    #     test_deck.add_card(
    #         ArtifactCard(
    #             artifact_data["name"],
    #             artifact_data["cost"],
    #             artifact_data["rarity"],
    #             artifact_data["durability"],
    #             artifact_data["effect"],
    #         )
    #     )
    # print("Generator deck stats:")
    # print(test_deck.get_deck_stats())


if __name__ == "__main__":
    main()
