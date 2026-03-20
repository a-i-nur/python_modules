#!/usr/bin/env python3
"""Exercise 1: Polymorphic Streams."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

SensorInfo = Dict[str, Union[str, float]]
TransactionInfo = Dict[str, Union[str, float]]
StreamStats = Dict[str, Union[str, int, float]]


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0
        self.failed_batches: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> StreamStats:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count,
            "failed_batches": self.failed_batches}


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        # счетчик критических температур
        self.alert_count: int = 0
        # средняя температура последнего обработанного батча
        self.last_avg_temp: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        readings = self._parse_batch(data_batch)
        if not readings:
            raise ValueError("sensor batch has no valid readings")

        print(f"Processing sensor batch: {data_batch}")
        self.processed_count += len(readings)

        # извлекаем только температурные показания для анализа
        temps = [
            float(item["value"])
            for item in readings
            if item["kind"] == "temp"]
        if not temps:
            raise ValueError("sensor batch has no temperature readings")

        self.last_avg_temp = sum(temps) / len(temps)
        self.alert_count += sum(1 for temp in temps if temp >= 30.0)

        # формируем строку с результатами анализа
        return (
            f"Sensor analysis: {len(readings)} readings processed, "
            f"avg temp: {self.last_avg_temp:.1f}°C")

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        # если критерий не "high_priority", возвращаем данные без изменений
        if criteria != "high_priority":
            return data_batch
        readings = self._parse_batch(data_batch)
        # фильтруем только температурные показания выше 30.0°C
        return [
            f"{item['kind']}:{item['value']}"
            for item in readings
            if item["kind"] == "temp" and float(item["value"]) >= 30.0]

    def get_stats(self) -> StreamStats:
        stats = super().get_stats()
        stats["stream_type"] = "sensor"
        stats["alert_count"] = self.alert_count
        stats["last_avg_temp"] = float(f"{self.last_avg_temp:.1f}")
        return stats

    def _parse_batch(self, data_batch: List[Any]) -> List[SensorInfo]:
        readings: List[SensorInfo] = []
        for item in data_batch:
            if not isinstance(item, str) or ":" not in item:
                continue
            raw_kind, raw_value = item.split(":", 1)
            kind = raw_kind.strip().lower()
            if kind not in {"temp", "humidity", "pressure"}:
                continue
            try:
                value = float(raw_value.strip())
            except ValueError:
                continue
            readings.append({"kind": kind, "value": value})
        return readings


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        # общий чистый денежный поток
        # (положительный для покупок, отрицательный для продаж)
        self.net_flow_total: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        transactions = self._parse_batch(data_batch)
        if not transactions:
            raise ValueError("transaction batch has no valid operations")

        print(f"Processing transaction batch: {data_batch}")
        self.processed_count += len(transactions)

        # вычисляем чистый денежный поток для текущего батча
        net_flow = 0.0
        # покупка (buy) увеличивает поток, продажа (sell) уменьшает
        for item in transactions:
            # извлекаем сумму и направление операции
            amount = float(item["amount"])
            # покупка увеличивает денежный поток, продажа уменьшает
            if item["action"] == "buy":
                net_flow += amount
            else:
                net_flow -= amount

        # обновляем общий чистый денежный поток для всего потока данных
        self.net_flow_total += net_flow
        # добавляем знак "+" для положительного потока,
        # иначе оставляем без знака
        sign = "+" if net_flow > 0 else "-"

        return (
            f"Transaction analysis: {len(transactions)} operations, "
            f"net flow: {sign}{net_flow:.1f} units")

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria != "high_priority":
            return data_batch
        transactions = self._parse_batch(data_batch)
        # фильтруем только операции с суммой 150.0 или выше
        return [
            f"{item['action']}:{item['amount']}"
            for item in transactions
            if float(item["amount"]) >= 150.0]

    def get_stats(self) -> StreamStats:
        stats = super().get_stats()
        stats["stream_type"] = "transaction"
        stats["net_flow_total"] = float(f"{self.net_flow_total:.1f}")
        return stats

    def _parse_batch(self, data_batch: List[Any]) -> List[TransactionInfo]:
        transactions: List[TransactionInfo] = []
        for item in data_batch:
            if not isinstance(item, str) or ":" not in item:
                continue
            raw_action, raw_amount = item.split(":", 1)
            action = raw_action.strip().lower()
            if action not in {"buy", "sell"}:
                continue
            try:
                amount = float(raw_amount.strip())
            except ValueError:
                continue
            transactions.append({"action": action, "amount": amount})
        return transactions


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.error_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        # извлекаем только текстовые события для анализа
        events = [item for item in data_batch if isinstance(item, str)]
        if not events:
            raise ValueError("event batch has no textual events")

        print(f"Processing event batch: {events}")
        self.processed_count += len(events)

        # подсчитываем количество событий, содержащих слово "error"
        # (без учета регистра)
        errors = sum(1 for item in events if "error" in item.lower())
        self.error_count += errors
        # корректно формируем слово "error" в зависимости от количества ошибок
        label = "error" if errors == 1 else "errors"

        return (
            f"Event analysis: {len(events)} events, "
            f"{errors} {label} detected")

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria != "high_priority":
            return data_batch
        # фильтруем только события, содержащие слово "error"
        # (без учета регистра)
        return [
            item
            for item in data_batch
            if isinstance(item, str) and "error" in item.lower()]

    def get_stats(self) -> StreamStats:
        stats = super().get_stats()
        stats["stream_type"] = "event"
        stats["error_count"] = self.error_count
        return stats


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_stream(
        self,
        stream: DataStream,
        batch: List[Any],
        criteria: Optional[str] = None,
    ) -> str:
        try:
            filtered_batch = stream.filter_data(batch, criteria)
            return stream.process_batch(filtered_batch)
        except Exception:
            stream.failed_batches += 1
            safe_batch = [item for item in batch if isinstance(item, str)]

            if safe_batch == batch or not safe_batch:
                return (
                    f"Stream error ({stream.stream_id}): "
                    f"unable to process batch")

            try:
                return stream.process_batch(safe_batch)
            except Exception:
                stream.failed_batches += 1
                return (
                    f"Stream error ({stream.stream_id}): "
                    f"unable to process batch after recovery")

    def process_all(self, batches: List[List[Any]]) -> List[str]:
        if len(batches) != len(self.streams):
            raise ValueError("number of batches must match number of streams")
        return [
            self.process_stream(stream, batch)
            for stream, batch in zip(self.streams, batches)]


def data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    print("Initializing Sensor Stream...")
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    print(
        processor.process_stream(
            sensor,
            ["temp:22.5", "humidity:65", "pressure:1013"]))
    print()

    print("Initializing Transaction Stream...")
    print("Stream ID: TRANS_001, Type: Financial Data")
    print(
        processor.process_stream(
            transaction,
            ["buy:100", "sell:150", "buy:75"]))
    print()

    print("Initializing Event Stream...")
    print("Stream ID: EVENT_001, Type: System Events")
    print(processor.process_stream(event, ["login", "error", "logout"]))
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()

    mixed_batches = [
        ["temp:31.4", "temp:30.2"],
        ["buy:200", "sell:50", "sell:100", "buy:25"],
        ["login", "error", "logout"]]

    results = processor.process_all(mixed_batches)
    print()

    print("Batch 1 Results:")
    for result in results:
        print(f"- {result}")
    print()

    print("Stream filtering active: High-priority data only")
    sensor_alerts = sensor.filter_data(mixed_batches[0], "high_priority")
    large_transactions = transaction.filter_data(
        mixed_batches[1],
        "high_priority")
    print(
        f"Filtered results: {len(sensor_alerts)} critical sensor alerts, "
        f"{len(large_transactions)} large transaction")
    print()

    print("=== Stream Statistics ===")
    for stream in processor.streams:
        stats = stream.get_stats()
        print(f"{stats['stream_type']} ({stats['stream_id']}):")
        for key, value in stats.items():
            if key != "stream_id":
                print(f"  - {key}: {value}")
    print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
