# Python Module 09 - Cosmic Data

## VSCode And mypy Troubleshooting

Sometimes `mypy` in the terminal says that everything is OK, but VSCode shows an
error like this:

```text
Cannot find implementation or library stub for module named "pydantic"
```

This usually means that the terminal and VSCode use different Python environments.

In the terminal, the local virtual environment may be active:

```text
(.venv)
```

But VSCode may still use another Python interpreter where `pydantic` is not
installed.

To fix it:

1. Open the command palette in VSCode:

```text
Ctrl+Shift+P
```

2. Run:

```text
Python: Select Interpreter
```

3. Select the project virtual environment:

```text
/home/dev/projects/42/python_modules/python_module_09/.venv/bin/python
```

4. Reload VSCode:

```text
Ctrl+Shift+P
Developer: Reload Window
```

After this, VSCode should use the same environment as the terminal.

Useful terminal checks:

```bash
which python
which mypy
python -c "import pydantic; print(pydantic.__version__)"
```

They should point to `.venv` or use packages installed inside `.venv`.

## What This Module Is About

This module teaches basic data validation with Pydantic.

The main idea is simple: in real programs, data can be wrong. A number can be too
large, a required field can be missing, or a date can have the wrong format.
Pydantic helps us describe what valid data should look like and then checks the
data for us.

In this module, we learn how to:

- create Pydantic models with `BaseModel`;
- add field rules with `Field`;
- use Python type hints for validation;
- work with optional fields;
- understand validation errors;
- later, use custom validation and nested models.

## Theory To Know

### Type Hints

Python type hints describe what type a value should have.

Example:

```python
crew_size: int
name: str
power_level: float
```

Pydantic reads these type hints and uses them during validation.

### BaseModel

`BaseModel` is the base class for Pydantic models.

When a class inherits from `BaseModel`, Pydantic can validate the fields of that
class.

```python
from pydantic import BaseModel


class SpaceStation(BaseModel):
    name: str
```

### Field

`Field` adds extra rules to a field.

Example:

```python
crew_size: int = Field(ge=1, le=20)
```

This means:

- `ge=1`: greater than or equal to 1;
- `le=20`: less than or equal to 20.

For strings:

```python
station_id: str = Field(min_length=3, max_length=10)
```

This means the string must have between 3 and 10 characters.

Common `Field` arguments in this module:

- `default`: value used when the field is not provided;
- `min_length`: minimum length for a string;
- `max_length`: maximum length for a string;
- `ge`: greater than or equal, `>=`;
- `gt`: greater than, `>`;
- `le`: less than or equal, `<=`;
- `lt`: less than, `<`.

Examples:

```python
crew_size: int = Field(ge=1, le=20)
```

This allows `1` and `20`.

```python
signal_strength: float = Field(gt=0.0, lt=10.0)
```

This does not allow `0.0` or `10.0`.

For this subject, ranges like `0.0-10.0` and `1-1440` are treated as inclusive,
so the solution uses `ge` and `le`.

### Optional Fields

An optional field can be missing or set to `None`.

```python
notes: str | None = Field(default=None, max_length=200)
```

`str | None` means the value can be a string or `None`.

`default=None` means that if the user does not provide `notes`, Pydantic will use
`None`.

### ValidationError

When data is invalid, Pydantic raises a `ValidationError`.

In this exercise, we catch this error to show the validation message:

```python
except ValidationError as error:
    print(error.errors()[0]["msg"])
```

## Lore And Connection To The Theory

The module uses a space story. We work for a cosmic data observatory.

The lore is not just decoration. It gives a practical reason for validation:

- a space station must have a valid crew size;
- power and oxygen levels must stay between 0 and 100 percent;
- contact reports must follow special rules;
- space missions must have a valid crew.

This matches real software. APIs, databases, forms, and files all receive data.
Before using that data, a program must check that it is valid.

## Exercise 0 - Space Station Data

### What To Do

Create the file:

```text
ex0/space_station.py
```

Inside this file, create a `SpaceStation` Pydantic model with these fields:

