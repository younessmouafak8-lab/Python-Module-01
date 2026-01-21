class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        print(f"{self.height}cm, {self.age} days old, {self.color}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        radius = self.height / 100
        shade_area = 3.14 * (radius ** 2)
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def get_info(self):
        print(
            f"{self.height}cm, {self.age} days old, "
            f"{self.trunk_diameter}cm diameter"
            )


class Vegtable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(self, name, height, age)
        self.harvest_season = harvest_season

    def nutritional_value(self):
        print(f"{self.name} is rich in vitamin C")

    def get_info(self):
        print(f"{self.height}cm, {self.age} days old, {self.harvest_season}")


def main():
    print("=== Garden Plant Types ===")
    Rose = Flower("Rose", 25, 30, "red color")
    print(f"\n{Rose.name} ({Rose.__class__.__name__}): ", end="")
    Rose.get_info()
    Rose.bloom()
    Oak = Tree("Oak", 500, 1825, 50)
    print(f"\n{Oak.name} ({Oak.__class__.__name__}): ", end="")
    Oak.get_info()
    Oak.produce_shade()


if __name__ == "__main__":
    main()
