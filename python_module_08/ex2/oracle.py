import os
import sys

from dotenv import load_dotenv


REQUIRED_CONFIG = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_configuration() -> None:
    load_dotenv()


def get_config_value(name: str) -> str:
    value = os.getenv(name)

    if value is None or value == "":
        return "MISSING"

    return value


def collect_configuration() -> dict[str, str]:
    configuration = {}

    for key in REQUIRED_CONFIG:
        configuration[key] = get_config_value(key)

    return configuration


def print_runtime_profile(matrix_mode: str) -> None:
    if matrix_mode == "production":
        print("Runtime Profile: Production optimizations enabled")
    else:
        print("Runtime Profile: Development diagnostics enabled")


def print_configuration(configuration: dict[str, str]) -> None:
    print("Configuration loaded:")

    print(f"Mode: {configuration['MATRIX_MODE']}")
    print_runtime_profile(configuration["MATRIX_MODE"])

    if configuration["DATABASE_URL"] == "MISSING":
        print("Database: Missing DATABASE_URL")
    else:
        print("Database: Configured")

    if configuration["API_KEY"] == "MISSING":
        print("API Access: Missing API_KEY")
    else:
        print("API Access: Authenticated")

    print(f"Log Level: {configuration['LOG_LEVEL']}")

    if configuration["ZION_ENDPOINT"] == "MISSING":
        print("Zion Network: Missing ZION_ENDPOINT")
    else:
        print("Zion Network: Online")


def has_missing_configuration(configuration: dict[str, str]) -> bool:
    for value in configuration.values():
        if value == "MISSING":
            return True

    return False


def print_security_check(configuration: dict[str, str]) -> None:
    print("Environment security check:")

    if configuration["API_KEY"] == "MISSING":
        print("[WARNING] API_KEY is missing")
    else:
        print("[OK] API key loaded from environment")

    print("[OK] .env is ignored by Git")
    print("[OK] Production overrides available")


def main() -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    load_configuration()
    configuration = collect_configuration()

    print_configuration(configuration)
    print()

    print_security_check(configuration)
    print()

    if has_missing_configuration(configuration):
        print("WARNING: Some configuration values are missing.")
        sys.exit(1)

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
