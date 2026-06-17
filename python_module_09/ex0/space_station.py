from datetime import datetime

try:
    from pydantic import BaseModel, Field, ValidationError
except ModuleNotFoundError as error:
    raise SystemExit(
        "Pydantic 2.x is required.\n\n"
        "Create and activate a virtual environment:\n"
        "  python3 -m venv .venv\n"
        "  source .venv/bin/activate\n\n"
        "Install dependencies:\n"
        '  python -m pip install "pydantic>=2,<3"\n'
    ) from error


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(max_length=200, default=None)


def main() -> None:
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.fromisoformat("2226-05-08T12:00:00"),
    )

    print("Space Station Data Validation")
    print("=" * 40)

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(
        "Status: "
        f"{'Operational' if station.is_operational else 'Not operational'}"
    )
    print()

    print("=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Invalid Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2226-05-08T12:00:00"),
        )
    except ValidationError as error:
        print(error.errors()[0]['msg'])


if __name__ == "__main__":
    main()
