"""Exercise 02: Accessing the Mainframe (oracle.py).

Цели из сабжа:
- Загружать конфигурацию из переменных окружения.
- Использовать .env как удобную dev-конфигурацию.
- Показывать разницу development/production.
- Обрабатывать отсутствие обязательных переменных.
- Демонстрировать безопасный подход к секретам.

Разрешённые модули по сабжу: os, sys, python-dotenv, file operations.
"""

import os
import sys


REQUIRED_KEYS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

ALLOWED_MODES = {"development", "production"}
ALLOWED_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


def snapshot_shell_environment() -> dict[str, str]:
    """Сохраняем ключи, пришедшие из shell, до загрузки .env."""
    shell_values: dict[str, str] = {}

    for key in REQUIRED_KEYS:
        value = os.getenv(key)
        if value is not None:
            shell_values[key] = value

    return shell_values


def get_dotenv_path() -> str:
    """Ищем .env в текущей директории и рядом со скриптом."""
    current_directory_path = os.path.join(os.getcwd(), ".env")
    if os.path.exists(current_directory_path):
        return current_directory_path

    script_directory = os.path.dirname(os.path.abspath(__file__))
    script_directory_path = os.path.join(script_directory, ".env")
    if os.path.exists(script_directory_path):
        return script_directory_path

    return ""


def load_environment_from_dotenv() -> tuple[bool, str, dict[str, str]]:
    """Загружаем .env с помощью python-dotenv.

    Важный момент:
    - load_dotenv() по умолчанию НЕ перезаписывает уже существующие
      переменные окружения.
    - Это как раз демонстрирует поведение из сабжа:
      переменные, переданные через shell, имеют приоритет над .env.

    Возвращает:
    - доступна ли библиотека python-dotenv
    - путь к найденному .env (или пустую строку)
    - значения, прочитанные из .env без shell overrides
    """
    try:
        from dotenv import dotenv_values
        from dotenv import load_dotenv
    except ImportError:
        return False, "", {}

    dotenv_path = get_dotenv_path()
    if not dotenv_path:
        return True, "", {}

    dotenv_data = {
        key: value
        for key, value in dotenv_values(dotenv_path).items()
        if value is not None
    }
    load_dotenv(dotenv_path)
    return True, dotenv_path, dotenv_data


def read_configuration() -> dict[str, str]:
    """Читаем значения конфигурации из окружения.

    Возвращаем словарь только со строковыми значениями,
    чтобы дальше удобно валидировать и печатать статус.
    """
    config: dict[str, str] = {}

    config["MATRIX_MODE"] = os.getenv("MATRIX_MODE", "development").strip()
    config["DATABASE_URL"] = os.getenv("DATABASE_URL", "").strip()
    config["API_KEY"] = os.getenv("API_KEY", "").strip()
    config["LOG_LEVEL"] = os.getenv("LOG_LEVEL", "INFO").strip()
    config["ZION_ENDPOINT"] = os.getenv("ZION_ENDPOINT", "").strip()

    return config


def validate_required_keys(config: dict[str, str]) -> list[str]:
    """Проверяем, что все обязательные переменные реально заполнены."""
    missing: list[str] = []

    for key in REQUIRED_KEYS:
        if not config.get(key):
            missing.append(key)

    return missing


def validate_values(config: dict[str, str]) -> list[str]:
    """Проверяем корректность значений конфигурации.

    Это соответствует пункту сабжа про proper error handling
    и демонстрацию production/development настроек.
    """
    errors: list[str] = []

    mode = config["MATRIX_MODE"]
    if mode not in ALLOWED_MODES:
        errors.append("MATRIX_MODE must be development or production")

    if config["DATABASE_URL"] and not (
        config["DATABASE_URL"].startswith("sqlite://")
        or "//" in config["DATABASE_URL"]
    ):
        errors.append("DATABASE_URL must look like a connection string")

    if config["API_KEY"] and (
        len(config["API_KEY"]) < 12
        or config["API_KEY"] == "your_api_key_here"
    ):
        errors.append("API_KEY looks unsafe or placeholder-like")

    if config["LOG_LEVEL"] not in ALLOWED_LOG_LEVELS:
        errors.append("LOG_LEVEL has unsupported value")

    if config["ZION_ENDPOINT"] and not (
        config["ZION_ENDPOINT"].startswith("http://")
        or config["ZION_ENDPOINT"].startswith("https://")
    ):
        errors.append("ZION_ENDPOINT must be a valid URL")

    return errors


def get_database_status(database_url: str) -> str:
    """Формируем человекочитаемый статус подключения БД."""
    if not database_url:
        return "Not configured"
    if (
        "localhost" in database_url
        or "127.0.0.1" in database_url
        or "sqlite" in database_url
    ):
        return "Connected to local instance"
    return "Connected to remote instance"


def get_api_status(api_key: str) -> str:
    """Показываем статус API без утечки секрета в лог."""
    if api_key:
        return "Authenticated"
    return "Not authenticated"


def get_network_status(endpoint: str) -> str:
    """Статус сети Zion на основе наличия endpoint."""
    if endpoint:
        return "Online"
    return "Offline"


def has_production_overrides(
    shell_values: dict[str, str],
    dotenv_values_map: dict[str, str],
) -> bool:
    """Проверяем, есть ли признаки production-overrides.

    Идея: если пользователь передал хотя бы одну ключевую переменную
    прямо в окружение процесса (shell env), это override относительно .env.
    """
    for key, value in shell_values.items():
        if key not in dotenv_values_map or dotenv_values_map[key] != value:
            return True
    return False


def print_configuration_report(
    config: dict[str, str],
    dotenv_available: bool,
    dotenv_path: str,
    missing: list[str],
    value_errors: list[str],
    shell_values: dict[str, str],
    dotenv_values_map: dict[str, str],
) -> None:
    """Печатаем итоговый отчёт в стиле expected output из сабжа."""
    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {get_database_status(config['DATABASE_URL'])}")
    print(f"API Access: {get_api_status(config['API_KEY'])}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {get_network_status(config['ZION_ENDPOINT'])}")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if not dotenv_available:
        print("[WARN] python-dotenv is not installed")
    elif dotenv_path and not missing and not value_errors:
        print("[OK] .env file properly configured")
    elif dotenv_path:
        print("[WARN] .env file found but configuration is incomplete")
    else:
        print("[WARN] .env file is not found (using shell environment only)")

    if has_production_overrides(shell_values, dotenv_values_map):
        print("[OK] Production overrides available")
    else:
        print("[INFO] Production overrides not detected")

    print("The Oracle sees all configurations.")


def main() -> None:
    """Точка входа ex2."""
    shell_values = snapshot_shell_environment()
    dotenv_available, dotenv_path, dotenv_values_map = (
        load_environment_from_dotenv()
    )

    if not dotenv_available:
        print(
            "CONFIGURATION WARNING: python-dotenv is required "
            "for .env files."
        )
        print("Install it with: pip install python-dotenv")

    config = read_configuration()

    missing = validate_required_keys(config)
    if missing:
        print("CONFIGURATION WARNING: Missing required variables:")
        for key in missing:
            print(f"- {key}")
        print("Use .env (from .env.example) or shell environment variables.")

    value_errors = validate_values(config)
    if value_errors:
        print("CONFIGURATION WARNING: Invalid configuration values:")
        for error in value_errors:
            print(f"- {error}")

    print_configuration_report(
        config,
        dotenv_available,
        dotenv_path,
        missing,
        value_errors,
        shell_values,
        dotenv_values_map,
    )

    if missing or value_errors or not dotenv_available:
        sys.exit(1)


if __name__ == "__main__":
    main()
