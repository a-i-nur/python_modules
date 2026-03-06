# CodeCultivation - Python Module 01

## 1) What this module is about and what it teaches

This module is about building a small "digital garden system" with Python classes.
It starts from program entry point basics and moves to Object-Oriented Programming (OOP).

Main learning goals:
- Understand how a Python file starts execution (`if __name__ == "__main__":`).
- Model real objects with classes (`Plant`, `SecurePlant`, `GardenManager`).
- Split data and behavior into methods.
- Use inheritance to avoid code duplication.
- Protect data with encapsulation and validation.
- Use method types correctly:
instance methods, `@classmethod`, `@staticmethod`.
- Organize a bigger architecture with nested helper class (`GardenStats`).

---

## 2) What you can use and what you cannot use


Global project rules:
- Python `3.10+`
- Follow `flake8` style
- One exercise = one file
- Naming:
classes in `PascalCase`, functions/variables in `snake_case`
- Type hints for functions/methods
- Code must run without errors
- From ex1 and later, use classes

Authorized by exercise:
- `ex0`: `print()`
- `ex1`: `print()`, `range()`
- `ex2`: `print()`, `range()`
- `ex3`: `print()`, `range()`
- `ex4`: `print()`, `range()`
- `ex5`: `super()`, `print()`, `range()`
- `ex6`: `super()`, `print()`, `range()`, `staticmethod()`, `classmethod()`

Practical "cannot":
- Do not break required file/function names.
- Do not replace OOP tasks with global procedural code.
- Do not bypass validation logic in security exercise.
- Do not duplicate base logic when inheritance is required.

---

## 3) Exercise-by-exercise breakdown

### ex0 - `ft_garden_intro`

What to do:
- Create a runnable script with a start point.
- Store simple plant data in variables and print it.

What it teaches:
- Program entry point.
- Script execution vs module import behavior.

Python concept used:
- `if __name__ == "__main__":`

Short theory:
- When Python executes a file directly, `__name__` is `"__main__"`.
- When the file is imported, `__name__` is the module name.
- This pattern lets you keep test/demo code at the bottom safely.

### ex1 - `ft_garden_data`

What to do:
- Create a `Plant` class with name/height/days.
- Build at least 3 objects and print structured info.

What it teaches:
- Basic class design.
- Object instantiation.

Python concept used:
- `class`, `__init__`, instance attributes, instance method.

Short theory:
- A class is a blueprint.
- An object is one concrete instance with its own state.
- `__init__` is a constructor-like initializer called at creation.

### ex2 - `ft_plant_growth`

What to do:
- Reuse `Plant` and add behaviors: `grow()`, `age()`, `get_info()`.
- Simulate one week of growth.

What it teaches:
- Behavior inside class methods.
- State transitions over time.

Python concept used:
- Encapsulating logic in methods.
- Iteration over collections of objects.

Short theory:
- OOP is not only data storage; objects should own actions on their state.
- A method updates object fields in a controlled place.

### ex3 - `ft_plant_factory`

What to do:
- Create many plants efficiently with initial values.
- Print all created plants and total count.

What it teaches:
- Constructor usage at scale.
- Shared class-level state (`_total_plants`).

Python concept used:
- Class attributes vs instance attributes.

Short theory:
- Instance attribute belongs to one object (`self.name`).
- Class attribute belongs to the class itself (`Plant._total_plants`) and is shared.

### ex4 - `ft_garden_security`

What to do:
- Build `SecurePlant` with protected internal data.
- Validate height/age so they cannot be negative.

What it teaches:
- Encapsulation and data integrity.
- Safe write access patterns.

Python concept used:
- Name mangling with `__height`, `__age`.
- `@property` + setters for controlled access.

Short theory:
- `@property` lets you expose method logic like attribute syntax.
- Setter can reject invalid values before storing.
- This keeps object state consistent.

### ex5 - `ft_plant_types`

What to do:
- Build hierarchy: base `Plant` + `Flower`, `Tree`, `Vegetable`.
- Add specific fields/methods per child type.
- Use `super().__init__()`.

What it teaches:
- Inheritance and override.
- Reuse common code from parent class.

Python concept used:
- Method overriding (`print_info` in each child).
- Parent constructor call with `super()`.

Short theory:
- Inheritance models "is-a" relation.
- Child class extends parent behavior.
- Override customizes behavior while keeping shared interface.

### ex6 - `ft_garden_analytics`

What to do:
- Build full analytics platform with manager + nested stats helper.
- Build inheritance chain `Plant -> FloweringPlant -> PrizeFlower`.
- Use instance, class, and static methods.

What it teaches:
- Multi-component architecture.
- Method type selection by responsibility.
- Analytics design around stored domain objects.

Python concepts used:
- `@classmethod` for type-level factory (`create_garden_network`).
- `@staticmethod` for utility validation (`is_valid_height`).
- Nested class (`GardenStats`) for grouped analytics logic.
- Polymorphism via `calculate_score()` and `print_info()`.

Short theory:
- Choose instance method when method needs `self`.
- Choose class method when method acts on class (`cls`) and may create objects.
- Choose static method for pure utility not needing `self/cls`.
- Polymorphism allows one loop to call same method name on different types.

