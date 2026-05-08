# DataDeck

## 1. What This Module Is About

This module is about abstract programming patterns in Python.

The project uses a small creature card game. The goal is not to build a real game. The
goal is to learn how to design code that is easy to extend.

This module teaches:

- abstract classes
- abstract factory pattern
- polymorphism
- multiple inheritance
- capability classes
- strategy pattern
- type annotations
- clean package structure

The project uses only Python standard tools. External libraries are forbidden by the
subject.

## 2. Theory You Need To Know

### Abstract Class

An abstract class is a contract.

It says what methods child classes must have, but it does not always implement the real
behavior.

In this project:

```python
class Creature(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass
```

This means every creature must implement `attack()`.

### Polymorphism

Polymorphism means different classes can use the same method name with different
behavior.

Example:

- `Flameling.attack()` returns a fire attack
- `Aquabub.attack()` returns a water attack

The main code can call:

```python
creature.attack()
```

without knowing the exact creature class.

### Abstract Factory

An abstract factory creates a family of related objects.

In this project, every creature factory creates:

- a base creature
- an evolved creature

Example:

- `FlameFactory` creates `Flameling` and `Pyrodon`
- `AquaFactory` creates `Aquabub` and `Torragon`

### Capability

A capability is an optional ability.

Not every creature can heal. Not every creature can transform.

So these abilities are not inside the base `Creature` class. They are separate abstract
classes:

- `HealCapability`
- `TransformCapability`

### Strategy Pattern

A strategy is an object that contains behavior.

In this project, strategies decide how a creature acts in battle:

- normal strategy: attack
- defensive strategy: attack and heal
- aggressive strategy: transform, attack, revert

The tournament code does not need to know all details. It only calls:

```python
strategy.act(creature)
```

## 3. Lore And Connection With Theory

The lore is a creature card game.

Creatures belong to families. A family has a base creature and an evolved creature.

This connects to abstract factory:

- one factory represents one family
- the factory creates the base and evolved cards

Creatures can also have special abilities.

This connects to capabilities:

- healing creatures can heal
- transform creatures can change form

During a tournament, different creatures need different battle behavior.

This connects to strategy:

- the strategy decides what action happens in battle
- the creature does not need to know tournament logic

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

## Exercise 0: Creature Factory

### 1. What To Do, What It Teaches, What Theory Is Needed

In exercise 0, you must create basic creature cards and factories.

You need:

- abstract class `Creature`
- concrete creatures
- abstract class `CreatureFactory`
- concrete factories
- root script `battle.py`

This exercise teaches the abstract factory pattern.

Theory needed:

- abstract classes
- inheritance
- polymorphism
- factory pattern

### 2. How It Is Done In My Code

Files:

```text
ex0/creature.py
ex0/creature_factory.py
ex0/__init__.py
battle.py
```

`Creature` is the abstract base class. It stores:

- `name`
- `creature_type`

It has:

- abstract method `attack()`
- concrete method `describe()`

Concrete creatures:

- `Flameling`
- `Pyrodon`
- `Aquabub`
- `Torragon`

Factories:

- `FlameFactory`
- `AquaFactory`

`ex0/__init__.py` exposes only factories, not concrete creatures.

### 3. How To Run And Demonstrate

Run:

```bash
python3 battle.py
```

Show:

- factories are created
- base and evolved creatures are created
- creatures describe themselves
- creatures attack
- base creatures fight

Important for subject:

- `battle.py` must be at the repository root
- `ex0/` must have `__init__.py`
- the package should not expose concrete creatures directly
- no virtual environment is required by the subject
- do not depend on external libraries

### 4. Subject Questions

Question: What is the abstract factory in ex0?

Answer: `CreatureFactory` is the abstract factory. It defines `create_base()` and
`create_evolved()`.

Question: What are the concrete factories?

Answer: `FlameFactory` and `AquaFactory`.

Question: Why use factories?

Answer: The main script can create creature families without depending on concrete
creature classes.

Pydantic question:

`Think About: How does Pydantic's automatic type conversion work?`

Answer: This question is not part of this subject. This project forbids external
libraries, and Pydantic is an external library. It should not be used here.

`What happens when you pass a string timestamp to a datetime field?`

Answer: This is also a Pydantic question and does not apply to this module.

### 5. Tricky Evaluation Questions

Question: Why is `Creature` abstract?

Answer: Because every creature must attack, but every creature attacks differently.

Question: Why not create `Flameling()` directly in `battle.py`?

Answer: Because `battle.py` should depend on the factory interface, not on concrete
creature classes.

Question: What happens if we add an electric family?

Answer: We can add new concrete creatures and a new factory, for example
`ElectricFactory`, without changing the abstract factory interface.

Question: What is polymorphism here?

Answer: All creatures have `attack()`, but every creature returns a different attack
message.

## Exercise 1: Capabilities

### 1. What To Do, What It Teaches, What Theory Is Needed

In exercise 1, you must add optional creature abilities.

You need:

- `HealCapability`
- `TransformCapability`
- healing creature family
- transform creature family
- factories for these families
- root script `capacitor.py`

This exercise teaches multiple inheritance and capability interfaces.

Theory needed:

- abstract classes
- multiple inheritance
- optional behavior
- state inside an object

### 2. How It Is Done In My Code

Files:

```text
ex1/capabilities.py
ex1/healing_creatures.py
ex1/transform_creatures.py
ex1/creature_factory.py
ex1/__init__.py
capacitor.py
```

`capabilities.py` contains:

- `HealCapability`
- `TransformCapability`

Healing creatures:

- `Sproutling`
- `Bloomelle`

Transform creatures:

- `Shiftling`
- `Morphagon`

