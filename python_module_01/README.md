# Python Module 01 — Overview and Theory (Simple English)

This module is a small учебный проект about Python basics and OOP with a “garden” theme. All examples are standalone: you can run each file with `python3 file_name.py`.

## What Each Exercise Does

### ex0: `ft_garden_intro.py`
- Shows variables and formatted output.
- Function `ft_garden_intro()` prints basic plant info.

### ex1: `ft_garden_data.py`
- Introduces a `Plant` class with fields `name`, `height`, `days`.
- Creates several objects and prints their data using `print_info()`.

### ex2: `ft_plant_growth.py`
- Adds methods `grow()` and `age()` to the `Plant` class.
- Simulates plant growth for one week using loops.

### ex3: `ft_plant_factory.py`
- Adds a counter of created objects: `Plant._total_plants`.
- Mass creation from a list of tuples.
- Prints total number of created plants.

### ex4: `ft_garden_security.py`
- `SecurePlant` uses protected fields `_height`, `_age`.
- Setters `set_height()` and `set_age()` with validation.
- Demonstrates “protected” access to data.

### ex5: `ft_plant_types.py`
- Inheritance: base `Plant`, derived `Flower`, `Tree`, `Vegetable`.
- Polymorphism: shared method `print_info()` for different types.
- Each type has its own behavior (blooming, shade, nutrition).

### ex6: `ft_garden_analytics.py`
- Multi-level inheritance (`Plant` → `FloweringPlant` → `PrizeFlower`).
- Manager class `GardenManager` stores gardens in a dict.
- Nested class `GardenStats` handles analytics.
- Example `@classmethod` (factory) and `@staticmethod` (stateless utility).

## 0.1) Architecture of ex6 (Based on the Fixed Code)

```
[ft_garden_analytics.py]
  Plant
    ├─ grow()                (common method)
    └─ print_info()          (base for polymorphism)
        ^
        | is-a
  FloweringPlant(Plant)
    ├─ +color, +blooming
    └─ print_info() OVERRIDE (different print)
        ^
        | is-a
  PrizeFlower(FloweringPlant)
    ├─ +score
    └─ print_info() OVERRIDE (different print again)

  GardenManager
    ├─ gardens: dict                        has-a (storage)
    ├─ create_garden_network() classmethod  (alternate constructor)
    ├─ is_valid_height() staticmethod       (utility, no state)
    ├─ add_garden/add_plant/help_plants_grow/report/compare/total
    └─ GardenStats (nested helper)          has-a/uses
         ├─ plants_added/total_growth
         ├─ type_breakdown (isinstance + inheritance)
         └─ garden_score (aggregation: height + bonuses)

ABC/Protocol: NO (and not required by subject)
override: YES — print_info() in FloweringPlant and PrizeFlower
polymorphism: YES — calling plant.print_info() on different objects
```

## 0.2) Flow (What Happens When Running ex6)

1. Python runs the file -> `if __name__ == "__main__":` is TRUE
2. `ft_garden_analytics()` is called

`ft_garden_analytics()`:
3. Print header
4. `garden_manager = GardenManager.create_garden_network()`
   - classmethod -> returns `cls()` -> creates `GardenManager()`
   - `__init__` -> `self.gardens = {}`
5. `add_garden("Alice")`, `add_garden("Bob")`
   - creates `gardens["Alice"]` and `gardens["Bob"]`
6. Create plants:
   - `oak = Plant(...)`
   - `rose = FloweringPlant(...)`
   - `sun_flower = PrizeFlower(...)`
7. `add_plant(...)` puts objects into the right lists
8. `help_plants_grow("Alice")`:
   - for each plant in `gardens["Alice"]["plants"]`:
     - `plant.grow()` (common call)
     - `stats["total_growth"] += 1`
9. `report("Alice")`:
   - for each plant: `plant.print_info()`  <-- POLYMORPHISM
     - `oak` -> `Plant.print_info`
     - `rose` -> `FloweringPlant.print_info`
     - `sun_flower` -> `PrizeFlower.print_info`
   - then `GardenStats` calculates added/growth/type_breakdown
10. `is_valid_height(oak.height)` -> True/False
11. `compare_garden_scores()` -> `GardenStats.garden_score()` for each owner
12. `total_gardens()` -> `len(self.gardens)`

Garden Structure
```
{
   "Alice": {
       "plants": [],
       "stats": {
           "plants_added": 0,
           "total_growth": 0
       }
   }
}
```

GardenManager
```
GardenManager
│
└── gardens (dict)
     │
     ├── "Alice"
     │     │
     │     ├── plants (list)
     │     │      ├─ Plant
     │     │      ├─ FloweringPlant
     │     │      └─ PrizeFlower
     │     │
     │     └── stats (dict)
     │            ├─ plants_added
     │            └─ total_growth
     │
     └── "Bob"
           │
           ├── plants
           └── stats
```

## Key Terms and Concepts

- Variable: a name that points to a value (`plant_name`, `height`).
- Function: a block of code you call by name (`ft_garden_intro()`).
- Class: a template for objects (`class Plant`).
- Object (instance): a concrete item made from a class (`rose = Plant(...)`).
- Attribute: data inside an object (`self.height`).
- Method: a function inside a class (`grow()`, `print_info()`).
- Encapsulation: hide details, access through methods.
  - In Python, `_height` means “internal” by convention.
- Inheritance: one class extends another (`class Flower(Plant)`).
- Polymorphism: one interface, different behavior.
  - Here: same `print_info()` for different plant types.
- `super()`: call parent constructor/method.
- `@classmethod`: class-level method with `cls`.
- `@staticmethod`: method without `self` or `cls`.
- `isinstance(obj, Class)`: check object type.
- Lists (`list`): ordered collections (`plants = [ ... ]`).
- Tuples (`tuple`): immutable groups (`("Rose", 25, 30)`).
- Dicts (`dict`): key-value pairs (`{"plants": [], "stats": {...}}`).
- Type hints: hints for readability and tools (`def grow(self) -> None`).

## How To Run

Each file is standalone:

```bash
python3 python_module_01/ex0/ft_garden_intro.py
python3 python_module_01/ex1/ft_garden_data.py
python3 python_module_01/ex2/ft_plant_growth.py
python3 python_module_01/ex3/ft_plant_factory.py
python3 python_module_01/ex4/ft_garden_security.py
python3 python_module_01/ex5/ft_plant_types.py
python3 python_module_01/ex6/ft_garden_analytics.py
```