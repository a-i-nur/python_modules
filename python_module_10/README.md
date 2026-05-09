# Python Module 10 - FuncMage

## 1. О чем модуль и чему он учит

Этот модуль про функциональное программирование в Python.

Главная идея: функция в Python является объектом первого класса. Это значит, что функцию можно:

- передавать как аргумент в другую функцию;
- возвращать из функции;
- сохранять в переменную;
- использовать для обработки коллекций данных.

Модуль постепенно учит:

- писать короткие анонимные функции через `lambda`;
- использовать `map`, `filter`, `sorted`, `min`, `max`;
- создавать функции, которые принимают или возвращают другие функции;
- понимать замыкания и область видимости;
- использовать `functools`;
- писать декораторы.

## 2. Теория, которую надо знать

Функция как объект первого класса:

```python
def spell(power: int) -> int:
    return power * 2


boost = spell
print(boost(10))
```

`lambda` - это анонимная функция:

```python
lambda x: x * 2
```

Она похожа на:

```python
def double(x):
    return x * 2
```

Но `lambda` используется для коротких одноразовых операций.

`sorted(iterable, key=...)` сортирует коллекцию. `key` говорит, по какому значению сортировать:

```python
sorted(items, key=lambda item: item["power"])
```

`filter(function, iterable)` оставляет только элементы, для которых функция вернула `True`:

```python
filter(lambda mage: mage["power"] >= 70, mages)
```

`map(function, iterable)` применяет функцию к каждому элементу:

```python
map(lambda spell: f"* {spell} *", spells)
```

`min` и `max` тоже могут принимать `key`:

```python
max(mages, key=lambda mage: mage["power"])
```

## 3. Лор и связь с теорией

По лору модуля мы изучаем магию функционального программирования.

Маги, заклинания и артефакты - это просто данные:

- маги представлены словарями;
- артефакты представлены словарями;
- заклинания представлены строками.

Функции - это "магические действия" над этими данными:

- сортировка артефактов по силе;
- фильтрация магов;
- преобразование названий заклинаний;
- подсчет статистики.

Лор помогает запомнить теорию: вместо обычных списков чисел мы работаем с игровыми объектами, но технически это те же самые словари, списки и функции.

# Exercise 0 - Lambda Sanctum

## 1. Что надо сделать, чему учит и какая теория нужна

Нужно создать файл:

```text
ex0/lambda_spells.py
```

В нем нужно реализовать 4 функции:

```python
def artifact_sorter(artifacts: list[dict]) -> list[dict]
def power_filter(mages: list[dict], min_power: int) -> list[dict]
def spell_transformer(spells: list[str]) -> list[str]
def mage_stats(mages: list[dict]) -> dict
```

Упражнение учит использовать `lambda` внутри стандартных функций Python:

- `sorted` для сортировки;
- `filter` для фильтрации;
- `map` для преобразования;
- `max` и `min` для поиска по ключу.

Главная теория:

- синтаксис `lambda аргументы: выражение`;
- отличие `map` от `filter`;
- параметр `key` в `sorted`, `min`, `max`;
- почему `map` и `filter` оборачиваются в `list`.

## 2. Как сделано у меня

Файл: `ex0/lambda_spells.py`

`artifact_sorter` сортирует артефакты по полю `"power"` по убыванию:

```python
return sorted(
    artifacts, key=lambda artifact: artifact["power"], reverse=True
)
```

`power_filter` оставляет только магов с силой не меньше `min_power`:

```python
return list(filter(lambda mage: mage["power"] >= min_power, mages))
```

`spell_transformer` добавляет к каждому заклинанию префикс и суффикс со звездочками:

```python
return list(map(lambda spell: f"* {spell} *", spells))
```

`mage_stats` возвращает статистику:

```python
return {
    "max_power": max(mages, key=lambda mage: mage["power"])["power"],
    "min_power": min(mages, key=lambda mage: mage["power"])["power"],
    "avg_power": round(
        sum(map(lambda mage: mage["power"], mages)) / len(mages),
        2,
    ),
}
```

Важно: в `max` и `min` сначала находится весь словарь мага, а потом из него берется поле `"power"`.

## 3. Как запустить и продемонстрировать

Перейти в папку модуля:

```bash
cd /home/dev/projects/42/python_modules/python_module_10
```

Запустить:

```bash
python3 ex0/lambda_spells.py
```

Ожидаемый пример вывода:

```text
Testing artifact sorter...
Fire Staff (92 power) comes before Ice Wand (67 power)

Testing power filter...
[{'name': 'Alex', 'power': 80, 'element': 'fire'}, {'name': 'Riley', 'power': 95, 'element': 'lightning'}]

Testing spell transformer...
* fireball * * heal * * shield *

Testing mage stats...
{'max_power': 95, 'min_power': 55, 'avg_power': 76.67}
```