- `station_id`: string, 3 to 10 characters;
- `name`: string, 1 to 50 characters;
- `crew_size`: integer, from 1 to 20;
- `power_level`: float, from 0.0 to 100.0;
- `oxygen_level`: float, from 0.0 to 100.0;
- `last_maintenance`: `datetime`;
- `is_operational`: boolean, default value `True`;
- `notes`: optional string, maximum 200 characters.

Also create a `main()` function that:

- creates a valid station;
- prints the station data;
- tries to create an invalid station;
- prints the validation error.

### What This Exercise Teaches

This exercise teaches the foundation of Pydantic:

- how to create a model;
- how to validate basic fields;
- how to set minimum and maximum values;
- how to use default values;
- how to catch and display validation errors.

The needed theory is:

- Python classes;
- type hints;
- `datetime`;
- `BaseModel`;
- `Field`;
- `ValidationError`.

### How My Solution Is Made

My solution defines this model:

```python
class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(max_length=200, default=None)
```

In `main()`, I create a valid station first.

Then I create another station with:

```python
crew_size=25
```

This is invalid because the maximum crew size is 20. Pydantic raises a
`ValidationError`, and the program prints the first error message.

I use:

```python
datetime.fromisoformat("2226-05-08T12:00:00")
```

This gives a real `datetime` object. It also keeps `mypy` happy, because `mypy`
expects the argument type to match the model field type.

### How To Run

The subject requires Pydantic, but the submitted project does not include a virtual
environment.

Do not submit `.venv`.

Create and activate a local environment yourself:

```bash
cd /home/dev/projects/42/python_modules/python_module_09
python3 -m venv .venv
source .venv/bin/activate
pip install pydantic
```

Run the exercise:

```bash
python3 ex0/space_station.py
```

Expected behavior:

- the valid station is printed;
- then the program prints an expected validation error for `crew_size`.

You can also run type checking if `mypy` is installed:

```bash
mypy ex0/space_station.py
```

The virtual environment is only for local work. The file to submit for Exercise 0
is:

```text
ex0/space_station.py
```

### Think About Questions

#### How does Pydantic automatic type conversion work?

Pydantic looks at the type hints in the model.

If a value is compatible with the expected type, Pydantic can convert it.

Example:

```python
crew_size: int
```

If the input is `"6"`, Pydantic can convert it to integer `6`.

For a `datetime` field, Pydantic can parse a valid timestamp string and convert it
to a `datetime` object.

This happens at runtime when the model instance is created.

#### What happens when you pass a string timestamp to a datetime field?

If the string has a valid datetime format, Pydantic converts it to a `datetime`
object.

Example:

```python
last_maintenance="2226-05-08T12:00:00"
```

Pydantic can understand this ISO format and store it as a `datetime`.

If the string is not a valid date, Pydantic raises a `ValidationError`.

In my final code, I use `datetime.fromisoformat(...)` before passing the value.
This is not required by Pydantic, but it is useful for static type checking with
`mypy`.

### Tricky Evaluation Questions

#### Why do we use `BaseModel`?

Because `BaseModel` gives the class Pydantic validation behavior. Without it, the
class would be a normal Python class and `Field` rules would not validate data.

#### Why use `Field` instead of manual `if` checks?

`Field` keeps validation rules close to the data definition. It is shorter,
clearer, and Pydantic gives standard error messages.

#### What does `ge` mean?

`ge` means greater than or equal.

```python
Field(ge=1)
```

means the value must be at least 1.

#### What does `le` mean?

`le` means less than or equal.

```python
Field(le=20)
```

means the value must be at most 20.

#### Why is `notes` written as `str | None`?

Because the field is optional. It can contain text, or it can be missing and become
`None`.

#### Why does `notes` have `default=None`?

Without `default=None`, the field type allows `None`, but the field may still be
required during model creation.

With `default=None`, the field is truly optional.

#### Why does `last_maintenance` not use `Field`?

The subject only says it must be a `DateTime` field. There are no extra limits for
this field, so the `datetime` type hint is enough.

