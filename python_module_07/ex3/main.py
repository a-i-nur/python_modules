"""Entry point for the ex3 game engine demo."""

from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    """Run the ex3 game engine demo."""
    print()
    print("=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Factory: FantasyCardFactory")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")
    print()

    engine.hand = factory.create_themed_deck(3)["cards"]
    hand_repr = [f"{card.name} ({card.cost})" for card in engine.hand]
    print("Simulating aggressive turn...")
    report = engine.simulate_turn()
    print(f"Hand: {hand_repr}")
    print()

    print("Turn execution:")
    print(f"Strategy: {report['strategy_used']}")
    print(f"Actions: {report['actions']}")
    print()

    print("Game Report:")
    print(
        {
            "turns_simulated": report["turns_simulated"],
            "strategy_used": report["strategy_used"],
            "total_damage": report["total_damage"],
            "cards_created": report["cards_created"],
        }
    )
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")

    # print("\n=== TEST WITH GENERATOR ===\n")
    # from tools.card_generator import CardGenerator
    #
    # generator = CardGenerator()
    # print("Generator random creature:")
    # print(generator.get_random_creature())
    # print("Generator random spell:")
    # print(generator.get_random_spell())
    # print("Generator random artifact:")
    # print(generator.get_random_artifact())


if __name__ == "__main__":
    main()