Для запуска не нужно создавать виртуальное окружение и не нужно ставить зависимости через `pip`.
В сабже запрещены внешние библиотеки, поэтому используются только встроенные функции Python.

Если проверяющий запускает не из папки `python_module_10`, можно указать полный путь к файлу:

```bash
python3 /home/dev/projects/42/python_modules/python_module_10/ex0/lambda_spells.py
```

## 4. Ответы на вопросы по ex0 из сабжа

### How do lambda expressions make code more concise?

`lambda` позволяет написать маленькую функцию прямо в месте использования.
Например, вместо отдельной функции:

```python
def get_power(mage):
    return mage["power"]
```

можно написать:

```python
lambda mage: mage["power"]
```

Это короче и удобно, когда функция нужна только один раз.

### When should you use lambda vs. regular function definitions?

`lambda` стоит использовать для коротких простых операций:

- получить поле из словаря;
- проверить условие;
- немного изменить строку или число.

Обычный `def` лучше использовать, если:

- логика длинная;
- нужны несколько строк кода;
- функция будет использоваться много раз;
- нужно хорошее имя и документация;
- код станет понятнее с обычной функцией.

## 5. Хитрые вопросы на evaluation

### Что такое lambda?

`lambda` - это анонимная функция, то есть функция без имени. Она имеет синтаксис:

```python
lambda аргументы: выражение
```

### Может ли lambda содержать несколько строк?

Нет. В `lambda` может быть только одно выражение после `:`.

### Почему в `filter` и `map` используется `list(...)`?

Потому что `map` и `filter` возвращают итераторы, а по заданию нужно вернуть обычный список.

### Чем `map` отличается от `filter`?

`map` преобразует каждый элемент и сохраняет количество элементов.

`filter` проверяет каждый элемент и оставляет только подходящие элементы.

### Что делает `key` в `sorted`?

`key` говорит, какое значение взять у каждого элемента для сортировки.

В этом решении:

```python
key=lambda artifact: artifact["power"]
```

сортировка идет по силе артефакта.

### Почему `reverse=True`?

Потому что по заданию нужно сортировать по убыванию: от большей силы к меньшей.

### Что вернет `max(mages, key=lambda mage: mage["power"])`?

Он вернет не число, а весь словарь мага с максимальной силой.

Поэтому в коде после `max(...)` используется `["power"]`, чтобы получить само число:

```python
max(mages, key=lambda mage: mage["power"])["power"]
```

### Почему среднее округляется через `round(..., 2)`?

Потому что сабж требует округлить среднюю силу до 2 знаков после запятой.

### Есть ли здесь глобальные переменные?

Нет. Данные для демонстрации находятся внутри `main()`, поэтому они не являются глобальными переменными.

### Почему используется `if __name__ == "__main__"`?

Чтобы демонстрационный код запускался только при прямом запуске файла.
Если файл импортируют для тестов, функции можно использовать без автоматического запуска `main()`.

### Что будет, если передать пустой список в `mage_stats`?

Будет ошибка, потому что `max`, `min` и деление на `len(mages)` не работают для пустого списка.
В сабже для ex0 не указана обработка пустого списка, поэтому решение ориентировано на корректные входные данные.

### Нарушает ли `main()` задание?

Нет. Сабж просит создать функции и показывает пример запуска файла.
`main()` нужен только для демонстрации работы функций.

# Exercise 1 - Higher Realm

## 1. Что надо сделать, чему учит и какая теория нужна

Нужно создать файл:

```text
ex1/higher_magic.py
```

В нем нужно реализовать 4 функции:

```python
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable
def power_amplifier(base_spell: Callable, multiplier: int) -> Callable
def conditional_caster(condition: Callable, spell: Callable) -> Callable
def spell_sequence(spells: list[Callable]) -> Callable
```

Упражнение учит функциям высшего порядка.

Функция высшего порядка - это функция, которая:

- принимает другую функцию как аргумент;
- возвращает новую функцию;
- или делает и то, и другое.

Главная теория:

- функции в Python являются объектами первого класса;
- функцию можно передать как аргумент;
- функцию можно вернуть из другой функции;
- внутренняя функция может использовать переменные внешней функции;
- `Callable` используется как type hint для вызываемых объектов.

## 2. Как сделано у меня

Файл: `ex1/higher_magic.py`

Импорт:

```python
from collections.abc import Callable
```

`spell_combiner` принимает два заклинания и возвращает новую функцию `combined_spell`.
Эта новая функция вызывает оба заклинания с одинаковыми аргументами и возвращает кортеж:

```python
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple:
        return spell1(target, power), spell2(target, power)

    return combined_spell
```

`power_amplifier` возвращает новую функцию, которая умножает `power` перед вызовом базового заклинания:

```python
def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell
```

`conditional_caster` сначала проверяет условие. Если условие истинно, заклинание выполняется. Иначе возвращается `"Spell fizzled"`:

