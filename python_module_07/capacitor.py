from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)


def main() -> None:

    print("Testing Creature with healing capability")
    print("  base:")
    healing_factory = HealingCreatureFactory()
    base_healing_creature = healing_factory.create_base()
    print(base_healing_creature.describe())
    print(base_healing_creature.attack())
    print(base_healing_creature.heal())
    print("  evolved:")
    evolved_healing_creature = healing_factory.create_evolved()
    print(evolved_healing_creature.describe())
    print(evolved_healing_creature.attack())
    print(evolved_healing_creature.heal())
    print()

    print("Testing Creature with transform capability")
    print("  base:")
    transform_factory = TransformCreatureFactory()
    base_transform_creature = transform_factory.create_base()
    print(base_transform_creature.describe())
    print(base_transform_creature.attack())
    print(base_transform_creature.transform())
    print(base_transform_creature.attack())
    print(base_transform_creature.revert())
    print("  evolved:")
    evolved_transform_creature = transform_factory.create_evolved()
    print(evolved_transform_creature.describe())
    print(evolved_transform_creature.attack())
    print(evolved_transform_creature.transform())
    print(evolved_transform_creature.attack())
    print(evolved_transform_creature.revert())


if __name__ == "__main__":
    main()
