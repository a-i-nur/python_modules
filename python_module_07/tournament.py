from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("* Battle *")
            creature_factory_1, strategy_1 = opponents[i]
            creature_factory_2, strategy_2 = opponents[j]

            creature_1 = creature_factory_1.create_base()
            creature_2 = creature_factory_2.create_base()

            print(creature_1.describe())
            print("  vs.")
            print(creature_2.describe())
            print("  now fight!")

            try:
                strategy_1.act(creature_1)
                strategy_2.act(creature_2)
                print()
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}\n")
                return


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    opponents = [
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy),
    ]
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    battle(opponents)

    print("Tournament 1 (error)")
    opponents = [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy),
    ]
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    battle(opponents)

    print("Tournament 2 (multiple)")
    opponents = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy),
    ]
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    battle(opponents)


if __name__ == "__main__":
    main()
