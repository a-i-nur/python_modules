import sys
# os - Provides a way of using operating
# system dependent functionality,
# such as file paths and environment variables.
import os
# site - Provides access to the site-packages directory,
# where third-party packages are installed.
import site


def display_current_environment_info() -> None:
    # sys.executable gives the path
    # to the Python interpreter being used
    print(f"Current Python: {sys.executable}")


def show_outside_matrix() -> None:
    print()
    print("MATRIX STATUS: You're still plugged in")
    print()

    display_current_environment_info()
    print("Virtual Environment: None detected")
    print()

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print()

    print("Then run this program again.")


def show_inside_construct() -> None:
    print()
    print("MATRIX STATUS: Welcome to the construct")
    print()

    display_current_environment_info()
    # os.path.basename(sys.prefix) gives
    # the name of the virtual environment
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print()

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()

    # site.getsitepackages() returns
    # a list of all global site-packages directories
    # site.getusersitepackages() returns
    # the user-specific site-packages directory
    print("Package installation path:")
    for i, package_path in enumerate(site.getsitepackages()):
        if i == 0:
            print(package_path)


def is_virtual_environment() -> bool:
    # Check if we're in a virtual environment
    # sys.prefix is the path to the current Python environment
    # sys.base_prefix is the path to the base Python installation
    is_venv = sys.prefix != sys.base_prefix
    return is_venv


def main() -> None:
    if is_virtual_environment():
        show_inside_construct()
    else:
        show_outside_matrix()


if __name__ == "__main__":
    main()
