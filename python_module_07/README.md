# DataDeck

DataDeck is a Python project about abstract programming patterns.

The project uses a small creature card game to practice:

- abstract classes
- abstract factories
- multiple inheritance
- capabilities
- strategy pattern
- type annotations

The code uses only Python standard tools.

## Requirements

- Python 3.10 or later
- `flake8`
- `mypy`
- no external libraries in the project code

## Project Structure

```text
battle.py
capacitor.py
tournament.py

ex0/
    __init__.py
    creature.py
    creature_factory.py

ex1/
    __init__.py
    capabilities.py
    healing_creatures.py
    transform_creatures.py
    creature_factory.py

ex2/
    __init__.py
    strategies.py
```

## How To Check The Project

Run all programs:

```bash
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

Check style:

```bash
python3 -m flake8 battle.py capacitor.py tournament.py ex0 ex1 ex2
```

Check types:

```bash
mypy battle.py capacitor.py tournament.py ex0 ex1 ex2
```

If `mypy` is installed only in the virtual environment:

```bash
./venv/bin/mypy battle.py capacitor.py tournament.py ex0 ex1 ex2
```

## Exercise 0: Creature Factory

Exercise 0 introduces the abstract factory pattern.

Main idea:

One factory creates a family of related creatures.

Example:

- `FlameFactory` creates `Flameling` and `Pyrodon`
- `AquaFactory` creates `Aquabub` and `Torragon`

Important classes:

- `Creature`: abstract base class
- `CreatureFactory`: abstract factory class
- `FlameFactory`: concrete factory
- `AquaFactory`: concrete factory

The `Creature` class defines common behavior:

- every creature has a name
- every creature has a type
- every creature can describe itself
- every creature must implement `attack()`

Run exercise 0:

```bash
python3 battle.py
```

What happens:

- the program creates flame and aqua factories
- each factory creates a base creature and an evolved creature
- the program prints descriptions and attacks
- base creatures fight

What to explain in evaluation:

An abstract factory creates related objects without exposing the concrete classes to the
main program. `battle.py` works with factories, not directly with concrete creature
classes.

### Theory For Exercise 0

Exercise 0 uses two important ideas: abstraction and factory creation.

Abstraction means the code depends on a general interface, not on one exact class.

In this exercise, `Creature` is abstract. It says: every creature must have `attack()`.
But it does not know how each creature attacks.

Example:

- `Flameling` attacks with Ember
- `Aquabub` attacks with Water Gun

This is polymorphism. The same method name, `attack()`, has different behavior in
different classes.

`CreatureFactory` is also abstract. It says every factory must create:

- one base creature
- one evolved creature

Concrete factories decide the real classes:

- `FlameFactory` creates flame creatures
- `AquaFactory` creates water creatures

Why this is useful:

- `battle.py` does not need to know all concrete creature classes
- adding a new family is easier
- the code has fewer hardcoded decisions

Simple defense sentence:

Exercise 0 shows that I can create objects through an abstract factory instead of
creating concrete classes directly in the main script.

## Exercise 1: Capabilities

Exercise 1 adds extra abilities to creatures.

Main idea:

Capabilities are separate from the `Creature` base class.

There are two capability abstract classes:

- `HealCapability`
- `TransformCapability`

Healing creatures:

- `Sproutling`
- `Bloomelle`

Transforming creatures:

- `Shiftling`
- `Morphagon`

Factories:

- `HealingCreatureFactory`
- `TransformCreatureFactory`

Run exercise 1:

```bash
python3 capacitor.py
```

What happens:

- healing creatures describe themselves, attack, and heal
- transform creatures describe themselves, attack, transform, attack again, and revert

What to explain in evaluation:

Capabilities are not part of every creature. Only some creatures can heal. Only some
creatures can transform. This keeps the design flexible because new capabilities can be
added without changing the base `Creature` class.

### Theory For Exercise 1

Exercise 1 uses multiple inheritance and interface-like abstract classes.

`HealCapability` and `TransformCapability` are not creatures. They are separate
abilities.

This is important because not all creatures have the same abilities.

Example:

- `Sproutling` is a `Creature` and has `HealCapability`
- `Shiftling` is a `Creature` and has `TransformCapability`

So a class can inherit from:

- the base creature class
- one capability class

This design keeps `Creature` simple. `Creature` only knows about normal creature data
and behavior. It does not contain `heal()`, `transform()`, or `revert()` because not all
creatures need those methods.

The transform capability also has state:

```python
self.transformed = False
```

This state changes the attack result:

- before transform: normal attack
- after transform: boosted attack
- after revert: normal attack again

Why this is useful:

- new capabilities can be added later
- the base `Creature` class stays clean
- the code can check abilities with `isinstance()`
- each class has a clear responsibility

Simple defense sentence:

Exercise 1 shows that I can add optional behavior with separate capability classes
instead of putting every possible method inside the base `Creature` class.

## Exercise 2: Abstract Strategy

Exercise 2 adds battle strategies.

Main idea:

A strategy decides how a creature acts in battle.

Strategies:

- `NormalStrategy`: any creature can use it; it only attacks
- `DefensiveStrategy`: only healing creatures can use it; it attacks and then heals
- `AggressiveStrategy`: only transform creatures can use it; it transforms, attacks, and reverts

There is also a custom exception:

- `InvalidStrategyError`

This exception is raised when a creature is used with the wrong strategy.

Run exercise 2:

```bash
python3 tournament.py
```

What happens:

- the program creates several creature factories
- the program creates several strategies
- each opponent is a pair: factory plus strategy
- every opponent fights every other opponent once
- invalid strategy combinations are handled safely

What to explain in evaluation:

The strategy pattern moves battle behavior out of the creature classes. The creature
does not need to know tournament rules. The strategy object decides what to do.

### Theory For Exercise 2

Exercise 2 uses the strategy pattern.

A strategy is a class that contains one behavior. In this project, each strategy decides
how a creature acts during battle.

The abstract class `BattleStrategy` defines two methods:

- `is_valid()`: checks if this creature can use this strategy
- `act()`: performs the strategy action

Concrete strategies:

- `NormalStrategy` works with every creature
- `DefensiveStrategy` works only with healing creatures
- `AggressiveStrategy` works only with transform creatures

This means the tournament code does not need to know all details about healing and
transforming. It only calls:

```python
strategy.act(creature)
```

The strategy object decides what to do.

Invalid combinations are possible. For example, `Flameling` cannot use
`AggressiveStrategy` because it cannot transform.

For this case, the code raises:

```python
InvalidStrategyError
```

The tournament catches this error and stops safely.

Why this is useful:

- battle behavior is separated from creature classes
- new strategies can be added later
- the tournament logic stays simple
- invalid combinations are handled clearly

Simple defense sentence:

Exercise 2 shows that I can move battle behavior into strategy classes, so the
tournament can work with different behaviors through one common interface.

## Design Pattern Summary

### Abstract Class

An abstract class is a contract.

Example:

`Creature` says every creature must have `attack()`.

Concrete classes decide the real attack.

### Abstract Factory

An abstract factory creates a family of related objects.

Example:

`FlameFactory` creates the flame family:

- base: `Flameling`
- evolved: `Pyrodon`

The main program does not need to create these classes directly.

### Capability

A capability is an extra ability.

Example:

- healing creatures have `heal()`
- transform creatures have `transform()` and `revert()`

This avoids putting all possible methods inside `Creature`.

### Strategy

A strategy is an object that represents behavior.

Example:

- normal behavior: attack
- defensive behavior: attack and heal
- aggressive behavior: transform, attack, revert

This avoids many `if` statements in the tournament code.

## Submission Checklist

Before submitting, check:

```bash
python3 battle.py
python3 capacitor.py
python3 tournament.py
python3 -m flake8 battle.py capacitor.py tournament.py ex0 ex1 ex2
mypy battle.py capacitor.py tournament.py ex0 ex1 ex2
```

Also check file names:

- `battle.py` is at the repository root
- `capacitor.py` is at the repository root
- `tournament.py` is at the repository root
- `ex0/__init__.py` exists
- `ex1/__init__.py` exists
- `ex2/__init__.py` exists

Only files inside the Git repository will be evaluated.

## Simple Defense Answers

Question: What is the goal of this project?

Answer: The goal is to practice abstract programming patterns in Python using a card
game example.

Question: What is an abstract factory?

Answer: It is a class that creates a family of related objects. In this project, each
factory creates a base creature and an evolved creature from the same family.

Question: Why not create creatures directly in `battle.py`?

Answer: Because the main program should not depend on concrete creature classes. It is
better to depend on the abstract factory interface.

Question: Why are capabilities separate from `Creature`?

Answer: Because not every creature can heal or transform. Separate capabilities keep the
base class small and make the code easier to extend.

Question: What is the strategy pattern?

Answer: The strategy pattern puts behavior in separate strategy classes. In this
project, each battle strategy decides how a creature acts during a fight.

Question: How do you handle invalid strategies?

Answer: Each strategy checks if the creature is valid. If not, it raises
`InvalidStrategyError`, and `tournament.py` catches it and aborts the tournament safely.

Question: Why use type annotations?

Answer: Type annotations make the code clearer and allow `mypy` to find mistakes before
running the program.
