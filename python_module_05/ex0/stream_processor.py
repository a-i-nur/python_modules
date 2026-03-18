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
        """Accept a single number or a non-empty list of numeric values."""
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
        """Return the count, sum, and average for the validated input."""
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
        len_nums = len(numbers)
        sum_nums = sum(numbers)
        average = sum_nums / len_nums
        return (
            f"Processed {len_nums} numeric values, "
            f"sum={sum_nums}, avg={average}")


class TextProcessor(DataProcessor):
    """Process plain text input and report basic text statistics."""

    def __init__(self) -> None:
        super().__init__()
        self.context: ProcessorContext = {"last_validation": None}

    def validate(self, data: Any) -> bool:
        """Accept only string input."""
        is_valid = isinstance(data, str)
        if is_valid:
            self.context["last_validation"] = "Text data verified"
        else:
            self.context["last_validation"] = None
        return is_valid

    def process(self, data: Any) -> str:
        """Return the character and word counts for the given text."""
        if not self.validate(data):
            raise ValueError("TextProcessor received invalid data")
        elif self.printing_validation:
            print(f"Validation: {self.context['last_validation']}")

        text = data
        len_text = len(text)
        count_words = len(text.split())
        return f"Processed text: {len_text} characters, {count_words} words"


class LogProcessor(DataProcessor):
    """Process log entries formatted as a level followed by a message."""

    LOG_LEVELS = {"ERROR", "WARNING", "INFO", "DEBUG", "CRITICAL"}

    def __init__(self) -> None:
        super().__init__()
        self.context: ProcessorContext = {"last_validation": None}

    def validate(self, data: Any) -> bool:
        """Accept log entries in the ``LEVEL: message`` format."""
        if not isinstance(data, str) or ":" not in data:
            self.context["last_validation"] = None
            return False
        level = data.split(":", 1)[0].strip().upper()
        is_valid = level in self.LOG_LEVELS
        if is_valid:
            self.context["last_validation"] = "Log entry verified"
        else:
            self.context["last_validation"] = None
        return is_valid

    def process(self, data: Any) -> str:
        """Extract the log level and message and format them for output."""
        if not self.validate(data):
            raise ValueError("LogProcessor received invalid log entry")
        elif self.printing_validation:
            print(f"Validation: {self.context['last_validation']}")

        raw_level, raw_message = data.split(":", 1)
        level = raw_level.strip().upper()
        message = raw_message.strip()
        if level == "ERROR" or level == "CRITICAL":
            label = "[ALERT]"
        elif level == "WARNING":
            label = "[WARNING]"
        elif level == "DEBUG":
            label = "[DEBUG]"
        else:
            label = "[INFO]"
        return f"{label} {level} level detected: {message}"


def safe_run(processor: DataProcessor, data: Any) -> str:
    """Run any processor through a shared interface and handle failures safely.

    This helper keeps ``stream_processor()`` focused on orchestration by
    centralizing exception handling for all ``DataProcessor`` implementations.
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

    test_cases: List[tuple[str, DataProcessor, Any]] = [
        ("Numeric Processor", numeric, [1, 2, 3, 4, 5]),
        ("Text Processor", text, "Hello Nexus World"),
        ("Log Processor", log, "ERROR: Connection timeout")]

    for title, processor, input_data in test_cases:
        print(f"Initializing {title}...")
        if isinstance(input_data, str):
            print(f'Processing data: "{input_data}"')
        else:
            print(f"Processing data: {input_data}")
        result = safe_run(processor, input_data)
        print(processor.format_output(result))
        print()

    print("=== Polymorphic Processing Demo ===")
    print()
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [numeric, text, log]
    mixed_input: List[Any] = [
        [1, 2, 3],
        "Hello World!",
        "INFO: System ready"]

    i = 0
    while i < len(processors):
        processor = processors[i]
        processor.printing_validation = False
        input_data = mixed_input[i]
        result = safe_run(processor, input_data)
        print(f"Result {i + 1}: {result}")
        i += 1
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