```python
def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return conditional_spell
```

`spell_sequence` принимает список заклинаний и возвращает функцию, которая вызывает все заклинания по очереди:

```python
def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence_spell
```

Важно: по сабжу `spell_sequence` должна вернуть список результатов, а не одну строку.

## 3. Как запустить и продемонстрировать

Перейти в папку модуля:

```bash
cd /home/dev/projects/42/python_modules/python_module_10
```

Запустить:

```bash
python3 ex1/higher_magic.py
```

Пример вывода моего файла:

```text
Testing spell combiner...
Combined spell result: ('Fireball hits Dragon with 10 power', 'Heal restores Dragon for 10 HP')

Testing power amplifier...
Original: 10, Amplified: Fireball hits Dragon with 30 power

Testing conditional caster...
Fireball hits Dragon with 15 power
Spell fizzled

Testing spell sequence...
['Fireball hits Dragon with 10 power', 'Heal restores Dragon for 10 HP']
```

Короткий пример в сабже может выглядеть иначе:

```text
Testing spell combiner...
Combined spell result: Fireball hits Dragon, Heals Dragon

Testing power amplifier...
Original: 10, Amplified: 30
```

Это не ошибка, потому что сабж требует сохранить основную структуру вывода, но разрешает кастомизировать сообщения.
Главное - поведение функций:

- `spell_combiner` возвращает функцию, которая возвращает tuple из двух результатов;
- `power_amplifier` возвращает функцию, которая вызывает базовое заклинание с умноженной силой;
- `conditional_caster` возвращает `"Spell fizzled"` при провале условия;
- `spell_sequence` возвращает список результатов.

Для запуска не нужно создавать виртуальное окружение и не нужно ставить зависимости через `pip`.
Используется только стандартная библиотека Python.

## 4. Ответы на вопросы по ex1 из сабжа

### How do higher-order functions enable code reuse and composition?

Функции высшего порядка позволяют переиспользовать код, потому что общая логика пишется один раз, а конкретное поведение передается как функция.

Например, `power_amplifier` не знает, какое именно заклинание ему передали.
Он просто усиливает любое заклинание:

```python
mega_fireball = power_amplifier(fireball, 3)
mega_heal = power_amplifier(heal, 3)
```

Композиция означает, что маленькие функции можно объединять в более сложное поведение.
Например, `spell_combiner` объединяет два заклинания, а `spell_sequence` строит цепочку заклинаний.

### What makes functions "first-class citizens" in Python?

Функции являются объектами первого класса, потому что с ними можно работать как с обычными значениями.

Функцию можно:

- сохранить в переменную;
- передать как аргумент;
- вернуть из другой функции;
- положить в список или словарь.

Пример:

```python
spells = [fireball, heal]
sequence = spell_sequence(spells)
```

Здесь функции `fireball` и `heal` лежат в списке как обычные объекты.

### From which package is it recommended to use Callable?

Рекомендуется использовать:

```python
from collections.abc import Callable
```

В старом коде можно встретить:

```python
from typing import Callable
```

Но в этом сабже прямо сказано использовать `Callable` из `collections.abc`.

### What is the purpose of callable()?

`callable()` проверяет, можно ли объект вызвать как функцию.

Пример:

```python
callable(fireball)
```

вернет:

```python
True
```

А:

```python
callable(42)
```

вернет:

```python
False
```

Это полезно, когда нужно убедиться, что переданный объект действительно можно вызвать через скобки:

```python
obj()
```

В моем решении `callable()` не обязателен, потому что сабж требует принимать функции, а не валидировать все возможные неправильные входные данные.

## 5. Хитрые вопросы на evaluation

### Что такое функция высшего порядка?

Это функция, которая принимает другую функцию как аргумент или возвращает новую функцию.

### Почему `spell_combiner` возвращает функцию, а не сразу результат?

Потому что задача в том, чтобы создать новый reusable spell.
Мы сначала создаем комбинированное заклинание, а потом вызываем его с конкретными `target` и `power`.

### Что возвращает `spell_combiner`?

Она возвращает функцию `combined_spell`.
А уже `combined_spell(...)` возвращает tuple из двух результатов:

```python
(spell1_result, spell2_result)
```

### Почему `power_amplifier` не изменяет исходную функцию?

Потому что функциональный подход предпочитает создавать новую функцию, а не менять старую.
Оригинальное заклинание остается прежним, а усиленное поведение находится в новой функции.

### Что такое замыкание в `power_amplifier`?

Внутренняя функция `amplified_spell` запоминает `base_spell` и `multiplier` из внешней функции.
Это и есть замыкание.

### Почему `conditional_caster` передает одинаковые аргументы в `condition` и `spell`?

Так требует сабж: и условие, и заклинание получают те же самые `target` и `power`.
Условие решает, можно ли выполнить заклинание с этими данными.

