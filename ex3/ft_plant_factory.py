class Plant:
    """
    The blueprint for generating Plants
    """
    counter = 0

    def __init__(self, name: str, height: int, plant_age: int) -> None:
        """
        setting the values of the object's attributes
        """
        self.name = name
        self.height = height
        self.plant_age = plant_age
        Plant.counter += 1

    def get_info(self) -> None:
        """
        prints the plant's infos
        """
        print(f"{self.name} ({self.height}cm, {self.plant_age} days old)")


def main() -> None:
    Plants = [("Rose", 25, 30),
              ("Oak", 200, 365),
              ("Cactus", 5, 90),
              ("Sunflower", 80, 45),
              ("Fern", 15, 120)
              ]
    for name, height, age in Plants:
        current = Plant(name, height, age)
        print("Created: ", end="")
        current.get_info()
    print("\nTotal plants created:", Plant.counter)


if __name__ == "__main__":
    main()
