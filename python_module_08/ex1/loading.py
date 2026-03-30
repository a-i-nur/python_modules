"""Exercise 01: Loading Programs (loading.py).

Этот скрипт соответствует требованиям сабжа:
- Использует pandas, numpy, matplotlib (и опционально requests).
- Делает анализ тестовых данных Matrix.
- Генерирует простую визуализацию в файл matrix_analysis.png.
- Аккуратно обрабатывает отсутствие зависимостей.
- Показывает версии установленных пакетов.
- Демонстрирует разницу между workflow pip и Poetry.

Ограничения сабжа для ex1: pandas, requests, matplotlib, numpy, sys, importlib.
"""

import importlib
import sys


# Список библиотек из сабжа.
# required=True -> без этой библиотеки программа не сможет выполнить анализ.
# required=False -> дополнительная библиотека (requests), разрешена и полезна,
#                  но не обязательна для выполнения задания.
LIBRARIES: list[tuple[str, str, bool]] = [
    ("pandas", "Data manipulation", True),
    ("numpy", "Numerical computations", True),
    ("matplotlib", "Visualization", True),
    ("requests", "Network access", False),
]


def import_optional_module(module_name: str) -> object | None:
    """Пробуем импортировать модуль и вернуть объект модуля либо None."""
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def check_dependencies() -> bool:
    """Проверка доступности библиотек и вывод их версий.

    Возвращает True, если все обязательные зависимости найдены.
    Возвращает False, если хотя бы одна обязательная зависимость отсутствует.
    """
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    missing_required = False

    for name, description, required in LIBRARIES:
        module = import_optional_module(name)

        if module is None:
            if required:
                print(
                    f"[MISSING] {name} - "
                    f"{description} not available"
                )
                missing_required = True
            else:
                print(
                    f"[OPTIONAL] {name} - "
                    f"{description} not available"
                )
            continue

        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - {description} ready")

    return not missing_required


def read_requirements_packages() -> list[str]:
    """Читаем requirements.txt и извлекаем имена пакетов.

    Парсер упрощённый, но достаточный для учебного сабжа.
    """
    packages: list[str] = []

    try:
        with open("requirements.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except OSError:
        return packages

    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        # Отсекаем версии вида ==, >=, <=.
        name = line.split("==")[0].split(">=")[0].split("<=")[0].strip()
        packages.append(name)

    return packages


def read_pyproject_packages() -> list[str]:
    """Читаем pyproject.toml и извлекаем dependencies из секции Poetry.

    Специально делаем простой парсинг текстом, чтобы не вводить
    дополнительные модули сверх списка из сабжа.
    """
    packages: list[str] = []
    inside_poetry_dependencies = False

    try:
        with open("pyproject.toml", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except OSError:
        return packages

    for raw_line in lines:
        line = raw_line.strip()

        if line == "[tool.poetry.dependencies]":
            inside_poetry_dependencies = True
            continue

        # Если встретили новую секцию TOML, прекращаем обработку зависимостей.
        if (
            inside_poetry_dependencies
            and line.startswith("[")
            and line.endswith("]")
        ):
            break

        if not inside_poetry_dependencies:
            continue

        if not line or line.startswith("#") or "=" not in line:
            continue

        name = line.split("=", 1)[0].strip()
        if name.lower() != "python":
            packages.append(name)

    return packages


def show_dependency_files_comparison() -> None:
    """Показываем, какие пакеты заявлены для pip и Poetry.

    Этим выполняем пункт сабжа "demonstrates difference between pip and Poetry
    dependency management".
    """
    pip_packages = read_requirements_packages()
    poetry_packages = read_pyproject_packages()

    print("Dependency management overview:")
    print("- pip source file: requirements.txt")
    if pip_packages:
        print("  packages:", ", ".join(pip_packages))
    else:
        print("  packages: not found or file missing")

    print("- Poetry source file: pyproject.toml")
    if poetry_packages:
        print("  packages:", ", ".join(poetry_packages))
    else:
        print("  packages: not found or file missing")


def print_install_help() -> None:
    """Печать подсказок по установке зависимостей."""
    print("\nDEPENDENCY ERROR: Required libraries are missing.")
    print("Install dependencies using one of these approaches:")
    print("1) pip")
    print("   pip install -r requirements.txt")
    print("2) Poetry")
    print("   poetry install")
    print("   poetry run python loading.py")


def run_matrix_analysis() -> None:
    """Создаём и анализируем учебные данные Matrix.

    Важный момент для сабжа: данные не обязаны быть реальными,
    можно использовать simulated/sample data.
    """
    numpy_module = importlib.import_module("numpy")
    pandas_module = importlib.import_module("pandas")
    pyplot = importlib.import_module("matplotlib.pyplot")

    print("Analyzing Matrix data...")

    # 1000 точек по требованию из expected behavior.
    point_count = 1000
    x_axis = numpy_module.linspace(0.0, 20.0, point_count)

    # Сигнал = синус + небольшой шум (чтобы данные выглядели реалистичнее).
    noise = numpy_module.random.normal(0.0, 0.15, point_count)
    signal = numpy_module.sin(x_axis) + noise

    data_frame = pandas_module.DataFrame(
        {
            "time": x_axis,
            "signal": signal,
        }
    )

    print(f"Processing {len(data_frame)} data points...")

    # Визуализация: обычный line-plot.
    pyplot.figure(figsize=(10, 5))
    pyplot.plot(data_frame["time"], data_frame["signal"], linewidth=1.0)
    pyplot.title("Matrix Data Signal")
    pyplot.xlabel("Time")
    pyplot.ylabel("Signal")
    pyplot.grid(True)
    pyplot.tight_layout()

    output_file = "matrix_analysis.png"
    pyplot.savefig(output_file)
    pyplot.close()

    print("Generating visualization...")
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    """Точка входа ex1."""
    show_dependency_files_comparison()

    if not check_dependencies():
        print_install_help()
        sys.exit(1)

    run_matrix_analysis()


if __name__ == "__main__":
    main()
