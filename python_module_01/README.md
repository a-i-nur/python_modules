# Python Module 01 - Defense Prep Guide

This file is made from:
- subject `p01.pdf`
- your current code in `python_module_01/ex0..ex6`

Use it to prepare for school 42 evaluation.

---

## ENGLISH VERSION (Simple English)

## 1. General Project Requirements

You must have:
- Python `3.10+`
- One file per exercise:
- `ex0/ft_garden_intro.py`
- `ex1/ft_garden_data.py`
- `ex2/ft_plant_growth.py`
- `ex3/ft_plant_factory.py`
- `ex4/ft_garden_security.py`
- `ex5/ft_plant_types.py`
- `ex6/ft_garden_analytics.py`
- Clean naming:
- classes: `PascalCase`
- functions/variables: `snake_case`
- Type hints in all functions and methods
- `flake8` style compliance
- Program must run without runtime errors
- Use classes from Exercise 1 and later

Quick mental model:

```text
ex0 -> entry point (__main__)
ex1 -> class as data blueprint
ex2 -> class behavior (methods that change state)
ex3 -> better object creation pattern
ex4 -> encapsulation and validation
ex5 -> inheritance (family of classes)
ex6 -> bigger architecture (nested helper + class/static methods)
```

## 2. What You Should NOT Do

Do not:
- break file names or folder names from subject
- forget type hints on methods/functions
- break `flake8` formatting
- use random global helper functions in ex6 (subject asks good structure)
- directly modify protected data in ex4 (`_height`, `_age`) from outside
- duplicate common code when inheritance is better (ex5)
- create code that crashes in demo run

Also important:
- Input validation is not required unless subject asks it
- In this module, validation is explicitly needed in ex4

---

## 3. Exercise by Exercise (What + How in Your Code)

## ex0 - `ft_garden_intro.py`

Goal from subject:
- Show a first program
- Use `if __name__ == "__main__":`
- Store simple plant data in variables
- Print it

How your code implements it:
- Function `ft_garden_intro()` creates:
- `plant_name`
- `plant_height`
- `plant_age`
- Prints all values
- Uses main guard:

```python
if __name__ == "__main__":
    ft_garden_intro()
```

Python theory here:
- `__name__` is `"__main__"` only when file is run directly
- main guard stops test/demo code from auto-running on import

Syntax used:

```python
def ft_garden_intro() -> None:
    ...
```

Metaphor:
- Main guard is like a gate: open only when this file is the main road.

Possible evaluation Q/A:
- Q: Why use `if __name__ == "__main__"`?
- A: To run demo code only when this file is executed directly, not imported.

---

## ex1 - `ft_garden_data.py`

Goal from subject:
- Manage at least 3 plants
- Create a `Plant` class as a blueprint
- Show plant data in organized way

How your code implements it:
- `Plant` class has:
- `name`, `height`, `days`
- `print_info()` method
- In `ft_garden_data()` you create `Rose`, `Sunflower`, `Cactus`
- Print registry header and plant lines

Python theory here:
- Class = blueprint
- Object/instance = real plant created from blueprint
- `__init__` is constructor (object setup)

Syntax used:

```python
class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
```

Metaphor:
- Class is a cookie mold, objects are cookies made from it.

Possible evaluation Q/A:
- Q: Why class and not 3 separate dicts?
- A: Class gives one clear structure and reusable behavior for many plants.

---

## ex2 - `ft_plant_growth.py`

Goal from subject:
- Reuse `Plant` class idea
- Add behaviors: `grow()`, `age()`, `get_info()`
- Simulate one week for multiple plants

How your code implements it:
- `grow()` adds `+1` to height
- `age()` adds `+1` day
- `get_info()` prints current state
- `ft_plant_growth()` uses list of 3 plants
- Nested loops:
- outer loop = 6 updates (Day 1 to Day 7)
- inner loop = apply updates to each plant

Structure:

```text
plants = [p1, p2, p3]
Day 1: print all
repeat 6 times:
  for each plant:
    grow
    age
Day 7: print all
```

Python theory here:
- Methods are functions inside a class
- `self` means current object
- Loop over list of objects to avoid repeated code

Possible evaluation Q/A:
- Q: Why nested loops?
- A: First loop is days, second loop updates each plant every day.

---

## ex3 - `ft_plant_factory.py`

Goal from subject:
- Create plants with initial values at construction
- Create at least 5 plants
- Show all and total count
- Make creation process clean

