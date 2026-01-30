class SecurePlant:
    """
    The blueprint for generating Plants,
    secured plants to be percise
    """
    def __init__(self, name: str) -> None:
        """
        setting the values of the object's attributes,
        making them private.
        """
        self.__name = name
        self.__height = 0
        self.__age = 0

    def set_height(self, value: int) -> None:
        """
        a function that evaluates the height value entered as input.
        before assigning them to the attributes
        """
        if value < 0:
            print(
                f"\nInvalid operation attempted: "
                f"height {value}cm [REJECTED]"
                )
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        """
        a function that evaluates the age value entered as input.
        before assigning them to the attributes
        """
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"age updated: {value} days [OK]")

    def get_height(self) -> int:
        """
        a function that returns the height of the plant
        """
        return self.__height

    def get_age(self) -> int:
        """
        a function that returns the age of the plant
        """
        return self.__age

    def get_info(self) -> None:
        """
        prints the plant's infos
        """
        print(f"{self.__name} ({self.__height}cm, {self.__age} days old)")


def main() -> None:
    Plants = ["Rose", 15, 20]
    print("=== Garden Security System ===")
    Rose = SecurePlant("Rose")
    print("Plant created:", Plants[0])
    Rose.set_height(25)
    Rose.set_age(30)
    Rose.set_height(-5)
    print("\nCurrent plant: ", end="")
    Rose.get_info()


if __name__ == "__main__":
    main()
