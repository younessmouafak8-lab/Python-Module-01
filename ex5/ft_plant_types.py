class Plant:
    """
    The blueprint for generating Plants,
    and a parent class which we will inherit from
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        setting the values of the object's attributes
        """
        self.name = name
        self.age = age
        self.height = height

    def known_info(self) -> str:
        """
        returns the plant's infos
        """
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    """
    Another blueprint, that inherits from the Plant class (parent)
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        setting the values of the object's attributes through calling
        the parent's constructor
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """
        prints the plant's ability to bloom
        """
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        """
        prints the plant's infos
        """
        print(f"{self.known_info()}, {self.color}")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: int, age: int, trunk_diameter: int) -> None:
        """
        setting the values of the object's attributes through calling
        the parent's constructor, and adding unique attributes
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        prints the shade produced by the Tree
        """
        radius = self.height / 100
        shade_area = 3.14 * (radius ** 2)
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def get_info(self) -> None:
        """
        prints the plant's infos
        """
        print(f"{self.known_info()}, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Another blueprint, that inherits from the Plant class (parent)
    """
    def __init__(self,
                 name: str,
                 height: int, age: int, harvest_season: str) -> None:
        """
        setting the values of the object's attributes through calling
        the parent's constructor, and adding unique attributes
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritional_value(self) -> None:
        """
        prints nutritional value of the vegetable
        """
        print(f"{self.name} is rich in vitamin C")

    def get_info(self) -> None:
        """
        prints the plant's infos
        """
        print(f"{self.known_info()}, {self.harvest_season}")


def main() -> None:
    print("=== Garden Plant Types ===")
    plants = [
                Flower("Rose", 25, 30, "red color"),
                Flower("Sunflower", 35, 40, "yellow color"),
                Tree("Oak", 500, 1825, 50),
                Tree("Centurion", 600, 2000, 60),
                Vegetable("Tomato", 80, 90, "summer harvest"),
                Vegetable("Potato", 50, 80, "winter harvest"),
            ]

    for plant in plants:
        plant_type = plant.__class__.__name__
        print(f"\n{plant.name} ({plant_type}): ", end="")
        plant.get_info()
        if plant_type == "Tree":
            plant.produce_shade()
        elif plant_type == "Vegetable":
            plant.nutritional_value()
        else:
            plant.bloom()


if __name__ == "__main__":
    main()