How your code implements it:
- `Plant.__init__` receives all initial values
- class variable `_total_plants` counts created objects
- source list with tuples holds start data
- loop creates objects with unpacking `Plant(*plant)`
- `print_total_plants()` prints counter

Structure:

```text
tuple data list -> loop -> Plant(*data) -> print each
class counter -> print total
```

Python theory here:
- Class variable is shared by all objects
- Constructor initializes object state
- Star-unpacking `*` passes tuple values as arguments

Possible evaluation Q/A:
- Q: Why keep `_total_plants` in class, not in function?
- A: It belongs to the Plant type globally, not to one local function run.

---

## ex4 - `ft_garden_security.py`

Goal from subject:
- Protect data from invalid updates
- Add setters/getters:
- `set_height`, `set_age`
- `get_height`, `get_age`
- Reject negative values and print error messages

How your code implements it:
- Class `SecurePlant`
- Internal fields: `_height`, `_age`
- Constructor calls setters, so even initial values are validated
- Setters reject negatives and keep old valid state
- Getter methods return safe values

Structure:

```text
outside code -> setter -> validation -> save or reject
outside code -> getter -> read safe value
```

Python theory here:
- Encapsulation: hide direct data writes, expose controlled methods
- Single underscore `_x` is Python convention: internal/protected field

Possible evaluation Q/A:
- Q: Why call setters inside `__init__`?
- A: So initial values and future updates follow same validation rules.

---

## ex5 - `ft_plant_types.py`

Goal from subject:
- Base class `Plant`
- Specialized classes:
- `Flower`
- `Tree`
- `Vegetable`
- Use inheritance and `super().__init__()`
- At least 2 objects of each type
- Avoid duplicated common code

How your code implements it:
- `Plant` stores common fields (`name`, `height`, `age`)
- `Flower` adds `color` + `bloom()`
- `Tree` adds `trunk_diameter` + `produce_shade()`
- `Vegetable` adds `harvest_season`, `nutritional_value`
- All child constructors call `super().__init__(...)`
- You create 6 objects total (2 per type)

Family tree:

```text
Plant
├── Flower
├── Tree
└── Vegetable
```

Python theory here:
- Inheritance lets child class reuse parent fields/methods
- `super()` calls parent behavior and prevents duplication
- Polymorphism style usage: one loop calls `plant.print_info()` for mixed types

Possible evaluation Q/A:
- Q: Why use `super()`?
- A: Parent setup code is reused, so child classes stay shorter and cleaner.

---

## ex6 - `ft_garden_analytics.py`

Goal from subject:
- Build bigger system architecture
- `GardenManager` handles multiple gardens
- Nested helper `GardenStats` computes stats
- Inheritance chain:
- `Plant -> FloweringPlant -> PrizeFlower`
- Use:
- instance methods
- class method (`create_garden_network`)
- static method (`is_valid_height`)

How your code implements it:
- `GardenManager.gardens` stores per-owner data:
- plant list
- stats dict
- `add_garden`, `add_plant`, `help_plants_grow`, `report`
- `GardenStats` nested class calculates:
- `plants_added`
- `total_growth`
- `type_breakdown`
- `garden_score`
- Demo creates two gardens (`Alice`, `Bob`) and compares scores

Architecture view:

```text
GardenManager
├── gardens[owner]
│   ├── plants: [Plant | FloweringPlant | PrizeFlower]
│   └── stats: {plants_added, total_growth}
└── GardenStats (nested helper for calculations)
```

Method-type theory:
- Instance method: needs object data (`self`)
- Class method: works with class (`cls`) and can create objects
- Static method: utility function placed in class namespace, no `self/cls`

Syntax examples:

```python
@classmethod
def create_garden_network(cls) -> "GardenManager":
    return cls()

@staticmethod
def is_valid_height(height: int) -> bool:
    return isinstance(height, int) and height >= 0
```

Possible evaluation Q/A:
- Q: Why nest `GardenStats` inside `GardenManager`?
- A: Stats are part of manager domain, so nesting keeps architecture organized.

---

## Fast Defense Checklist (English)

Before evaluation:
- run all files with `python3`
- run `flake8`
- confirm all functions/methods have type hints
- be ready to explain:
- `__main__` guard
- class vs object
- `self`, `__init__`
- encapsulation in ex4
- inheritance and `super()` in ex5
- instance/class/static methods in ex6

---

## РУССКАЯ ВЕРСИЯ

## 1. Общие требования проекта

