import alchemy
import alchemy.elements


def main() -> None:
    print()
    print("=== Sacred Scroll Mastery ===")
    print()

    print("Testing direct module access:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())
    print()

    print("Testing package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_fire():", alchemy.create_fire())
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed")

    try:
        print("alchemy.create_water():", alchemy.create_water())
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")

    try:
        print("alchemy.create_earth():", alchemy.create_earth())
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print("alchemy.create_air():", alchemy.create_air())
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    # alternative way to test package-level access using getattr()
    # try:
    #     create_earth = getattr(alchemy, "create_earth")
    #     print("alchemy.create_earth():", create_earth())
    # except AttributeError:
    #     print("alchemy.create_earth(): AttributeError - not exposed")
    # try:
    #     create_air = getattr(alchemy, "create_air")
    #     print("alchemy.create_air():", create_air())
    # except AttributeError:
    #     print("alchemy.create_air(): AttributeError - not exposed")

    print()
    print("Package metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    main()
