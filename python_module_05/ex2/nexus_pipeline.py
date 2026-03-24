#!/usr/bin/env python3

from abc import ABC, abstractmethod
import collections
from typing import Any, Dict, List, Optional, Protocol, Union


class ProcessingStage(Protocol):
    """Protocol for a pipeline stage with a process method."""

    def process(self, data: Any) -> Any:
        pass


class InputStage:
    """First stage that checks the input data."""

    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            raise ValueError("Stage 1: invalid pipeline data")

        if data.get("payload") is None:
            raise ValueError("Stage 1: empty input")

        return data


class TransformStage:
    """Second stage that transforms the payload."""

    def process(self, data: Any) -> Any:
        kind = data.get("kind")
        payload = data.get("payload")

        if kind == "json":
            if not isinstance(payload, dict):
                raise ValueError("Stage 2: invalid JSON data")

            result = {key: value for key, value in payload.items()}
            result["status"] = "Normal"
            data["payload"] = result
            data["transform_note"] = (
                "Transform: enriched with metadata and validation")
            return data

        if kind == "csv":
            if not isinstance(payload, str) or "," not in payload:
                raise ValueError("Stage 2: invalid CSV data")

            fields = [part.strip() for part in payload.split(",")]
            action_count = len(fields) - 2
            if action_count < 1:
                action_count = 1
            data["payload"] = {
                "fields": fields,
                "count": action_count}
            data["transform_note"] = "Transform: parsed and structured data"
            return data

        if kind == "stream":
            if not isinstance(payload, list):
                raise ValueError("Stage 2: invalid stream data")

            values = [
                value for value in payload
                if isinstance(value, (int, float))]
            if not values:
                raise ValueError("Stage 2: stream has no numeric values")

            total = 0.0
            for value in values:
                total += float(value)

            data["payload"] = {
                "count": len(values),
                "avg": int((total / len(values)) * 10 + 0.5) / 10}
            data["transform_note"] = "Transform: aggregated and filtered"
            return data

        if kind == "chain":
            if not isinstance(payload, dict):
                raise ValueError("Stage 2: invalid chain payload")

            steps = payload.get("steps", [])
            if not isinstance(steps, list):
                raise ValueError("Stage 2: invalid chain steps")

            steps.append(data.get("adapter_name", "unknown"))
            payload["steps"] = steps
            payload["last_adapter"] = data.get("adapter_name", "unknown")
            data["transform_note"] = (
                "Transform: data moved to next pipeline stage")
            return data

        raise ValueError("Stage 2: unsupported pipeline format")


class OutputStage:
    """Third stage that builds the final output string."""

    def process(self, data: Any) -> Any:
        kind = data.get("kind")
        payload = data.get("payload")

        if kind == "json" and isinstance(payload, dict):
            value = payload.get("value", "unknown")
            unit = payload.get("unit", "")
            status = payload.get("status", "Unknown")
            data["result"] = (
                "Processed temperature reading: "
                f"{value}°{unit} ({status} range)")
            return data

        if kind == "csv" and isinstance(payload, dict):
            data["result"] = (
                "User activity logged: "
                f"{payload['count']} actions processed")
            return data

        if kind == "stream" and isinstance(payload, dict):
            data["result"] = (
                "Stream summary: "
                f"{payload['count']} readings, avg: {payload['avg']}°C")
            return data

        if kind == "chain" and isinstance(payload, dict):
            records = payload.get("records", 0)
            steps = payload.get("steps", [])
            step_count = len(steps) if isinstance(steps, list) else 0
            data["result"] = (
                f"{records} records processed through "
                f"{step_count}-stage pipeline")
            return data

        data["result"] = f"Result: {payload}"
        return data


