# Python Module 00 - Growing Code

## 1) What this module is about

This module is an introduction to Python basics using a garden theme.
It teaches how to:
- write simple functions
- read input and print output
- work with variables and numbers
- use conditions (`if/else`)
- repeat actions with loops and recursion
- use type annotations in function signatures
- respect flake8

The project focus is syntax, clarity, and understanding of core programming logic.

## 2) Subject rules: what is allowed and forbidden

Allowed (from subject):
- Python 3.10+ functions.
- One requested function per exercise file.
- Direct input/output inside functions.
- Basic built-ins listed in each exercise (`input`, `int`, `print`, `range`, etc.).
- Type hints are optional in general, but required by signature in ex7.

Forbidden / not expected:
- Do not write a main program in exercise files.
- Do not add `if __name__ == "__main__":` in exercise files.
- Do not call exercise functions directly inside exercise files.
- Do not add extra functions/files not requested by the exercise (except allowed recursion helper approach in ex5).
- Input validation and invalid/negative cases are not required unless explicitly asked.

## 3) Exercise by exercise breakdown

### ex0 - `ft_hello_garden`
- Task: print a welcome message.
- Learned: how to define and call a basic function.
- Python concepts: function definition (`def`), output with `print()`.
- Theory: a function groups instructions into a reusable block. `print()` writes text to standard output.

### ex1 - `ft_plot_area`
- Task: read length and width, print rectangle area.
- Learned: convert user input from text to integer and do arithmetic.
- Python concepts: `input()`, `int()`, multiplication, f-strings.
- Theory: `input()` always returns `str`, so numeric operations require conversion. Variables store intermediate values.

### ex2 - `ft_harvest_total`
- Task: read 3 daily harvest values and print total.
- Learned: aggregate multiple values into one result.
- Python concepts: integer addition, variable assignment, formatted output.
- Theory: accumulation is a basic pattern where several values are summed into a single total.

### ex3 - `ft_plant_age`
- Task: check if plant age is more than 60 days.
- Learned: make decisions from conditions.
- Python concepts: comparison operators (`>`), `if/else` branching.
- Theory: boolean expressions (`True/False`) control which branch runs.

### ex4 - `ft_water_reminder`
- Task: check days since watering and print one of two messages.
- Learned: conditional logic with threshold rules.
- Python concepts: `if/else`, integer comparison.
- Theory: conditionals encode business rules and return different outcomes for different inputs.

### ex5 - `ft_count_harvest_iterative` and `ft_count_harvest_recursive`
- Task: print day count from 1 to N, then `Harvest time!`, in two styles.
- Learned: two ways to repeat actions.
- Python concepts: `for` + `range()` (iteration), recursion (function calling itself), base case logic.
- Theory: iteration repeats with loop control variables; recursion reduces a problem into smaller calls and must stop at a base case.

### ex6 - `ft_garden_summary`
- Task: read garden name and plant count, print a 3-line summary.
- Learned: combine string and numeric data into structured output.
- Python concepts: string input, integer input, f-strings, newline formatting.
- Theory: data presentation is part of program design; output should be clear and consistent.

### ex7 - `ft_seed_inventory`
- Task: handle seed info by `seed_type`, `quantity`, `unit` and support units `packets`, `grams`, `area`.
- Learned: use typed function signatures and branch by enum-like string values.
- Python concepts: type hints (`str`, `int`, `-> None`), `if/elif/else`, string method `capitalize()`.
- Theory: type annotations improve readability and tooling support (linters, IDEs, static checkers). They document expected inputs and outputs.

## 4) How to run tests with `main.py`

From module root:

```bash
cd python_module_00
python3 main.py
```

Then choose:
- `0..7` to test one exercise
- `a` to test all exercises (interactive ones will ask for inputs)

### Why this `main.py` works from module root
- It loads files directly from `ex0` ... `ex7` by path.
- No need to move exercise files into the root directory.
- It checks that each function exists and shows readable error messages.

## 5) Python theory (short): how it works under the hood + brief history

### Short history
- Python was created by Guido van Rossum and first released in 1991.
- The language was designed to be readable, simple, and productive.
- Today Python is used in backend development, automation, data science, AI/ML, testing, and education.

### How Python works (basic flow)
1. You write source code in `.py` files.
2. The Python interpreter reads your code and compiles it to bytecode (`.pyc`).
3. This bytecode is executed by the Python Virtual Machine (PVM).
4. At runtime, Python manages memory automatically (reference counting + garbage collection).

### What is "under the hood"
- `CPython` is the standard implementation (written mostly in C).
- It includes:
  - parser + compiler (source code -> bytecode),
  - virtual machine (runs bytecode),
  - runtime system (objects, memory, exceptions, imports),
  - standard library (ready modules for common tasks).
- Python is dynamically typed: variable type is checked at runtime.
- Python is high-level: many low-level details are hidden to keep code clear.

### Code model in simple words
- Program = modules (`.py` files) + functions + classes + statements.
- Execution is top to bottom, except where control flow changes (`if`, loops, function calls).
- Functions create local scope; modules have global scope.
- Imports load code from other modules and let you reuse logic.

### Why this matters for beginners
- You can start quickly because syntax is simple.
- You still need to understand flow, scope, data types, and runtime behavior.
- Clean and readable code is a core Python principle.