Что обязательно должно быть:
- Python `3.10+`
- Один файл на упражнение:
- `ex0/ft_garden_intro.py`
- `ex1/ft_garden_data.py`
- `ex2/ft_plant_growth.py`
- `ex3/ft_plant_factory.py`
- `ex4/ft_garden_security.py`
- `ex5/ft_plant_types.py`
- `ex6/ft_garden_analytics.py`
- Чистые названия:
- классы: `PascalCase`
- функции/переменные: `snake_case`
- Type hints у всех функций и методов
- Соответствие `flake8`
- Программы должны запускаться без runtime-ошибок
- Начиная с Exercise 1 использовать классы

Быстрая логика роста модуля:

```text
ex0 -> точка входа (__main__)
ex1 -> класс как шаблон данных
ex2 -> поведение класса (изменение состояния)
ex3 -> более удобное создание объектов
ex4 -> инкапсуляция и валидация
ex5 -> наследование (семейство классов)
ex6 -> архитектура системы (nested helper + class/static методы)
```

## 2. Что нельзя делать

Нельзя:
- ломать имена файлов/папок из сабжекта
- забывать type hints у функций/методов
- нарушать `flake8`
- в ex6 разносить логику случайными глобальными функциями
- в ex4 менять `_height` и `_age` напрямую снаружи
- дублировать общий код, где нужен inheritance (ex5)
- оставлять код, который падает при запуске

Важно:
- Валидация инпута не нужна, если это не просит сабжект
- В этом модуле явная валидация нужна в ex4

---

## 3. По каждому упражнению (что нужно + как у тебя сделано)

## ex0 - `ft_garden_intro.py`

Что требует сабжект:
- Первый запускаемый скрипт
- Использовать `if __name__ == "__main__":`
- Сохранить данные растения в переменные
- Вывести через `print`

Как сделано у тебя:
- `ft_garden_intro()` создает:
- `plant_name`
- `plant_height`
- `plant_age`
- Печатает все значения
- Есть main guard:

```python
if __name__ == "__main__":
    ft_garden_intro()
```

Теория Python:
- `__name__ == "__main__"` только при прямом запуске файла
- При `import` блок не выполняется

Метафора:
- Main guard как шлагбаум: откроется только для "главной дороги".

Возможный вопрос на проверке:
- В: Зачем `if __name__ == "__main__"`?
- О: Чтобы демо-код запускался только при прямом запуске файла, а не при импорте.

---

## ex1 - `ft_garden_data.py`

Что требует сабжект:
- Минимум 3 растения
- Класс `Plant` как шаблон
- Организованный вывод данных

Как сделано у тебя:
- Класс `Plant` хранит:
- `name`, `height`, `days`
- Есть метод `print_info()`
- В `ft_garden_data()` создаются `Rose`, `Sunflower`, `Cactus`
- Печатается реестр

Теория Python:
- Class = шаблон
- Object (instance) = конкретный объект по шаблону
- `__init__` = конструктор

Метафора:
- Класс - это формочка, объекты - печеньки из нее.

Возможный вопрос:
- В: Почему класс, а не 3 отдельные dict?
- О: Класс задает единую структуру и позволяет переиспользовать поведение.

---

## ex2 - `ft_plant_growth.py`

Что требует сабжект:
- Поведение растения: `grow()`, `age()`, `get_info()`
- Симуляция недели для нескольких растений

Как сделано у тебя:
- `grow()` делает `+1` к высоте
- `age()` делает `+1` к дням
- `get_info()` печатает состояние
- В `ft_plant_growth()` список из 3 растений
- Вложенные циклы:
- внешний = дни
- внутренний = обновление каждого растения

Схема:

```text
plants = [p1, p2, p3]
Day 1: print all
repeat 6 times:
  for each plant:
    grow
    age
Day 7: print all
```

Теория Python:
- Метод - функция внутри класса
- `self` - текущий объект
- Список объектов + цикл убирает дублирование

Возможный вопрос:
- В: Зачем вложенные циклы?
- О: Первый цикл это дни, второй - обновление каждого растения в каждый день.

---

## ex3 - `ft_plant_factory.py`

Что требует сабжект:
- Создание растений с начальными значениями
- Минимум 5 растений
- Показать созданные растения и итоговое количество
- Сделать процесс создания удобным

Как сделано у тебя:
- `__init__` принимает стартовые поля
- `_total_plants` считает все созданные объекты
- Список кортежей хранит исходные данные
- В цикле создаются объекты через `Plant(*plant)`
- `print_total_plants()` печатает счетчик

