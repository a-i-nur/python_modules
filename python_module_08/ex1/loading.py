import importlib


def analyze_matrix_data() -> None:
    print("Analyzing Matrix data...")

    pandas = importlib.import_module("pandas")
    numpy = importlib.import_module("numpy")
    requests = importlib.import_module("requests")
    pyplot = importlib.import_module("matplotlib.pyplot")

    seed = 42

    try:
        response = requests.get(
            "https://aisenseapi.com/services/v1/random_number/1/100000",
            timeout=5,
        )
        response.raise_for_status()
        seed = int(response.json()["random_number"])
        print(f"Mainframe seed received: {seed}")
    except Exception as e:
        print("Mainframe API status: unavailable")
        print(f"Error: {e}")
        print(f"Using fallback seed: {seed}")
    print()

    numpy.random.seed(seed)

    data_points = 1000
    signal_values = numpy.random.normal(loc=50, scale=10, size=data_points)

    print(f"Processing {data_points} data points...")

    matrix_data = pandas.DataFrame(
        {
            "signal_strength": signal_values,
        }
    )

    average_signal = matrix_data["signal_strength"].mean()
    maximum_signal = matrix_data["signal_strength"].max()
    minimum_signal = matrix_data["signal_strength"].min()

    print(f"Average signal strength: {average_signal:.2f}")
    print(f"Maximum signal strength: {maximum_signal:.2f}")
    print(f"Minimum signal strength: {minimum_signal:.2f}")

    print("Generating visualization...")
    print()

    pyplot.figure(figsize=(10, 6))
    pyplot.hist(matrix_data["signal_strength"], bins=30)
    pyplot.title("Matrix Signal Strength Distribution")
    pyplot.xlabel("Signal Strength")
    pyplot.ylabel("Frequency")
    pyplot.savefig("matrix_analysis.png")
    pyplot.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def check_dependencies(pkg_name: str, description: str) -> bool:
    try:
        pkg = importlib.import_module(pkg_name)
        version = getattr(pkg, "__version__", "unknown")
        print(f"[OK] {pkg_name} ({version}) - {description}")
        return True
    except ImportError:
        print(f"[MISSING] {pkg_name} - Please install this package.")
        return False


def main() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()

    print("Dependency management:")
    print("pip uses requirements.txt as a simple dependency list.")
    print(
        "Poetry uses pyproject.toml to manage dependencies and environments."
    )
    print()

    print("Checking dependencies:")
    packages = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
        ("requests", "Network access ready"),
        ("matplotlib", "Visualization ready"),
    ]

    missing_packages = []

    for pkg_name, description in packages:
        if not check_dependencies(pkg_name, description):
            missing_packages.append(pkg_name)

    print()

    if missing_packages:
        print("Missing dependencies detected.")
        print("Install them with pip:")
        print("pip install -r requirements.txt")
        print()
        print("Or install them with Poetry:")
        print("poetry install")
        return

    analyze_matrix_data()


if __name__ == "__main__":
    main()