`Field` is useful when we need constraints like minimum length, maximum value, or a
default.

#### Why catch `ValidationError`?

Because this is the specific error Pydantic raises when validation fails.

Catching `ValidationError` is better than catching a generic `Exception`, because it
shows that this error is expected and related to validation.

#### Is `ValidationError` allowed?

Yes. It is part of Pydantic, and this module is about Pydantic. The subject asks us
to show the validation error message, so using `ValidationError` is appropriate.

#### Why not use `model_validator` in Exercise 0?

Exercise 0 only needs simple field validation. `Field` is enough.

`model_validator` is useful when a rule depends on multiple fields at the same
time. That appears in later exercises.

#### Why not submit `.venv`?

`.venv` is a local environment. It can be large and machine-specific.

The project submission should contain source files, not installed packages.

The evaluator can create their own environment and install Pydantic.

#### Why did `mypy` complain about a string for `datetime`?

Pydantic can convert a string to `datetime` at runtime, but `mypy` checks types
before running the program.

The field type is `datetime`, so `mypy` expects a real `datetime` object.

That is why the final code uses:

```python
datetime.fromisoformat("2226-05-08T12:00:00")
```

## Exercise 1 - Alien Contact Logs

### What To Do

Create the file:

```text
ex1/alien_contact.py
```

First, define a `ContactType` enum with four allowed contact types:

- `radio`;
- `visual`;
- `physical`;
- `telepathic`.

Then create an `AlienContact` Pydantic model with these fields:

- `contact_id`: string, 5 to 15 characters;
- `timestamp`: `datetime`;
- `location`: string, 3 to 100 characters;
- `contact_type`: `ContactType`;
- `signal_strength`: float, from 0.0 to 10.0;
- `duration_minutes`: integer, from 1 to 1440;
- `witness_count`: integer, from 1 to 100;
- `message_received`: optional string, maximum 500 characters;
- `is_verified`: boolean, default value `False`.

After the field validation, add custom model validation with:

```python
@model_validator(mode="after")
```

The custom rules are:

- contact ID must start with `"AC"`;
- physical contact reports must be verified;
- telepathic contact requires at least 3 witnesses;
- strong signals above 7.0 should include a received message.

### What This Exercise Teaches

This exercise teaches custom validation.

Exercise 0 only used simple field rules. Exercise 1 adds business rules that depend
on more than one field.

The needed theory is:

- `Enum`;
- Pydantic `BaseModel`;
- `Field`;
- optional fields;
- `datetime`;
- `ValidationError`;
- `@model_validator(mode="after")`;
- raising `ValueError` inside validators.

### How My Solution Is Made

My solution defines this enum:

```python
class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"
```

`Enum` means that the field can only use one of the allowed values. This prevents
invalid contact types like `"banana"` or `"unknown"`.

The model uses `Field` for simple constraints:

```python
contact_id: str = Field(min_length=5, max_length=15)
location: str = Field(min_length=3, max_length=100)
signal_strength: float = Field(ge=0.0, le=10.0)
duration_minutes: int = Field(ge=1, le=1440)
witness_count: int = Field(ge=1, le=100)
message_received: str | None = Field(default=None, max_length=500)
is_verified: bool = False
```

Then the model uses `@model_validator(mode="after")` for rules that need multiple
fields:

```python
@model_validator(mode="after")
def validate_contact_rules(self) -> "AlienContact":
    if not self.contact_id.startswith("AC"):
        raise ValueError('Contact ID must start with "AC"')

    if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
        raise ValueError("Physical contact reports must be verified")

    if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
        raise ValueError("Telepathic contact requires at least 3 witnesses")

    if self.signal_strength > 7.0 and not self.message_received:
        raise ValueError("Strong signals (> 7.0) should include received messages")

    return self
```

The `return self` line is important. In `mode="after"`, Pydantic expects the
validator to return the validated model instance.

### How To Run

Use the same local environment as Exercise 0.

If it does not exist yet:

```bash
cd /home/dev/projects/42/python_modules/python_module_09
python3 -m venv .venv
source .venv/bin/activate
pip install pydantic
```