Схема:

```text
список кортежей -> цикл -> Plant(*данные) -> печать
общий счетчик класса -> итог
```

Теория Python:
- Class variable общая для всех экземпляров
- Конструктор инициализирует объект
- `*` распаковывает кортеж в аргументы

Возможный вопрос:
- В: Почему `_total_plants` в классе, а не в функции?
- О: Это общее состояние типа `Plant`, а не одной функции.

---

## ex4 - `ft_garden_security.py`

Что требует сабжект:
- Защита от некорректных данных
- Методы:
- `set_height`, `set_age`
- `get_height`, `get_age`
- Запрет отрицательных значений + сообщения об ошибке

Как сделано у тебя:
- Класс `SecurePlant`
- Внутренние поля `_height`, `_age`
- Конструктор вызывает сеттеры (валидация с самого начала)
- Сеттеры отклоняют отрицательные значения и не ломают текущее состояние
- Геттеры отдают безопасные данные

Схема:

```text
внешний код -> setter -> проверка -> сохранить / отклонить
внешний код -> getter -> чтение безопасного значения
```

Теория Python:
- Инкапсуляция: контроль доступа через методы
- `_field` - соглашение "внутреннее поле"

Возможный вопрос:
- В: Зачем в `__init__` вызывать сеттеры, а не присвоить напрямую?
- О: Чтобы начальные значения проходили те же правила валидации.

---

## ex5 - `ft_plant_types.py`

Что требует сабжект:
- Базовый `Plant`
- Специализации:
- `Flower`
- `Tree`
- `Vegetable`
- Наследование + `super().__init__()`
- Минимум 2 объекта каждого типа
- Не дублировать общий код

Как сделано у тебя:
- `Plant` хранит общие поля
- `Flower` добавляет `color` и `bloom()`
- `Tree` добавляет `trunk_diameter` и `produce_shade()`
- `Vegetable` добавляет `harvest_season`, `nutritional_value`
- Во всех дочерних конструкторах есть `super().__init__(...)`
- Создано 6 объектов (по 2 каждого типа)

Дерево классов:

```text
Plant
├── Flower
├── Tree
└── Vegetable
```

Теория Python:
- Inheritance переиспользует логику родителя
- `super()` вызывает родительскую инициализацию
- Полиморфный стиль: один цикл вызывает `print_info()` у разных типов

Возможный вопрос:
- В: Зачем `super()`?
- О: Чтобы переиспользовать код родителя и не дублировать общие поля.

---

## ex6 - `ft_garden_analytics.py`

Что требует сабжект:
- Большая архитектура
- `GardenManager` для многих садов
- Вложенный помощник `GardenStats`
- Цепочка наследования:
- `Plant -> FloweringPlant -> PrizeFlower`
- Показать:
- instance methods
- class method (`create_garden_network`)
- static method (`is_valid_height`)

Как сделано у тебя:
- `GardenManager.gardens` хранит данные по владельцам:
- список растений
- словарь статистики
- Методы: `add_garden`, `add_plant`, `help_plants_grow`, `report`
- Вложенный `GardenStats` считает:
- `plants_added`
- `total_growth`
- `type_breakdown`
- `garden_score`
- В демо создаются два сада (`Alice`, `Bob`) и сравниваются очки

Схема архитектуры:

```text
GardenManager
├── gardens[owner]
│   ├── plants: [Plant | FloweringPlant | PrizeFlower]
│   └── stats: {plants_added, total_growth}
└── GardenStats (вложенный helper для расчетов)
```

Теория типов методов:
- Instance method: нужен `self`, работает с данными объекта
- Class method: нужен `cls`, работает на уровне класса (например, фабрика)
- Static method: утилита в пространстве имен класса, без `self/cls`

Синтаксис:

```python
@classmethod
def create_garden_network(cls) -> "GardenManager":
    return cls()

@staticmethod
def is_valid_height(height: int) -> bool:
    return isinstance(height, int) and height >= 0
```

Возможный вопрос:
- В: Зачем `GardenStats` вложен в `GardenManager`?
- О: Это логика аналитики именно менеджера, поэтому так структура чище.

---

## Быстрый чеклист перед защитой

Перед сдачей:
- запусти каждый файл через `python3`
- прогони `flake8`
- проверь type hints у всех функций/методов
- будь готов объяснить:
- `__main__` guard
- class vs object
- `self`, `__init__`
- инкапсуляцию в ex4
- inheritance и `super()` в ex5
- instance/class/static methods в ex6