#### ex6 project schema

```text
ft_garden_analytics.py
|
+-- Plant
|   +-- fields: name, height, age, type
|   +-- methods: grow, print_info, calculate_score
|
+-- FloweringPlant(Plant)
|   +-- fields: color, blooming
|   +-- methods: print_info(override), calculate_score(override)
|
+-- PrizeFlower(FloweringPlant)
|   +-- fields: score
|   +-- methods: print_info(override), calculate_score(override)
|
+-- GardenManager
    +-- gardens: { owner: {plants: [], stats: {...}} }
    +-- methods:
        - create_garden_network (classmethod)
        - is_valid_height (staticmethod)
        - add_garden, add_plant, help_plants_grow, report,
          compare_garden_scores, total_gardens
    +-- nested class GardenStats
        - plants_added
        - total_growth
        - type_breakdown
        - garden_score
```

#### ex6 run flow schema

```text
Start ft_garden_analytics()
  -> GardenManager.create_garden_network()
  -> add_garden("Alice"), add_garden("Bob")
  -> create plants (Plant / FloweringPlant / PrizeFlower)
  -> add_plant(...) into gardens
  -> help_plants_grow("Alice")
       -> each plant.grow()
       -> stats.total_growth += 1
  -> report("Alice")
       -> print plant info (polymorphism)
       -> GardenStats calculations
  -> is_valid_height(...)
  -> compare_garden_scores()
       -> sum via plant.calculate_score() (polymorphism)
  -> total_gardens()
End
```

#### ex6 core structures schema

```text
GardenManager.gardens
{
  "Alice": {
    "plants": [Plant, FloweringPlant, PrizeFlower, ...],
    "stats": {
      "plants_added": int,
      "total_growth": int
    }
  },
  "Bob": {
    "plants": [...],
    "stats": {...}
  }
}
```

---

## 4) How to run with test `main.py`

From module root:

```bash
cd python_module_01
python3 main.py
```

Menu:
- `0`..`6` to run one exercise
- `a` to run all exercises sequentially

You can also run each file directly, for example:

```bash
python3 ex6/ft_garden_analytics.py
```

---

## 5) Python execution model, `__init__`, `__name__`, and dunder methods

### 5.1 Why `if __name__ == "__main__":` works

Important: use `==`, not `=`.

- `=` means assignment.
- `==` means comparison.

How Python sets `__name__`:
- If file runs directly (`python3 file.py`) -> `__name__` is `"__main__"`.
- If file is imported -> `__name__` is module path/name.

Why this block is useful:
- Keep demo/test code in the same file.
- Prevent this demo code from running on import.
- Make module reusable in bigger projects.

### 5.2 What `__init__` really does

`__init__` is an initializer, not the object creator itself.

Creation flow:
1. Python calls `__new__` to create a new instance.
2. Python calls `__init__` to fill that instance with initial state.
3. You receive a ready object.

Important details:
- `__init__` must return `None`.
- Real memory/object allocation is in `__new__`.
- For most user classes, you usually define only `__init__`.

### 5.3 What are dunder (magic) methods

"Dunder" means "double underscore", like `__init__`.
These methods are special protocol hooks used by Python internals.

Common examples:
- Object lifecycle: `__new__`, `__init__`, `__del__`
- String representation: `__repr__`, `__str__`
- Size/truth: `__len__`, `__bool__`
- Container access: `__getitem__`, `__setitem__`, `__iter__`
- Comparisons: `__eq__`, `__lt__`, `__gt__`
- Arithmetic: `__add__`, `__sub__`, `__mul__`
- Call behavior: `__call__`
- Attribute access hooks: `__getattr__`, `__getattribute__`, `__setattr__`

Why they matter:
- Python syntax maps to these methods.
- Example: `len(obj)` calls `obj.__len__()`.
- Example: `a + b` calls `a.__add__(b)`.

### 5.4 How Python code maps to protocols

Small mapping table:
- `print(obj)` -> `obj.__str__()` (or fallback to `__repr__`)
- `obj1 == obj2` -> `obj1.__eq__(obj2)`
- `for x in obj` -> iterator protocol (`__iter__` / `__next__`)
- `obj[key]` -> `obj.__getitem__(key)`
- `if obj:` -> `obj.__bool__()` or `__len__()`

This is why "magic methods" are core Python behavior, not side features.

### 5.5 Everything is an object in Python

In Python, values are objects:
- `int`, `str`, `list`, `dict`, functions, classes, modules, exceptions.

Implications:
- Every object has type and identity.
- You can inspect type with `type(obj)`.
- Classes are objects too (created by metaclass `type`).
- Functions are first-class objects (store in variables, pass as args).

### 5.6 How to inspect dunder methods and internals

Useful tools:
- `dir(obj)` -> available attributes/methods, including dunder names.
- `type(obj)` -> exact runtime class.
- `isinstance(obj, Class)` -> relation check.
- `help(obj)` -> docs + signatures.
- `obj.__dict__` -> instance attribute storage (if available).
- `Class.__mro__` or `Class.mro()` -> method resolution order.

