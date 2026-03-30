"""Entry point for the ex4 tournament platform demo."""

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    """Run the ex4 tournament platform demo."""
    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")
    fire_dragon = TournamentCard(
        card_id="dragon_001",
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack_power=8,
        health=8,
        base_rating=1200,
    )
    ice_wizard = TournamentCard(
        card_id="wizard_001",
        name="Ice Wizard",
        cost=4,
        rarity="Rare",
        attack_power=6,
        health=7,
        base_rating=1150,
    )

    platform.register_card(fire_dragon)
    platform.register_card(ice_wizard)

    print(f"{fire_dragon.name} (ID: {fire_dragon.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {fire_dragon.calculate_rating()}")
    print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}")

    print(f"{ice_wizard.name} (ID: {ice_wizard.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {ice_wizard.calculate_rating()}")
    print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}")

    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")

    print("Tournament Leaderboard:")
    for index, card in enumerate(platform.get_leaderboard(), start=1):
        info = card.get_rank_info()
        print(
            f"{index}. {card.name} - Rating: {info['rating']} "
            f"({info['record']})"
        )

    print("Platform Report:")
    print(platform.generate_tournament_report())

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

    # print("\n=== TEST WITH GENERATOR ===\n")
    # from tools.card_generator import CardGenerator
    #
    # generator = CardGenerator()
    # creature_data = generator.get_creature("Stone Golem")
    # if creature_data is not None:
    #     generated_card = TournamentCard(
    #         card_id="golem_001",
    #         name=creature_data["name"],
    #         cost=creature_data["cost"],
    #         rarity=creature_data["rarity"],
    #         attack_power=creature_data["attack"],
    #         health=creature_data["health"],
    #         base_rating=1180,
    #     )
    #     print("Generator tournament stats:")
    #     print(generated_card.get_tournament_stats())


if __name__ == "__main__":
    main()