Run the exercise:

```bash
python3 ex1/alien_contact.py
```

Expected behavior:

- the program prints a valid alien contact report;
- then it tries to create an invalid telepathic contact;
- Pydantic raises a validation error;
- the program prints the clear error message.

You can also run type checking:

```bash
mypy ex1/alien_contact.py
```

The virtual environment is only for local work. Do not submit `.venv`.

The file to submit for Exercise 1 is:

```text
ex1/alien_contact.py
```

### Advanced Tip

The subject says:

```text
The @model_validator decorator allows you to validate the entire model after all
fields have been validated. Remember to return self at the end of your validator
function.
```

This means that `model_validator` is used when a rule depends on the whole model,
not only one field.

Example:

```python
if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
    raise ValueError("Telepathic contact requires at least 3 witnesses")
```

This rule needs two fields:

- `contact_type`;
- `witness_count`.

That is why `Field` alone is not enough.

With `mode="after"`, Pydantic first validates all fields and then runs this method.
Inside the method, `self` is already a validated model object.

### Tricky Evaluation Questions

#### What is an enum?

An enum is a fixed list of allowed values.

In this exercise, `ContactType` makes sure that a contact type can only be
`radio`, `visual`, `physical`, or `telepathic`.

#### Why not use a simple `str` for `contact_type`?

Because a simple string would allow invalid values like `"wrong"` or `"banana"`.

An enum makes invalid contact types fail validation.

#### What is `@model_validator(mode="after")`?

It is a Pydantic decorator for validating the whole model after normal field
validation is complete.

It is useful for business rules that depend on several fields.

#### Do we call `validate_contact_rules()` manually?

No. Pydantic calls it automatically when an `AlienContact` object is created.

#### Why is `mode="after"` used here?

Because we want to work with a complete model where all fields already have proper
types.

For example, `self.contact_type` is already a `ContactType`, and
`self.timestamp` is already a `datetime`.

#### What does `startswith("AC")` do?

It checks whether a string begins with `"AC"`.

```python
"AC_2024_001".startswith("AC")
```

returns `True`.

```python
"XX_2024_001".startswith("AC")
```

returns `False`.

#### Why use `not self.contact_id.startswith("AC")`?

Because the rule says the ID must start with `"AC"`.

The condition means: if the ID does not start with `"AC"`, raise an error.

#### Why raise `ValueError` inside the validator?

Inside a Pydantic validator, `ValueError` is the standard way to say that custom
validation failed.

Pydantic catches this `ValueError` and wraps it into a `ValidationError`.

#### Why catch `ValidationError` outside?

Because from outside the model creation, Pydantic reports validation failures as
`ValidationError`.

The code inside the validator raises `ValueError`, but the code around
`AlienContact(...)` catches `ValidationError`.

#### Why does the error sometimes say `Value error, ...`?

For custom validators, Pydantic includes the original `ValueError` in the
validation error message.

The full message can look like this:

```text
Value error, Telepathic contact requires at least 3 witnesses
```

If we want only the original text, we can print:

```python
print(error.errors()[0]["ctx"]["error"])
```

#### Why do strong signals need a message?

This is a business rule from the subject.

In the lore, a strong signal is important enough that a message should be included.
In programming terms, this is a rule that depends on both `signal_strength` and
`message_received`.

#### What happens if several rules are invalid?

In this solution, the validator raises the first custom error it finds.

For example, if the ID is wrong, the validator stops there and does not continue to
the next custom rules.

#### What is the difference between `Field` validation and `model_validator`?

`Field` validates one field at a time.

Examples:

- string length;
- minimum number;
- maximum number.

`model_validator` validates relationships between fields.

Examples:

- physical contacts must be verified;
- telepathic contacts need at least 3 witnesses;
- strong signals need messages.

## Exercise 2 - Space Crew Management

### What To Do

Create the file:

```text
ex2/space_crew.py
```

First, define a `Rank` enum with five allowed crew ranks:

- `cadet`;
- `officer`;
- `lieutenant`;
- `captain`;
- `commander`.