Quick REPL examples:

```python
class A:
    def __init__(self, x):
        self.x = x
    def __len__(self):
        return self.x

a = A(3)
print(type(a))       # <class '__main__.A'>
print(len(a))        # 3 -> calls __len__
print(a.__dict__)    # {'x': 3}
print(A.mro())       # [A, object]
```

### 5.7 Dunder naming vs private naming

Do not mix these:
- `__init__` style: reserved special protocol names (language-defined behavior).
- `__height` style: name mangling for class-internal attributes.

Both use double underscore, but purpose is different.

### 5.8 How Python executes your code internally

High-level pipeline:
1. Source `.py` is parsed to AST (syntax tree).
2. AST is compiled to bytecode instructions.
3. Python VM executes bytecode.

Why this is useful for dunder understanding:
- Many bytecode ops call object protocols (dunder hooks).
- Example: binary add op dispatches to `__add__`.
- Attribute read can trigger `__getattribute__`.

How to inspect:
- `dis` module shows bytecode.

Example:

```python
import dis

def demo(a, b):
    return a + b

dis.dis(demo)
```

This helps you see where Python triggers protocol-based behavior.

---

## 6) OOP theory in Python (simple language)

### 6.1 What is OOP

OOP is a style where code is built around objects.
Object = data + behavior.
Class = blueprint for objects.

In Python:
- class defines structure and methods
- object stores its own state
- methods describe actions

### 6.2 Core terms

- `class`: template (for example `Plant`)
- `instance`: real object from class (for example one rose)
- `attribute`: object data (`self.height`)
- `method`: function inside class (`grow()`)
- `self`: current object reference

### 6.3 Abstraction in Python

Meaning:
- Show only useful interface.
- Hide internal details.

How in Python:
- Public methods form API (`grow`, `report`).
- Internal implementation can change without changing API.
- Optional: `abc` module with abstract base classes (`ABC`, `@abstractmethod`)
for strict interface contracts.

Simple example idea:
- User calls `garden_manager.report("Alice")`.
- User does not need to know how stats are counted internally.

### 6.4 Encapsulation in Python

Meaning:
- Keep object state safe and consistent.

Python tools:
- Naming conventions:
  - `name`: public API
  - `_name`: internal/protected by convention (not strict)
  - `__name`: name mangling (`_ClassName__name`) to reduce accidental access
- `@property` for controlled access
- setter validation for safe writes

#### 6.4.1 `_` vs `__` (important)

- `_attr`:
  - "internal use" signal to developers
  - still accessible directly
- `__attr`:
  - Python rewrites name internally (name mangling)
  - harder to access by mistake
  - not true security, but practical protection

#### 6.4.2 Properties, getters, setters

In Pythonic style:
- Prefer `@property` over manual `get_x()/set_x()` when possible.
- External code uses `obj.height` syntax.
- Internally, getter/setter methods run logic (validation, computed values).

Pattern:

```python
class SecurePlant:
    def __init__(self, height: int):
        self.__height = 0
        self.height = height

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
```

Why useful:
- keep simple usage syntax
- centralize validation
- protect invariants

### 6.5 Inheritance in Python

Meaning:
- Child class reuses and extends parent class.

Syntax:
- `class Flower(Plant): ...`
- `super().__init__(...)` calls parent initializer

Useful features:
- Code reuse for shared fields/methods
- Method overriding for custom behavior
- Multi-level inheritance (`Plant -> FloweringPlant -> PrizeFlower`)
- Multiple inheritance supported in Python (use carefully)

Method Resolution Order (MRO):
- Python decides which parent method to call using MRO.
- You can inspect with `ClassName.mro()`.

### 6.6 Polymorphism in Python

Meaning:
- One interface, many implementations.

In practice:
- Different classes define same method names (`print_info`, `calculate_score`).
- One loop calls method on mixed object list.
- Correct override runs by real object type at runtime.

Kinds often seen in Python:
- Subtype polymorphism (inheritance + overriding) -> used in this module.
- Duck typing polymorphism ("if it has needed method, it works").
- Operator overloading (`__add__`, `__len__`, etc.) for custom behavior.

### 6.7 Method types in Python classes

- Instance method:
  - first arg `self`
  - uses object state
- Class method:
  - decorator `@classmethod`, first arg `cls`
  - operates on class level, often factory constructors
- Static method:
  - decorator `@staticmethod`
  - utility logic grouped in class namespace

Quick rule:
- Need object data -> instance method
- Need class/type data or alternative constructor -> class method
- Need utility helper near class context -> static method

### 6.8 Other useful OOP-related principles in Python

- Composition over inheritance:
  - often better to store helper objects than build deep hierarchies
- Single Responsibility:
  - one class should have one clear role
  - example: `GardenStats` only calculates stats
- Open/Closed principle (practical view):
  - add new plant type by extending classes, avoid rewriting manager core
- Cohesion and coupling:
  - keep related logic together, reduce hard dependencies

---

## Final note

By ex6, you moved from simple script execution to structured OOP architecture:
objects, inheritance, encapsulation, polymorphism, and class-level design decisions.
That is the main value of module 01.
