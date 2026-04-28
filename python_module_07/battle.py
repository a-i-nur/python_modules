from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(
        factory: CreatureFactory,
) -> None:
    print("Testing factory")

    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())

    print()


def test_battle(
        first_factory: CreatureFactory,
        second_factory: CreatureFactory,
) -> None:
    print("Testing battle")
    creature1 = first_factory.create_base()
    creature2 = second_factory.create_base()
    print(creature1.describe())
    print("  vs.")
    print(creature2.describe())
    print("  fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)

    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
