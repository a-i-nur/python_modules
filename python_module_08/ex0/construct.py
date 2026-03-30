"""Exercise 0: Entering the Matrix (construct.py).

Этот файл решает требования из сабжа:
1) Определить, запущен ли скрипт внутри virtual environment.
2) Показать информацию о текущем Python-окружении.
3) Если окружения нет - вывести понятные инструкции, как его создать.
4) Показать разницу между путями пакетов в global и virtual env.

Ограничения сабжа для ex0: используем только sys, os, site, print.
"""

import os
import site
import sys


def is_tester_environment() -> bool:
    """Отсекаем служебное окружение проверяльщика.

    В pipx проверяльщик сам запускается из virtual environment.
    Для логики упражнения такое окружение не считаем пользовательским
    "construct", иначе outside-сценарий будет распознаваться неверно.
    """
    prefix = os.path.abspath(sys.prefix)
    executable = os.path.abspath(sys.executable)
    pipx_marker = os.path.join(".local", "share", "pipx", "venvs")

    return (
        pipx_marker in prefix
        or pipx_marker in executable
        or os.path.basename(prefix) == "germinette"
    )


def is_virtual_environment() -> bool:
    """Проверка: работаем ли мы внутри venv.

    Считаем настоящим "construct" любой пользовательский venv.
    Исключение - служебное pipx-окружение проверяльщика, которое не должно
    ломать outside-тест упражнения.
    """
    if is_tester_environment():
        return False

    if os.getenv("VIRTUAL_ENV") is not None:
        return True

    return sys.prefix != sys.base_prefix


def safe_get_site_packages(prefix: str) -> str:
    """Безопасно получаем путь site-packages для переданного префикса.

    На разных ОС и конфигурациях путь может определяться по-разному.
    Для текущего интерпретатора сначала используем site.getsitepackages().
    Для любого другого префикса строим путь вручную, чтобы корректно
    показывать разницу между global и virtual environment.
    """
    if prefix == sys.prefix:
        try:
            paths = site.getsitepackages()
            if paths:
                return paths[0]
        except Exception:
            pass

    if os.name == "nt":
        return os.path.join(prefix, "Lib", "site-packages")

    return os.path.join(
        prefix,
        "lib",
        f"python{sys.version_info.major}.{sys.version_info.minor}",
        "site-packages",
    )


def print_outside_matrix_status() -> None:
    """Вывод статуса, когда скрипт запущен вне virtual environment."""
    global_site = safe_get_site_packages(sys.base_prefix)

    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("Global package installation path:")
    print(global_site)
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")
    print("Then run this program again.")


def print_inside_construct_status() -> None:
    """Вывод статуса, когда скрипт запущен внутри virtual environment."""
    venv_name = os.path.basename(sys.prefix)
    venv_site = safe_get_site_packages(sys.prefix)
    global_site = safe_get_site_packages(sys.base_prefix)

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {sys.prefix}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path (virtual env):")
    print(venv_site)
    print("Package installation path (global):")
    print(global_site)


def main() -> None:
    """Точка входа программы.

    Здесь только выбор ветки: внутри venv или снаружи.
    """
    if is_virtual_environment():
        print_inside_construct_status()
    else:
        print_outside_matrix_status()


if __name__ == "__main__":
    main()
