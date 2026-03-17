#!/usr/bin/env python3


from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

NumericInput = Union[int, float, List[Union[int, float]]]
ProcessorContext = Dict[str, Optional[str]]


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.printing_validation: bool = True

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self.context: ProcessorContext = {"last_validation": None}

    def validate(self, data: Any) -> bool:
        """Разрешаем число или непустой список чисел int/float."""
        if isinstance(data, (int, float)):
            self.context["last_validation"] = "Numeric data verified"
            return True
        if (
            isinstance(data, list)
            and len(data) > 0
            and all(isinstance(item, (int, float)) for item in data)
        ):
            self.context["last_validation"] = "Numeric data verified"
            return True
        self.context["last_validation"] = None
        return False

    def process(self, data: Any) -> str:
        """Считаем количество, сумму и среднее значение."""
        if not self.validate(data):
            raise ValueError("NumericProcessor received invalid data")
        elif self.printing_validation:
            print(f"Validation: {self.context['last_validation']}")

        normalized: NumericInput = data
        numbers: List[Union[int, float]]
        if isinstance(normalized, (int, float)):
            numbers = [normalized]
        else:
            numbers = normalized
        count = len(numbers)
        total = sum(numbers)
        average = total / count
        return (
            f"Processed {count} numeric values, "
            f"sum={total}, avg={average}"
        )


class TextProcessor(DataProcessor):
    """Специализированный процессор текстовых данных."""

    def __init__(self) -> None:
        super().__init__()
        self.context: ProcessorContext = {"last_validation": None}

    def validate(self, data: Any) -> bool:
        """Для текста подходит только строка."""
        is_valid = isinstance(data, str)
        self.context["last_validation"] = (
            "Text data verified" if is_valid else None
        )
        return is_valid

    def process(self, data: Any) -> str:
        """Считаем символы и слова в строке."""
        if not self.validate(data):
            raise ValueError("TextProcessor received invalid data")
        elif self.printing_validation:
            print(f"Validation: {self.context['last_validation']}")

        text = data
        chars = len(text)
        words = len(text.split())
        return f"Processed text: {chars} characters, {words} words"


class LogProcessor(DataProcessor):
    """Специализированный процессор лог-сообщений."""

    LEVELS = {"ERROR", "WARNING", "INFO", "DEBUG"}

    def __init__(self) -> None:
        super().__init__()
        self.context: ProcessorContext = {"last_validation": None}

    def validate(self, data: Any) -> bool:
        """Лог должен быть строкой с форматом LEVEL: message."""
        if not isinstance(data, str) or ":" not in data:
            self.context["last_validation"] = None
            return False
        level = data.split(":", 1)[0].strip().upper()
        is_valid = level in self.LEVELS
        self.context["last_validation"] = (
            "Log entry verified" if is_valid else None
        )
        return is_valid

    def process(self, data: Any) -> str:
        """Извлекаем уровень лога и текст сообщения."""
        if not self.validate(data):
            raise ValueError("LogProcessor received invalid log entry")
        elif self.printing_validation:
            print(f"Validation: {self.context['last_validation']}")

        raw_level, raw_message = data.split(":", 1)
        level = raw_level.strip().upper()
        message = raw_message.strip()
        label = "ALERT" if level == "ERROR" else "INFO"
        return f"[{label}] {level} level detected: {message}"


def safe_run(processor: DataProcessor, data: Any) -> str:
    """Единая точка запуска процессора с безопасной обработкой ошибок.

    Этот helper нужен, чтобы в stream_processor() полиморфно вызывать разные
    процессоры через общий интерфейс DataProcessor и не дублировать
    try/except-блоки.
    """
    try:
        return processor.process(data)
    except Exception as e:
        return f"Processing error: {e}"


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    demos: List[tuple[str, DataProcessor, Any]] = [
        ("Numeric Processor", numeric, [1, 2, 3, 4, 5]),
        ("Text Processor", text, "Hello Nexus World"),
        ("Log Processor", log, "ERROR: Connection timeout")]

    for title, processor, sample in demos:
        print(f"Initializing {title}...")
        if isinstance(sample, str):
            print(f'Processing data: "{sample}"')
        else:
            print(f"Processing data: {sample}")
        result = safe_run(processor, sample)
        print(processor.format_output(result))
        print()

    print("=== Polymorphic Processing Demo ===")
    print()
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [numeric, text, log]
    mixed_samples: List[Any] = [
        [1, 2, 3],
        "Hello World!",
        "INFO: System ready",]

    index = 1
    while index < len(processors) + 1:
        processor = processors[index - 1]
        processor.printing_validation = False
        sample = mixed_samples[index - 1]
        result = safe_run(processor, sample)
        print(f"Result {index}: {result}")
        index += 1
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
