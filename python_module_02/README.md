# Garden Guardian - Python Module 02

## 1) What this module is about

This module teaches Python exception handling for robust programs.
Theme: smart agriculture data pipelines that must keep working even when bad data or runtime problems appear.

Main learning goals:
- handle runtime errors with `try/except`
- distinguish common built-in exception types
- create custom exceptions for domain-specific errors
- always clean up resources with `finally`
- explicitly signal invalid states with `raise`
- combine all techniques in one small management system

---

## 2) Subject rules: what is allowed and expected

- Python `3.10+`
- `flake8` style
- type hints in functions/methods
- one exercise per file
- all programs must not crash
- use exception handling clearly (`try`, `except`, `finally`, `raise`)
- keep solutions simple and focused on learning

General built-in exceptions allowed by subject include:
`ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`, `KeyError`, `IndexError`, `AttributeError`, `Exception`.

Important practical expectations:
- show both normal path and error path in test function
- catch errors and continue execution
- print clear, user-friendly error messages
- use custom exceptions when built-ins are not expressive enough

---

## 3) Exercise-by-exercise breakdown

### ex0 - `ft_first_exception`

Task:
- validate temperature input for plants (`0..40`)
- convert `str` to `int`
- catch invalid numeric conversion

This exercise demonstrates:
- `check_temperature(temp_str)` returns `int | None`
- handles good input, non-number input, too-low and too-high ranges
- `test_temperature_input()` proves program keeps running after errors

Core concept:
- `ValueError` from `int("abc")` is expected and handled safely

---

### ex1 - `ft_different_errors`

Task:
- show multiple common exception types

This exercise demonstrates:
- `ValueError` (`int("plant")`)
- `ZeroDivisionError` (`42 / 0`)
- `FileNotFoundError` (`open("missing.txt")`)
- `KeyError` (missing dict key)
- grouped handler: `except (ZeroDivisionError, ValueError):`

Core concept:
- different failures have different types; one codebase can catch each specifically or several together

---

### ex2 - `ft_custom_errors`

Task:
- create custom exception hierarchy for garden domain

This exercise demonstrates:
- `GardenError(Exception)` as base domain error
- `PlantError(GardenError)` and `WaterError(GardenError)` as specialized children
- raising and catching specific and parent-level errors

Core concept:
- inheritance allows broad handling (`GardenError`) and precise handling (`PlantError` / `WaterError`)

---

### ex3 - `ft_finally_block`

Task:
- show cleanup that always runs

This exercise demonstrates:
- opens watering system message
- iterates plants and raises error for invalid item (`None`)
- catches `ValueError`
- always executes cleanup in `finally`

Core concept:
- `finally` executes whether exception happened or not

---

### ex4 - `ft_raise_errors`

Task:
- validate plant health data and raise clear errors when invalid

This exercise demonstrates:
- `check_plant_health(plant_name, water_level, sunlight_hours)`
- explicit validation boundaries:
  - plant name not empty
  - water in `1..10`
  - sunlight in `2..12`
- raises `ValueError` with descriptive messages

Core concept:
- `raise` is used for defensive programming and precise error reporting

---

### ex5 - `ft_garden_management`

Task:
- integrate all module concepts into one small system

This exercise demonstrates:
- `GardenManager` with methods: `add_plant`, `water_plants`, `check_plant_health`
- custom exceptions reused (`GardenError`, `PlantError`, `WaterError`)
- `try/except/finally` inside operations and in test scenario
- graceful error recovery while continuing later operations

Core concept:
- reliability comes from combining validation, raising, catching, cleanup, and recovery logic

---

## 4) How to run

From module root:

```bash
cd python_modules_git2/python_module_02
python3 ex0/ft_first_exception.py
python3 ex1/ft_different_errors.py
python3 ex2/ft_custom_errors.py
python3 ex3/ft_finally_block.py
python3 ex4/ft_raise_errors.py
python3 ex5/ft_garden_management.py
```

If you want, run all quickly:

```bash
for f in ex*/ft_*.py; do python3 "$f"; echo; done
```

---

## 5) Theory (Exceptions + Call Stack)

### 5.1 `try`, `except`, `else`, `finally`