### Почему `spell_sequence` возвращает `list[str]`, а не `str`?

Потому что в сабже написано: "Returns a list of all spell results".
Если вернуть одну строку, это будет отличаться от контракта функции.

### Что будет, если список `spells` пустой?

`spell_sequence([])` вернет функцию.
Если вызвать эту функцию, она вернет пустой список:

```python
[]
```

### Чем `Callable` отличается от `callable()`?

`Callable` - это type hint. Он нужен для аннотаций типов:

```python
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
```

`callable()` - это встроенная функция Python. Она проверяет объект во время выполнения:

```python
callable(spell1)
```

### Почему не используется `lambda` в ex1?

Потому что ex1 тренирует не lambda, а функции высшего порядка.
Здесь нужно создавать вложенные функции через `def`, чтобы вернуть новую функцию с понятным поведением.

### Нарушают ли демонстрационные функции `fireball`, `heal`, `has_enough_power` задание?

Нет. Они нужны только для запуска и демонстрации.
Основные сдаваемые функции - это `spell_combiner`, `power_amplifier`, `conditional_caster`, `spell_sequence`.

# Exercise 2 - Memory Depths

## 1. Что надо сделать, чему учит и какая теория нужна

Нужно создать файл:

```text
ex2/scope_mysteries.py
```

В нем нужно реализовать 4 функции:

```python
def mage_counter() -> Callable
def spell_accumulator(initial_power: int) -> Callable
def enchantment_factory(enchantment_type: str) -> Callable
def memory_vault() -> dict[str, Callable]
```

Упражнение учит lexical scoping, closures и `nonlocal`.

Главная идея: внутренняя функция может "помнить" переменные из внешней функции даже после того, как внешняя функция уже завершилась.

Нужная теория:

- lexical scope - область видимости определяется местом, где функция написана;
- closure - функция вместе с сохраненным окружением;
- `nonlocal` - позволяет изменять переменную из ближайшей внешней функции;
- приватное состояние можно хранить без глобальных переменных.

## 2. Как сделано у меня

Файл: `ex2/scope_mysteries.py`

Импорт:

```python
from collections.abc import Callable
```

`mage_counter` создает независимый счетчик. Переменная `count` живет внутри замыкания:

```python
def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter
```

`spell_accumulator` запоминает текущую накопленную силу:

```python
def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power

    return accumulator
```

`enchantment_factory` запоминает тип зачарования и возвращает функцию для предметов:

```python
def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant
```

`memory_vault` создает приватное хранилище `memories` и возвращает две функции для работы с ним:

```python
def memory_vault() -> dict[str, Callable]:
    memories = {}

    def store(key: str, value: object) -> None:
        memories[key] = value

    def recall(key: str) -> object:
        return memories.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall,
    }
```

Важно: `memories` не является глобальной переменной. Она находится внутри `memory_vault` и доступна только функциям `store` и `recall`.

## 3. Как запустить и продемонстрировать

Перейти в папку модуля:

```bash
cd /home/dev/projects/42/python_modules/python_module_10
```

Запустить:

```bash
python3 ex2/scope_mysteries.py
```

Пример вывода:

```text
Testing mage counter...
counter_a call 1: 1
counter_a call 2: 2
counter_b call 1: 1

Testing spell accumulator...
Base 100, add 20: 120
Base 100, add 30: 150

Testing enchantment factory...
Flaming Sword
Frozen Shield

Testing memory vault...
Store 'secret' = 42
Recall 'secret': 42
Recall 'unknown': Memory not found
```

Для запуска не нужно создавать виртуальное окружение и не нужно ставить зависимости через `pip`.
Используется только стандартная библиотека Python.

Что важно показать на защите:

- `counter_a` и `counter_b` имеют независимое состояние;
- `accumulator` помнит сумму между вызовами;
- `flaming` и `frozen` запоминают разные `enchantment_type`;
- `memory_vault` хранит данные без глобальных переменных.

## 4. Ответы на вопросы по ex2 из сабжа

### How do closures enable functions to "remember" their creation environment?

Замыкание позволяет внутренней функции сохранить доступ к переменным внешней функции.

Например:

```python
def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter
```

Когда `mage_counter()` завершилась, переменная `count` не исчезает, потому что возвращенная функция `counter` продолжает на нее ссылаться.
Поэтому `counter()` "помнит" свое окружение создания.

### What are the benefits of lexical scoping in functional programming?

Lexical scoping делает поведение функций предсказуемым: переменные ищутся там, где функция была написана, а не там, где она была вызвана.

Преимущества:

- можно создавать функции с приватным состоянием;
- не нужны глобальные переменные;
- легче понимать, откуда берутся данные;
- можно создавать независимые экземпляры функций, например два разных счетчика;
- код становится более модульным и безопасным.