Then create a `CrewMember` model with these fields:

- `member_id`: string, 3 to 10 characters;
- `name`: string, 2 to 50 characters;
- `rank`: `Rank`;
- `age`: integer, from 18 to 80;
- `specialization`: string, 3 to 30 characters;
- `years_experience`: integer, from 0 to 50;
- `is_active`: boolean, default value `True`.

Then create a `SpaceMission` model with these fields:

- `mission_id`: string, 5 to 15 characters;
- `mission_name`: string, 3 to 100 characters;
- `destination`: string, 3 to 50 characters;
- `launch_date`: `datetime`;
- `duration_days`: integer, from 1 to 3650;
- `crew`: list of `CrewMember`, from 1 to 12 members;
- `mission_status`: string, default value `"planned"`;
- `budget_millions`: float, from 1.0 to 10000.0.

After that, add custom mission validation:

- mission ID must start with `"M"`;
- mission must have at least one Commander or Captain;
- long missions above 365 days need 50% experienced crew;
- all crew members must be active.

### What This Exercise Teaches

This exercise teaches nested Pydantic models.

Exercise 0 validates simple fields. Exercise 1 validates relationships between
fields. Exercise 2 validates a model that contains other models.

The needed theory is:

- `Enum`;
- `BaseModel`;
- `Field`;
- list type hints;
- nested Pydantic models;
- `datetime`;
- `@model_validator(mode="after")`;
- `ValidationError`;
- `any`;
- `sum` over boolean values.

### How My Solution Is Made

My solution defines this enum:

```python
class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"
```

Then it defines `CrewMember`:

```python
class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True
```

Then it defines `SpaceMission`:

```python
class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)
```

The most important field is:

```python
crew: list[CrewMember] = Field(min_length=1, max_length=12)
```

This means that `crew` must be a list, and every item in the list must be a valid
`CrewMember`.

The custom validator checks mission-level rules:

```python
@model_validator(mode="after")
def validate_mission(self) -> "SpaceMission":
    if not self.mission_id.startswith("M"):
        raise ValueError("Mission ID must start with 'M'")

    if not any(
        member.rank in {Rank.COMMANDER, Rank.CAPTAIN}
        for member in self.crew
    ):
        raise ValueError("Mission must have at least one Commander or Captain")

    if self.duration_days > 365:
        experienced_crew = sum(
            member.years_experience >= 5
            for member in self.crew
        )
        if experienced_crew < len(self.crew) / 2:
            raise ValueError(
                "Long missions (> 365 days) need "
                "50% experienced crew (5+ years)"
            )

    inactive_members = [
        member
        for member in self.crew
        if not member.is_active
    ]

    if inactive_members:
        raise ValueError("All crew members must be active")

    return self
```

The valid demo mission has one Commander and enough experienced crew. The invalid
demo mission has only a Lieutenant and an Officer, so it fails with:

```text
Mission must have at least one Commander or Captain
```

### How To Run

Use the same local environment as the previous exercises.

If it does not exist yet:

```bash
cd /home/dev/projects/42/python_modules/python_module_09
python3 -m venv .venv
source .venv/bin/activate
pip install pydantic
```

Run the exercise:

```bash
python3 ex2/space_crew.py
```

Expected behavior:

- the program prints a valid mission;
- it prints all crew members;
- then it tries to create an invalid mission;
- Pydantic raises a validation error;
- the program prints the clear error message.

You can also run type checking:

```bash
mypy ex2/space_crew.py
```

The virtual environment is only for local work. Do not submit `.venv`.

The file to submit for Exercise 2 is:

```text
ex2/space_crew.py
```

### Think About Questions

#### How does Pydantic handle validation of nested models?

Pydantic validates nested models recursively.

In this exercise, `SpaceMission` has this field:

```python
crew: list[CrewMember]
```

So Pydantic validates the `crew` list first, then validates every item in the list
as a `CrewMember`.

It checks each crew member's fields:

- `member_id`;
- `name`;
- `rank`;
- `age`;
- `specialization`;
- `years_experience`;
- `is_active`.