- `try`: execute risky code that may fail.
- `except`: catch and handle an exception object if its type matches.
- `else`: execute only when the `try` block finished with no exception.
- `finally`: execute cleanup code in all cases (success, handled error, or propagated error).

Pattern:

```python
try:
    risky_operation()
except ValueError as e:
    print("Handled:", e)
else:
    print("No errors")
finally:
    print("Cleanup always runs")
```

Detailed flow:
- When an error happens (or you call `raise`), Python creates an exception object.
- This object is usually an instance of an exception class (for example `ValueError`).
- Common useful attributes are:
  - `args`: tuple with constructor arguments/message
  - `__traceback__`: traceback object (call stack at failure point)
  - `__cause__`: explicit chained cause (`raise ... from e`)
  - `__context__`: previous exception during implicit chaining
- Useful methods for representation include:
  - `__str__()` -> readable message
  - `__repr__()` -> debug representation
- Then Python checks `except` blocks from top to bottom:
  - if type matches, that handler executes (the exception is caught/handled there)
  - if type does not match, Python continues searching next `except`
  - if no handler matches in this frame, exception propagates to caller (stack unwinding)

---

### 5.2 `raise` and why it matters

Use `raise` to throw and trigger an exception when data is invalid and function cannot continue correctly.

```python
def set_water(level: int) -> None:
    if level < 1 or level > 10:
        raise ValueError(f"Invalid water level: {level}")
```

Why:
- fail fast
- prevent corrupted state
- make caller decide recovery strategy

---

### 5.3 Exception inheritance

Exceptions are classes.
You can build a tree:

```text
Exception
└── GardenError
    ├── PlantError
    └── WaterError
```

Benefits:
- catch specific error when needed
- catch parent for a whole category

```python
try:
    do_garden_work()
except PlantError:
    print("Plant-specific issue")
except GardenError:
    print("Any garden issue")
```

Order matters: specific first, broad later.

---

### 5.4 What `as e` means in `except`

```python
except ValueError as e:
```

- `ValueError` is the exception type
- `e` is the exception object instance that was raised
- `str(e)` is usually the human-readable message

You can inspect more:
- `type(e)` for class
- traceback info via `traceback` module

---

### 5.5 Call stack basics: top, bottom, push, pop

Call stack is a LIFO structure (Last In, First Out):
- bottom: oldest frame (first call)
- top: current active frame (latest call)

Operations:
- push: when a function is called, new frame is pushed to top
- pop: when function returns (or crashes), top frame is popped

Example flow:

```python
def c():
    raise ValueError("boom")

def b():
    c()

def a():
    b()

a()
```

Stack evolution:
1. start: `[]`
2. call `a` -> push `a`: `[a]`
3. `a` calls `b` -> push `b`: `[a, b]`
4. `b` calls `c` -> push `c`: `[a, b, c]` (top is `c`)
5. `c` raises `ValueError`
6. if `c` does not catch it, stack unwinds:
   - pop `c`, propagate to `b`
   - if `b` does not catch, pop `b`, propagate to `a`
   - if `a` does not catch, pop `a`, program-level traceback

This is called exception propagation (bubbling up the stack).

---

### 5.6 Propagation and re-raising

You can catch, log, and re-raise:

```python
def parse_temp(text: str) -> int:
    try:
        return int(text)
    except ValueError as e:
        print("parse_temp failed:", e)
        raise
```

- bare `raise` re-throws the same exception, preserving traceback

Or wrap with context:

```python
def load_sensor_value(text: str) -> int:
    try:
        return int(text)
    except ValueError as e:
        raise ValueError("Bad sensor payload") from e
```

`from e` creates exception chaining:
- high-level message for your domain
- keeps original root cause

---

### 5.7 Practical reliability rules

- catch only errors you can handle
- do not hide unexpected exceptions silently
- keep error messages precise and actionable
- clean up resources in `finally` or with context managers (`with`)
- use custom exceptions for domain clarity
- validate early, raise early

About catching "everything":
- `except Exception as e:` catches almost all normal runtime/application errors.
- `except BaseException as e:` catches truly everything, including system-level signals like `KeyboardInterrupt` and `SystemExit`.

Difference:
- `Exception` is for regular program errors (recommended in most broad handlers).
- `BaseException` is the root of all exceptions, including ones that usually should not be swallowed.