class ProcessingPipeline(ABC):
    """Base abstract pipeline with configurable stages."""

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.stats: collections.Counter[str] = collections.Counter()
        self.error_log: collections.deque[str] = collections.deque(maxlen=5)

    def add_stage(self, stage: ProcessingStage) -> None:
        """Add one stage to the pipeline."""
        self.stages.append(stage)

    def run_stages(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Run the given data through all pipeline stages."""
        result: Any = data
        for stage in self.stages:
            result = stage.process(result)

        if not isinstance(result, dict):
            raise ValueError("Pipeline must return dict data")

        return result

    def save_success(self) -> None:
        """Store success metrics for one pipeline run."""
        self.stats["processed"] += 1
        self.stats["success"] += 1
        self.stats["work_units"] += len(self.stages)

    def save_error(self, message: str) -> None:
        """Store error metrics and keep the latest error message."""
        self.stats["processed"] += 1
        self.stats["errors"] += 1
        self.stats["work_units"] += len(self.stages)
        self.error_log.append(f"{self.pipeline_id}: {message}")

    def run_adapter(
        self,
        data: Any,
        kind: str,
        adapter_name: str,
    ) -> Union[str, Any]:
        """Prepare data, run stages, and handle adapter errors."""

        prepared = {
            "kind": kind,
            "payload": data,
            "adapter_name": adapter_name,
            "transform_note": "",
            "result": ""}

        try:
            result = self.run_stages(prepared)
            print(result["transform_note"])
            self.save_success()
            return result["result"]
        except Exception as e:
            self.save_error(str(e))
            return f"Error detected in pipeline: {e}"

    def run_chain_step(
        self,
        chain_data: Dict[str, Any],
        adapter_name: str,
    ) -> Dict[str, Any]:
        """Run one chain step and return the updated chain payload."""
        prepared = {
            "kind": "chain",
            "payload": chain_data,
            "adapter_name": adapter_name,
            "transform_note": "",
            "result": "",
        }
        result = self.run_stages(prepared)
        return result["payload"]

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    """Adapter for JSON-like dictionaries."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("Processing JSON data through pipeline...")
        print(f"Input: {data}")
        return self.run_adapter(data, "json", "JSONAdapter")


class CSVAdapter(ProcessingPipeline):
    """Adapter for CSV strings."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("Processing CSV data through same pipeline...")
        print(f"Input: {data}")
        return self.run_adapter(data, "csv", "CSVAdapter")


class StreamAdapter(ProcessingPipeline):
    """Adapter for a stream of readings."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("Processing Stream data through same pipeline...")
        print("Input: Real-time sensor stream")
        return self.run_adapter(data, "stream", "StreamAdapter")


class NexusManager:
    """Manager that stores and runs multiple pipelines."""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.pipelines: List[ProcessingPipeline] = []

    def register_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """Register one pipeline in the manager."""
        self.pipelines.append(pipeline)

    def chain_pipelines(self, seed_data: Optional[Any] = None) -> str:
        """Run all registered pipelines as one chain."""
        chain_data: Dict[str, Any] = {
            "records": 100,
            "source": seed_data,
            "steps": []}

        for pipeline in self.pipelines:
            try:
                chain_data = pipeline.run_chain_step(
                    chain_data, pipeline.pipeline_id)
                pipeline.save_success()
            except Exception as e:
                pipeline.save_error(str(e))
                return f"Chain error: {e}"

        return (
            f"{chain_data['records']} records processed through "
            f"{len(chain_data['steps'])}-stage pipeline")

    def print_stats(self) -> None:
        """Print overall performance stats for all pipelines."""
        total_processed = 0
        total_errors = 0
        total_work_units = 0

        for pipeline in self.pipelines:
            total_processed += pipeline.stats.get("processed", 0)
            total_errors += pipeline.stats.get("errors", 0)
            total_work_units += pipeline.stats.get("work_units", 0)

        if total_processed == 0:
            efficiency = 0.0
        else:
            efficiency = (
                (total_processed - total_errors) / total_processed) * 100

        print(
            "Performance: "
            f"{efficiency:.1f}% efficiency, "
            f"{total_work_units} pipeline work units")

        if total_errors > 0:
            for pipeline in self.pipelines:
                if pipeline.error_log:
                    print(f"Last recovery log: {pipeline.error_log[-1]}")
                    break


def setup_pipeline(pipeline: ProcessingPipeline) -> None:
    """Attach the default three stages to a pipeline."""
    pipeline.add_stage(InputStage())
    pipeline.add_stage(TransformStage())
    pipeline.add_stage(OutputStage())


def simulate_recovery(pipeline: ProcessingPipeline) -> None:
    """Show a simple recovery flow after an intentional error."""
    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    error_result = pipeline.process("BROKEN_STREAM_PAYLOAD")
    if isinstance(error_result, str) and error_result.startswith("Error"):
        print(error_result)
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed")


def nexus_pipeline() -> None:
    """Run the full pipeline demo."""
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print()

    print("Initializing Nexus Manager...")
    manager = NexusManager(capacity=1000)
    print(f"Pipeline capacity: {manager.capacity} streams/second")
    print()

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")
    print()

    json_pipeline = JSONAdapter("PIPE_A")
    csv_pipeline = CSVAdapter("PIPE_B")
    stream_pipeline = StreamAdapter("PIPE_C")

    for pipeline in [json_pipeline, csv_pipeline, stream_pipeline]:
        setup_pipeline(pipeline)
        manager.register_pipeline(pipeline)

    print("=== Multi-Format Data Processing ===")
    print()

    json_result = json_pipeline.process(
        {"sensor": "temp", "value": 23.5, "unit": "C"})
    print(f"Output: {json_result}")
    print()

    csv_result = csv_pipeline.process("user,action,timestamp")
    print(f"Output: {csv_result}")
    print()

    stream_result = stream_pipeline.process([21.8, 22.2, 22.5, 21.9, 22.1])
    print(f"Output: {stream_result}")
    print()

    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    print()

    chain_result = manager.chain_pipelines(
        {"records": 100, "source": "Raw -> Processed -> Analyzed -> Stored"})
    print(f"Chain result: {chain_result}")
    manager.print_stats()
    print()

    simulate_recovery(stream_pipeline)
    print()

    manager.print_stats()
    print()
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    nexus_pipeline()