#### What happens when a CrewMember fails validation within a SpaceMission?

If one crew member is invalid, the whole `SpaceMission` validation fails.

Pydantic raises a `ValidationError`, and the error location points to the nested
field.

For example, if a crew member has:

```python
age=5
```

the error can point to:

```text
crew.0.age
```

This means: in the `crew` list, item `0`, field `age` is invalid.

Important detail: if we create `CrewMember(...)` separately before passing it to
`SpaceMission`, the error can happen earlier during `CrewMember` creation.

If we pass crew members as dictionaries, Pydantic validates them inside
`SpaceMission`.

Example:

```python
crew=[
    {
        "member_id": "CM001",
        "name": "Test Pilot",
        "rank": "officer",
        "age": 5,
        "specialization": "Navigation",
        "years_experience": 2,
    }
]
```

Here Pydantic will try to build a `CrewMember` from the dictionary. Since `age=5`
is invalid, `SpaceMission` validation fails.

Short evaluation answer:

```text
Pydantic validates nested models recursively. In SpaceMission, crew is a list of
CrewMember, so Pydantic checks the list size and then validates each item as a
CrewMember. If one crew member is invalid, the whole SpaceMission validation fails
and Pydantic raises a ValidationError. The error location points to the nested
field, for example crew.0.age.
```

### Tricky Evaluation Questions

#### Why use `list[CrewMember]`?

Because a mission has multiple crew members, and every item should follow the
`CrewMember` model.

This gives validation for both the list itself and the objects inside it.

#### What does `Field(min_length=1, max_length=12)` mean for a list?

It means the list must contain at least 1 item and at most 12 items.

For `crew`, this matches the subject requirement: 1 to 12 crew members.

#### Why does the mission need a Commander or Captain?

This is a mission safety rule from the subject.

In code, it is checked with:

```python
any(
    member.rank in {Rank.COMMANDER, Rank.CAPTAIN}
    for member in self.crew
)
```

`any` returns `True` if at least one crew member has one of these ranks.

#### How does the long mission experience rule work?

If:

```python
self.duration_days > 365
```

then the mission is long.

The code counts experienced crew members:

```python
experienced_crew = sum(
    member.years_experience >= 5
    for member in self.crew
)
```

In Python, `True` counts as `1` and `False` counts as `0`, so `sum` counts how many
crew members have at least 5 years of experience.

Then the code checks whether this count is at least half of the crew:

```python
experienced_crew < len(self.crew) / 2
```

If fewer than 50% are experienced, validation fails.

#### Does 50% mean exactly half or more?

The mission is valid when at least half of the crew has 5+ years of experience.

For 4 crew members, at least 2 must be experienced.

For 3 crew members, at least 2 are needed, because 1 is less than 1.5.

#### Why check `is_active` in the mission validator?

The rule depends on all crew members, not one field of the mission.

The validator scans the crew list:

```python
inactive_members = [
    member
    for member in self.crew
    if not member.is_active
]
```

If the list is not empty, at least one member is inactive, so validation fails.

#### Why does the invalid demo mission use valid CrewMember fields?

Because the demo is meant to show the mission-level rule:

```text
Mission must have at least one Commander or Captain
```

If a crew member had an invalid age or invalid name, Pydantic would fail earlier on
the nested `CrewMember` validation. That would not demonstrate the intended mission
rule.

#### Why use `datetime.fromisoformat()` for dates?

Pydantic can parse datetime strings at runtime, but `mypy` expects a real
`datetime` object when the field type is `datetime`.

Using `datetime.fromisoformat()` keeps the code clear for both Pydantic and static
type checking.

#### What happens if several mission rules are invalid?

This solution raises the first custom validation error it finds.

For example, if the mission ID is wrong, the validator raises that error first and
does not continue to later custom rules.

#### Why catch `ValidationError`?

Pydantic reports validation failures as `ValidationError`.

Inside custom validators we raise `ValueError`, and Pydantic wraps it into a
`ValidationError`.

The demo catches `ValidationError` to print a readable message.