ASCII class map (demo):

```text
BaseException
├── Exception
│   ├── ValueError
│   ├── TypeError
│   ├── ZeroDivisionError
│   ├── KeyError
│   └── FileNotFoundError
├── SystemExit
├── KeyboardInterrupt
└── GeneratorExit
```

When to use:
- Use `Exception` for top-level safety boundaries (for example service loop, CLI command boundary) where you can log and recover.
- Use `BaseException` only in rare infrastructure cases (final cleanup/logging/re-raise), and usually re-raise immediately.

When not to use:
- Do not use broad catch inside core business logic if you cannot recover meaningfully.
- Do not swallow `BaseException`, because it may block normal process stop (`Ctrl+C`) or exit flow.

These rules are exactly what Module 02 builds step by step.

---

## 6) Quick Q&A (Interview style)

### Q1: How is `raise` different from `except`?
A:
- `raise` throws/triggers an exception.
- `except` catches/handles an exception.
- In short: `raise` creates the failure signal, `except` processes it.

### Q2: Why use separate error types?
A:
- To react differently to different failures.
- `ValueError` means bad value, `FileNotFoundError` means missing file, etc.
- Specific types make logs, debugging, and recovery logic much clearer.

### Q3: Why is `finally` important?
A:
- It guarantees cleanup logic executes in both success and failure paths.
- Typical use: close file/socket/connection, release lock, stop resource.

### Q4: When should you catch a specific type vs `Exception`?
A:
- Catch concrete type (`ValueError`, `KeyError`, custom error) when you know exactly how to recover.
- Catch `Exception` at top-level boundaries (CLI entrypoint, worker loop, API handler) to prevent app crash and return controlled response.

### Q5: What happens if an exception is not caught?
A:
- It propagates up the call stack.
- If no frame catches it, program stops with traceback.

### Q6: Why should `except Exception` not be used everywhere?
A:
- It can hide real bugs and make debugging harder.
- It may convert serious coding errors into silent bad behavior.
- Broad catch should be rare and placed at boundaries, not deep in business logic.

### Q7: How should an error message be written?
A:
- Include what is wrong, actual value, expected range/format, and context.
- Good: `"Water level 15 is too high (max 10)"`
- Weak: `"Invalid input"`

### Q8: What is the benefit of custom exceptions in a real project?
A:
- Domain clarity (`PaymentError`, `AuthError`, `GardenError`).
- Clean grouping and selective handling by category.
- Better API contracts between modules and cleaner monitoring/alerts.

### Q9: Why does `finally` run even when there is a `return`?
A:
- Python executes `finally` before the function actually exits.
- This guarantees cleanup even when leaving early.

Example (`return` in `try`):

```python
def demo_try_return() -> int:
    try:
        return 10
    finally:
        print("finally from try")
```

Example (`return` in `except`):

```python
def demo_except_return(x: str) -> int:
    try:
        return int(x)
    except ValueError:
        return -1
    finally:
        print("finally from except")
```

### Q10: What is better: print the error inside a function or propagate it upward?
A:
- If function is low-level/library-like: raise and let caller decide.
- If function is top-level/UI boundary: catch and print/log user-facing message.

Approach 1 (print inside function):

```python
def parse_local(text: str) -> int | None:
    try:
        return int(text)
    except ValueError as e:
        print("Parse error:", e)
        return None
```

Approach 2 (propagate upward):

```python
def parse_core(text: str) -> int:
    return int(text)  # may raise ValueError

def main() -> None:
    try:
        value = parse_core("abc")
        print(value)
    except ValueError as e:
        print("Input is invalid:", e)
```

### Q11: When should one `except` handle multiple types?
A:
- When recovery action is identical for several errors.
- Example: same fallback for `ValueError` and `TypeError`.

```python
try:
    risky()
except (ValueError, TypeError) as e:
    print("Bad data:", e)
```

### Q12: How do you verify that error handling really works?
A:
- Run positive and negative tests intentionally.
- Trigger each expected error path at least once.
- Verify:
  - app does not crash unexpectedly
  - correct handler is executed
  - message is clear
  - cleanup (`finally`) really runs
  - program can continue when it should