### Why is global forbidden, but nonlocal allowed?

`global` запрещен, потому что он изменяет переменную на уровне всего модуля.
Такая переменная доступна отовсюду, и ее может изменить любая часть программы.
Это делает код менее предсказуемым.

`nonlocal` разрешен, потому что он изменяет переменную только из ближайшей внешней функции.
Такое состояние ограничено конкретным замыканием.

Пример с `nonlocal`:

```python
def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter
```

Здесь `count` не виден всему модулю. Он доступен только функции `counter`.

### What are the key differences between global and nonlocal?

`global` работает с переменной уровня модуля.
`nonlocal` работает с переменной из внешней функции.

`global` создает общее состояние для всего файла.
`nonlocal` создает состояние внутри конкретного замыкания.

`global` легко случайно изменить из разных мест.
`nonlocal` ограничен внутренней функцией и ее внешним окружением.

В этом модуле `nonlocal` подходит, потому что нужно сохранить состояние счетчика или аккумулятора, но не делать его общим для всей программы.

## 5. Хитрые вопросы на evaluation

### Что такое closure?

Closure, или замыкание, - это функция, которая запоминает переменные из области, где она была создана.

### Что такое lexical scope?

Lexical scope означает, что область видимости переменных определяется расположением кода.
Внутренняя функция видит переменные внешней функции, потому что она написана внутри нее.

### Зачем нужен `nonlocal`?

`nonlocal` нужен, когда внутренняя функция должна изменить переменную из внешней функции.

Без `nonlocal` такой код сломается:

```python
def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        count += 1
        return count

    return counter
```

Python решит, что `count` - локальная переменная внутри `counter`, и будет ошибка.

### Почему в `enchantment_factory` не нужен `nonlocal`?

Потому что `enchantment_type` только читается, но не изменяется.
`nonlocal` нужен именно для изменения переменной внешней функции.

### Почему в `memory_vault` не нужен `nonlocal` для `memories`?

Потому что мы не переназначаем переменную `memories`.
Мы меняем содержимое словаря:

```python
memories[key] = value
```

Если бы мы писали:

```python
memories = {}
```

внутри `store`, тогда понадобился бы `nonlocal`.

### Почему два счетчика независимы?

Потому что каждый вызов `mage_counter()` создает новую переменную `count` и новое замыкание.

Пример:

```python
counter_a = mage_counter()
counter_b = mage_counter()
```

У `counter_a` свой `count`, у `counter_b` свой `count`.

### Что возвращает `memory_vault()`?

Она возвращает словарь с двумя функциями:

```python
{
    "store": store,
    "recall": recall,
}
```

Функции `store` и `recall` имеют общий доступ к приватному словарю `memories`.

### Почему `store` возвращает `None`?

Потому что ее задача - сохранить значение.
Она изменяет внутреннее хранилище, а не вычисляет новый результат для возврата.

### Что будет, если вызвать `recall` с неизвестным ключом?

Вернется строка:

```python
"Memory not found"
```

Так требует сабж.

### Нарушает ли `memory_vault` запрет на глобальные переменные?

Нет. `memories` находится внутри функции `memory_vault`, а не на уровне файла.
Это приватное состояние замыкания, а не глобальная переменная.

# Exercise 3 - Ancient Library

## 1. Что надо сделать, чему учит и какая теория нужна

Нужно создать файл:

```text
ex3/functools_artifacts.py
```

В нем нужно реализовать 4 функции:

```python
def spell_reducer(spells: list[int], operation: str) -> int
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]
def memoized_fibonacci(n: int) -> int
def spell_dispatcher() -> Callable[[Any], str]
```

Упражнение учит использовать инструменты функционального программирования из стандартной библиотеки:

- `functools.reduce`;
- `functools.partial`;
- `functools.lru_cache`;
- `functools.singledispatch`;
- функции из модуля `operator`.

Главная теория:

- `reduce` сворачивает список значений в одно итоговое значение;
- `partial` создает новую функцию с заранее заполненными аргументами;
- `lru_cache` кеширует результаты функции;
- `singledispatch` выбирает реализацию функции по типу первого аргумента.

## 2. Как сделано у меня

Файл: `ex3/functools_artifacts.py`

Импорты:

```python
import operator
from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from typing import Any
```

`spell_reducer` сворачивает список чисел в одно число.
Поддерживаются операции `"add"`, `"multiply"`, `"max"`, `"min"`:

```python
def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda first, second: max(first, second),
        "min": lambda first, second: min(first, second),
    }

    if operation not in operations:
        return 0

    return reduce(operations[operation], spells)
```

Почему для `max` и `min` используются `lambda`:

```python
"max": lambda first, second: max(first, second)
```

Так `mypy` проще понять, что каждая операция принимает ровно два `int` и возвращает `int`.

`partial_enchanter` создает готовые версии зачарования через `partial`.
У каждой версии заранее заполнены `power=50` и `element`:

```python
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }
```

`memoized_fibonacci` считает Fibonacci и кеширует результаты через `lru_cache`:

```python
@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
```

Кеш можно проверить так:

```python
memoized_fibonacci.cache_info()
```

`spell_dispatcher` использует `singledispatch`.
Одна функция ведет себя по-разному для разных типов:

```python
def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch
```

## 3. Как запустить и продемонстрировать

Перейти в папку модуля:

```bash
cd /home/dev/projects/42/python_modules/python_module_10
```

Запустить:

```bash
python3 ex3/functools_artifacts.py
```

Пример вывода:

```text
Testing spell reducer...
Sum: 100
Product: 240000
Max: 40

Testing partial enchanter...
Fire enchantment on Sword with 50 power
Ice enchantment on Shield with 50 power
Lightning enchantment on Staff with 50 power

Testing memoized fibonacci...
Fib(0): 0
Fib(1): 1
Fib(10): 55
Fib(15): 610

Testing spell dispatcher...
Damage spell: 42 damage
Enchantment: fireball
Multi-cast: 3 spells
Unknown spell type
```

Проверить типизацию:

```bash
mypy ex3
```

Если VS Code показывает старую ошибку про `reduce`, а командная строка проходит, обычно это кеш диагностики IDE или выбран не тот Python interpreter.
Можно сохранить файл, перезагрузить окно VS Code и удалить `.mypy_cache`.

Для запуска не нужно ставить внешние библиотеки.
`functools`, `operator`, `typing` и `collections.abc` входят в стандартную библиотеку Python.

## 4. Ответы на вопросы по ex3 из сабжа

### How does functools.reduce enable powerful data aggregation?

`functools.reduce` позволяет агрегировать список значений в один итоговый результат.

Например, список сил:

```python
[10, 20, 30, 40]
```

можно свернуть в:

- сумму: `100`;
- произведение: `240000`;
- максимум: `40`;
- минимум: `10`.

`reduce` берет первые два элемента, применяет к ним функцию, потом берет результат и следующий элемент, и так до конца списка.

Пример для сложения:

```text
(((10 + 20) + 30) + 40) = 100
```

В моем коде это выглядит так:

```python
return reduce(operations[operation], spells)
```

Сила `reduce` в том, что одна и та же структура кода может выполнять разные агрегации.
Меняется только функция-операция.

### What are the performance benefits of memoization with lru_cache?

`lru_cache` сохраняет результаты предыдущих вызовов функции.
Если функция вызывается повторно с теми же аргументами, Python берет результат из кеша, а не считает заново.

Это особенно полезно для рекурсивного Fibonacci.
Без кеша функция постоянно пересчитывает одни и те же значения.

Например, для `fib(15)` много раз заново считаются `fib(10)`, `fib(9)`, `fib(8)` и так далее.
С `lru_cache` каждое значение `fib(n)` вычисляется один раз, а потом переиспользуется.

Итог:

- меньше повторных вычислений;
- быстрее рекурсивные функции;
- можно проверить статистику кеша через `cache_info()`.

Пример:

```python
memoized_fibonacci.cache_info()
```

## 5. Хитрые вопросы на evaluation

### Что делает `reduce`?

`reduce` применяет функцию к элементам последовательности и сворачивает их в одно значение.

Пример:

```python
reduce(operator.add, [10, 20, 30])
```

результат:

```python
60
```

### Почему для пустого списка возвращается `0`?

Потому что сабж требует: если `spells` пустой, вернуть `0`.
Без этой проверки `reduce` упадет на пустом списке без начального значения.

### Почему неизвестная операция возвращает `0`?

Сабж говорит properly handle the error.
В этом решении неизвестная операция безопасно обрабатывается через возврат `0`, без падения программы.

### Что такое `operator.add` и `operator.mul`?

Это функции из стандартного модуля `operator`.

```python
operator.add(a, b)
```

то же самое, что:

```python
a + b
```

`operator.mul(a, b)` то же самое, что `a * b`.

### Что делает `partial`?

`partial` создает новую функцию, где часть аргументов уже заполнена.

Например:

```python
partial(base_enchantment, 50, "fire")
```

создает функцию, которой потом нужно передать только `target`.

### Почему в `partial_enchanter` возвращается словарь?

Потому что нужно вернуть несколько готовых функций-зачарований.
По ключу `"fire"` лежит fire enchantment, по `"ice"` - ice enchantment, по `"lightning"` - lightning enchantment.

### Что делает `@lru_cache`?

Это декоратор, который кеширует результаты функции.
Если вызвать функцию с теми же аргументами еще раз, результат берется из кеша.

### Что значит LRU?

LRU означает Least Recently Used.
Если кеш ограничен по размеру, самые давно не использованные значения удаляются первыми.

В моем коде используется:

```python
@lru_cache
```

Без указания размера, поэтому используется стандартное поведение декоратора.

### Почему Fibonacci хорошо показывает пользу кеша?

Потому что обычная рекурсивная реализация Fibonacci много раз считает одни и те же значения.
Кеш убирает эти повторные вычисления.

### Что делает `singledispatch`?

`singledispatch` позволяет создать одну функцию с разным поведением для разных типов первого аргумента.

В моем решении:

- `int` -> damage spell;
- `str` -> enchantment;
- `list` -> multi-cast;
- другой тип -> unknown spell type.

### Почему функция называется `_` внутри `@dispatch.register`?

Имя `_` используется, потому что конкретное имя функции не важно.
Важен тип аргумента в аннотации:

```python
def _(spell: int) -> str:
```

`singledispatch` регистрирует эту реализацию для типа `int`.

### Что вернет dispatcher для словаря?

Словарь не зарегистрирован отдельно, поэтому сработает базовая функция:

```python
"Unknown spell type"
```

### Почему `spell_dispatcher` возвращает `dispatch`, а не вызывает его сразу?

Потому что по сабжу нужно создать dispatcher function.
Сначала мы создаем диспетчер, а потом вызываем его с разными типами данных:

```python
dispatcher = spell_dispatcher()
dispatcher(42)
dispatcher("fireball")
```

# Exercise 4 - Master's Tower

## 1. Что надо сделать, чему учит и какая теория нужна

Нужно создать файл:

```text
ex4/decorator_mastery.py
```

В нем нужно реализовать:

```python
def spell_timer(func: Callable) -> Callable
def power_validator(min_power: int) -> Callable
def retry_spell(max_attempts: int) -> Callable

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool

    def cast_spell(self, spell_name: str, power: int) -> str
```

Упражнение учит:

- писать декораторы;
- писать decorator factory;
- использовать `functools.wraps`;
- оборачивать функции с `*args` и `**kwargs`;
- обрабатывать exceptions внутри декоратора;
- использовать `@staticmethod`;
- применять декоратор внутри метода класса.

Главная теория:

- декоратор принимает функцию и возвращает новую функцию;
- `@decorator` - это синтаксический сахар;
- `functools.wraps` сохраняет имя и метаданные оригинальной функции;
- decorator factory сначала принимает параметры, а потом возвращает сам декоратор;
- `staticmethod` - метод класса, которому не нужен `self`.

## 2. Как сделано у меня

Файл: `ex4/decorator_mastery.py`

Импорты:

```python
import time
from collections.abc import Callable
from functools import wraps
```

`spell_timer` измеряет время выполнения функции:

```python
def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result

    return wrapper
```

`power_validator` - это decorator factory.
Он принимает `min_power`, а потом возвращает декоратор:

```python
def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int, *args: object, **kwargs: object) -> object:
            if power >= min_power:
                return func(power, *args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator
```

`retry_spell` повторяет вызов функции, если она падает с exception:

```python
def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator
```

`MageGuild.validate_mage_name` - статический метод.
Он проверяет, что имя минимум 3 символа и состоит только из букв и пробелов:

```python
class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            character.isalpha() or character == " " for character in name
        )
```

`MageGuild.cast_spell` использует `power_validator(10)` внутри метода:

```python
    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def cast(power: int, name: str) -> str:
            return f"Successfully cast {name} with {power} power"

        return cast(power, spell_name)
```

Демонстрационные функции:

```python
@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def unstable_spell() -> str:
    raise ValueError("Spell exploded")


@retry_spell(3)
def successful_spell() -> str:
    return "Waaaaaaagh spelled !"
```

`successful_spell` добавлена, чтобы показать строку из примера сабжа:

```text
Waaaaaaagh spelled !
```

## 3. Как запустить и продемонстрировать

Перейти в папку модуля:

```bash
cd /home/dev/projects/42/python_modules/python_module_10
```

Запустить:

```bash
python3 ex4/decorator_mastery.py
```

Пример вывода:

```text
Testing spell timer...
Casting fireball...
Spell completed in 0.100 seconds
Result: Fireball cast!

Testing retrying spell...
Spell failed, retrying... (attempt 1/3)
Spell failed, retrying... (attempt 2/3)
Spell casting failed after 3 attempts
Waaaaaaagh spelled !

Testing MageGuild...
True
False
Successfully cast Lightning with 15 power
Insufficient power for this spell
```

Время может быть `0.100`, `0.101`, `0.102` и так далее.
Это нормально, потому что `time.sleep(0.1)` не гарантирует точное время до миллисекунды.
Важно, что формат такой:

```text
Spell completed in X.XXX seconds
```

Для запуска не нужно ставить внешние библиотеки.
Используются только `time`, `collections.abc` и `functools` из стандартной библиотеки.

## 4. Ответы на вопросы по ex4 из сабжа

