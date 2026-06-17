from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both spells must be callable")

    def combined_spell(target: str, power: int) -> tuple:
        return spell1(target, power), spell2(target, power)

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("Base spell must be callable")

    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("Condition and spell must be callable")

    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    if not all(callable(spell) for spell in spells):
        raise TypeError("All spells must be callable")

    def sequence_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence_spell


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} power"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def has_enough_power(_target: str, power: int) -> bool:
    return power >= 10


def main() -> None:
    print()
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    fire_result, heal_result = combined("Dragon", 10)
    print(f"Combined spell result: {fire_result}, {heal_result}")

    print()
    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original_power = 10
    print(
        f"Original: {original_power}, "
        f"Amplified: {mega_fireball('Dragon', original_power)}"
    )

    print()
    print("Testing conditional caster...")
    safe_fireball = conditional_caster(has_enough_power, fireball)
    print(safe_fireball("Dragon", 15))
    print(safe_fireball("Dragon", 5))

    print()
    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 10))

    # print()
    # print("Testing callable validation...")
    # try:
    #     spell_combiner(fireball, "not a spell")
    # except TypeError as error:
    #     print(error)


if __name__ == "__main__":
    main()