Factories:

- `HealingCreatureFactory`
- `TransformCreatureFactory`

`TransformCapability` stores state:

```python
self.transformed = False
```

This state changes the attack result.

### 3. How To Run And Demonstrate

Run:

```bash
python3 capacitor.py
```

Show:

- healing creatures can describe, attack, and heal
- transform creatures can describe, attack, transform, attack again, and revert
- after transform, the attack changes
- after revert, the creature returns to normal state

Important for subject:

- `capacitor.py` must be at the repository root
- `ex1/` must have `__init__.py`
- ex1 must build on ex0
- capability classes should not inherit from `Creature`
- no external libraries are needed

### 4. Subject Questions

Question: Why are capabilities separate from `Creature`?

Answer: Because not all creatures have all abilities. Keeping capabilities separate
makes the base class smaller and the design easier to extend.

Question: Why does transform need state?

Answer: The creature must remember if it is transformed. The attack changes depending on
that state.

Question: Why use multiple inheritance?

Answer: A healing creature is both a `Creature` and a `HealCapability`. A transform
creature is both a `Creature` and a `TransformCapability`.

Pydantic question:

`Think About: How does Pydantic's automatic type conversion work?`

Answer: This question does not apply to this subject. Pydantic is not allowed here
because external libraries are forbidden.

`What happens when you pass a string timestamp to a datetime field?`

Answer: In Pydantic, it can convert valid timestamp strings to `datetime`, but this is
not relevant to this project and should not be used in the code.

### 5. Tricky Evaluation Questions

Question: Why not put `heal()` inside `Creature`?

Answer: Because then every creature would have a method that many creatures cannot use.
That makes the base class too large.

Question: Why call both parent initializers in transform creatures?

Answer: Because the creature part needs name and type, and the transform capability
needs its own `transformed` state.

Question: Can a creature have both heal and transform?

Answer: Yes, the design allows it. A future class could inherit from `Creature`,
`HealCapability`, and `TransformCapability`, if needed.

Question: What does `isinstance(creature, HealCapability)` check?

Answer: It checks if the object has the healing capability.

## Exercise 2: Abstract Strategy

### 1. What To Do, What It Teaches, What Theory Is Needed

In exercise 2, you must add battle strategies and a tournament.

You need:

- abstract `BattleStrategy`
- `NormalStrategy`
- `DefensiveStrategy`
- `AggressiveStrategy`
- invalid strategy handling
- root script `tournament.py`

This exercise teaches the strategy pattern.

Theory needed:

- abstract classes
- polymorphism
- strategy pattern
- exception handling
- using capabilities with `isinstance()`

### 2. How It Is Done In My Code

Files:

```text
ex2/strategies.py
ex2/__init__.py
tournament.py
```

`BattleStrategy` defines:

- `act()`
- `is_valid()`

Strategies:

- `NormalStrategy`: attacks with any creature
- `DefensiveStrategy`: works with healing creatures
- `AggressiveStrategy`: works with transform creatures

Invalid combinations raise:

```python
InvalidStrategyError
```

`tournament.py` catches this error and aborts the tournament safely.

### 3. How To Run And Demonstrate

Run:

```bash
python3 tournament.py
```

Show:

- tournament 0 works normally
- tournament 1 shows invalid strategy handling
- tournament 2 shows several opponents fighting each other

Important for subject:

- `tournament.py` must be at the repository root
- `ex2/` must have `__init__.py`
- the tournament receives pairs: factory plus strategy
- each opponent fights every other opponent once
- invalid pairs must be handled without a raw crash

### 4. Subject Questions

Question: What is a strategy?

Answer: A strategy is an object that contains battle behavior.

Question: Why use strategies?

Answer: The creature classes stay simple. Battle behavior is moved into separate
strategy classes.

Question: What makes a strategy valid?

Answer: `is_valid()` checks if the creature has the needed capability.

Pydantic question:

`Think About: How does Pydantic's automatic type conversion work?`

Answer: This is not part of this module. Pydantic is an external library and is
forbidden by the subject.

`What happens when you pass a string timestamp to a datetime field?`

Answer: In Pydantic, valid strings can be parsed into `datetime`, but this project does
not use Pydantic or `datetime` parsing.

### 5. Tricky Evaluation Questions

Question: Why does `NormalStrategy` work with every creature?

Answer: Because every creature has `attack()`.

Question: Why does `AggressiveStrategy` need `TransformCapability`?

Answer: Because it calls `transform()` and `revert()`. Normal creatures do not have
these methods.

Question: Why does `DefensiveStrategy` need `HealCapability`?

Answer: Because it calls `heal()`.

Question: Why use a custom exception?

Answer: It makes invalid strategy errors clear and easy to catch in `tournament.py`.

Question: Why not put all battle logic in `tournament.py`?

Answer: That would create many `if` statements. Strategies keep the tournament simple
and make it easier to add new battle behavior later.

## How To Check The Whole Module

Run all scripts:

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

If `mypy` is installed only in the local virtual environment:

```bash
./venv/bin/mypy battle.py capacitor.py tournament.py ex0 ex1 ex2
```

## Submission Checklist

Before submission, check:

- all root scripts exist
- all exercise folders have `__init__.py`
- scripts run with `python3`
- `flake8` passes
- `mypy` passes
- no external libraries are required by the code
- only repository files are submitted

Important file names:

- `battle.py`
- `capacitor.py`
- `tournament.py`
- `ex0/`
- `ex1/`
- `ex2/`

During evaluation, focus on understanding:

- why abstract classes are used
- why factories create families
- why capabilities are separate
- why strategies are separate from creatures
- how invalid strategy combinations are handled
