class SecurePlant:
    def __init__(self, name, height, plant_age):
        self.__name = name
        self.__height = height
        self.__plant_age = plant_age

    def set_height(self, value):
        if value < 0:
            print(
                f"\nInvalid operation attempted: "
                f"height {value}cm [REJECTED]"
                )
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value):
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"age updated: {value} days [OK]")

    def get_height(self, value):
        return self.__height

    def get_age(self, value):
        return self.__age

    def get_info(self):
        print(f"{self.__name} ({self.__height}cm, {self.__age} days old)")


def main():
    Plants = ["Rose", 15, 20]
    print("=== Garden Security System ===")
    Rose = SecurePlant("Rose", 15, 20)
    print("Plant created:", Plants[0])
    Rose.set_height(25)
    Rose.set_age(30)
    Rose.set_height(-5)
    print("\nCurrent plant: ", end="")
    Rose.get_info()


if __name__ == "__main__":
    main()
