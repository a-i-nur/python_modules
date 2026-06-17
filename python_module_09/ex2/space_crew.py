from datetime import datetime
from enum import Enum

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ModuleNotFoundError as error:
    raise SystemExit(
        "Pydantic 2.x is required.\n\n"
        "Create and activate a virtual environment:\n"
        "  python3 -m venv .venv\n"
        "  source .venv/bin/activate\n\n"
        "Install dependencies:\n"
        '  python -m pip install "pydantic>=2,<3"\n'
    ) from error


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(
            member.rank in {Rank.COMMANDER, Rank.CAPTAIN}
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_crew = sum(
                member.years_experience >= 5
                for member in self.crew
            )
            if experienced_crew < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need "
                    "50% experienced crew (5+ years)"
                )

        inactive_members = [
            member
            for member in self.crew
            if not member.is_active
        ]

        if inactive_members:
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    crew = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=42,
            specialization="Mission Command",
            years_experience=15,
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=35,
            specialization="Navigation",
            years_experience=8,
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=31,
            specialization="Engineering",
            years_experience=6,
        ),
    ]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.fromisoformat("2024-06-01T09:00:00"),
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )

    print("Space Mission Crew Validation")
    print("=" * 40)
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")

    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} "
            f"({member.rank.value}) - "
            f"{member.specialization}"
        )
    print()

    print("=" * 40)
    print("Expected validation error:")

    try:
        SpaceMission(
            mission_id="M2026_MOON",
            mission_name="Invalid Training Mission",
            destination="Moon",
            launch_date=datetime.fromisoformat("2024-07-01T09:00:00"),
            duration_days=30,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Aynur",
                    rank=Rank.LIEUTENANT,
                    age=32,
                    specialization="Navigation",
                    years_experience=7,
                ),
                CrewMember(
                    member_id="CM005",
                    name="Adelia",
                    rank=Rank.OFFICER,
                    age=32,
                    specialization="Engineering",
                    years_experience=5,
                ),
            ],
            budget_millions=500.0,
        )
    except ValidationError as error:
        first_error = error.errors()[0]

        if "ctx" in first_error and "error" in first_error["ctx"]:
            print(first_error["ctx"]["error"])
        else:
            print(first_error["msg"])


if __name__ == "__main__":
    main()