### How do decorators enable separation of concerns?

Декораторы позволяют вынести дополнительное поведение отдельно от основной логики функции.

Например, `fireball` отвечает только за результат заклинания:

```python
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"
```

А `spell_timer` отдельно отвечает за измерение времени.
Так логика заклинания не смешивается с логикой логирования и тайминга.

То же самое с `retry_spell`: функция не обязана сама знать, сколько раз ее повторять при ошибке.
Этим занимается декоратор.

### What's the difference between @staticmethod and regular instance methods?

Обычный instance method получает `self` первым аргументом.
Он работает с конкретным объектом класса:

```python
def cast_spell(self, spell_name: str, power: int) -> str:
```

`@staticmethod` не получает `self`.
Он не зависит от состояния конкретного объекта:

```python
@staticmethod
def validate_mage_name(name: str) -> bool:
```

`validate_mage_name` сделан статическим методом, потому что для проверки имени не нужны поля объекта `MageGuild`.
Метод зависит только от аргумента `name`.

## 5. Хитрые вопросы на evaluation

### Что такое декоратор?

Декоратор - это функция, которая принимает другую функцию и возвращает новую функцию с измененным или дополненным поведением.

### Что означает `@spell_timer`?

Это короткая форма записи:

```python
fireball = spell_timer(fireball)
```

То есть функция `fireball` заменяется результатом вызова `spell_timer(fireball)`.

### Зачем нужен `functools.wraps`?

`wraps` сохраняет метаданные оригинальной функции:

- `__name__`;
- `__doc__`;
- другие служебные атрибуты.

Без `wraps` декорированная функция могла бы называться `wrapper`, а не `fireball`.

### Почему в wrapper используются `*args` и `**kwargs`?

Чтобы декоратор мог работать с функциями с разными аргументами.

```python
def wrapper(*args: object, **kwargs: object) -> object:
```

Такой wrapper принимает любые позиционные и именованные аргументы и передает их дальше в оригинальную функцию.

### Что такое decorator factory?

Decorator factory - это функция, которая сначала принимает параметры, а потом возвращает декоратор.

Например:

```python
@power_validator(10)
```

Сначала вызывается `power_validator(10)`, он возвращает `decorator`, и уже этот `decorator` оборачивает функцию.

### Почему `power_validator` имеет три уровня функций?

Потому что нужно:

1. принять `min_power`;
2. принять функцию, которую декорируем;
3. создать wrapper, который будет выполняться при вызове функции.

Структура:

```python
power_validator -> decorator -> wrapper
```

### Почему `power_validator` проверяет первый аргумент `power`?

Так требует сабж: декоратор применяется к standalone function, whose first argument is power.
В `cast_spell` внутренняя функция `cast` специально написана так:

```python
def cast(power: int, name: str) -> str:
```

Поэтому `power_validator(10)` может проверить первый аргумент.

### Почему `cast_spell` создает внутреннюю функцию `cast`?

Потому что `power_validator` ожидает, что первым аргументом будет `power`.
У метода `cast_spell(self, spell_name, power)` первым аргументом технически является `self`, поэтому удобнее создать внутреннюю функцию:

```python
def cast(power: int, name: str) -> str:
```

и применить декоратор к ней.

### Что делает `retry_spell`?

Он вызывает функцию.
Если функция бросает exception, декоратор пробует вызвать ее еще раз до `max_attempts`.
Если все попытки провалились, возвращается строка:

```python
"Spell casting failed after 3 attempts"
```

### Почему retry печатает только attempt 1/3 и 2/3, но не 3/3?

Потому что после третьей неудачи уже нет следующей попытки.
В этот момент функция возвращает итоговое сообщение о полном провале.

### Почему используется `except Exception`?

Потому что декоратор должен ловить обычные ошибки выполнения заклинания и повторять попытку.
В учебном задании это достаточно.

### Почему `time.sleep(0.1)` может дать 0.100 или 0.101 seconds?

Потому что операционная система не гарантирует пробуждение ровно через 0.100 секунды.
Измеренное время может немного отличаться.

### Что проверяет `validate_mage_name`?

Он проверяет:

- длина имени минимум 3 символа;
- каждый символ является буквой или пробелом.

Примеры:

```python
MageGuild.validate_mage_name("Alex")  # True
MageGuild.validate_mage_name("Jo")    # False
```

### Почему `validate_mage_name` статический метод?

Потому что он не использует `self` и не зависит от состояния объекта.
Это просто проверка входной строки.

### Нарушает ли `successful_spell` задание?

Нет. Это демонстрационная функция.
Она показывает успешный вызов под `retry_spell` и добавляет строку из expected output сабжа:

```text
Waaaaaaagh spelled !
```

Основные сдаваемые элементы остаются теми же:

- `spell_timer`;
- `power_validator`;
- `retry_spell`;
- `MageGuild`.
