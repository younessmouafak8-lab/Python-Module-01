class Plant:
    """
    The blueprint for generating Plants
    """
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        """
        setting the values of the object's attributes
        """
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self, value: int) -> None:
        """
        a function that increaments the plant's height by the given value
        """
        self.height += value

    def age(self, value: int) -> None:
        """
        a function that increaments the plant's age by the given value
        """
        self.plant_age += value

    def get_info(self) -> None:
        """
        prints the plant's infos
        """
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def main() -> None:
    day_1 = 25
    print("=== Day 1 ===")
    Rose = Plant("Rose", day_1, 30)
    Rose.get_info()
    for i in range(1, 7):
        Rose.age(1)
        Rose.grow(1)
    print(f"=== Day {i+1} ===")
    Rose.get_info()
    day_7 = Rose.height - day_1
    print(f"Growth this week: +{day_7}cm")


if __name__ == "__main__":
    main()
