class GardenManager:
    """ Blueprint that manages multipe garden """
    counter = 0
    gardens: list = []

    def __init__(self, name: str):
        """ storing the gardens name, and counting the added gardens
            then creaing the gradens list """
        self.name = name
        self.garden_stats = self.GardenStats(self)
        GardenManager.counter += 1
        GardenManager.create_garden_network(self)

    class GardenStats:
        """ the nested class that manages the statistics part,
        also adding and keeping track of the plants of each garden"""
        def __init__(self, owner: object) -> None:
            """
            the garndens required values, list of the plants,
            counting each added plant and marking their types
            """
            self.plants: list = []
            self.outer = owner
            self.plants_counter = 0
            self.growth = 0
            self.type_regular = 0
            self.type_fl = 0
            self.type_prize = 0

        def add_plant(self, plant: object, print_it: int = 1) -> None:
            """
            adding the plant and counting each types number
            then displaying a message when demanded
            """
            if print_it:
                print(
                        f"Added {plant.name} to "
                        f"{self.outer.name.capitalize()}'s garden"
                        )
            self.plants += [plant]
            self.plants_counter += 1
            if plant.type == "regular":
                self.type_regular += 1
            elif plant.type == "flowering":
                self.type_fl += 1
            else:
                self.type_prize += 1

        def report(self) -> None:
            """
            displaying a report for the garden
            """
            print()
            print(f"=== {self.outer.name.capitalize()}'s Garden Report ===")
            print("Plants in garden:")
            for plant in self.plants:
                print(plant.display())

        def growing_plants(self, value: int = 1) -> None:
            """
            growing the gardens plant by the give value (usualy 1)
            """
            print(
                    f"{self.outer.name.capitalize()} "
                    f"is helping all plants grow..."
                  )
            for plant in self.plants:
                plant.grow(value)
                self.growth += value

        def results(self) -> None:
            """
            printing the results after adding and growing,
            and counting the types
            """
            print()
            print(f"Plants added: {self.plants_counter}, "
                  f"Total growth {self.growth}cm")
            print(f"Plant types: {self.type_regular} regular, {self.type_fl} "
                  f"flowering, {self.type_prize} prize flowers")

        def height_check(self) -> str:
            """
            checking if the height of each plant is valid
            """
            print()
            for plant in self.plants:
                if plant.height < 0:
                    return "False"
            return "True"

        def scores(self) -> int:
            """
            counting the score of the garden
            """
            counter = 0
            for plant in self.plants:
                counter += plant.height
                if plant.type == "prize flowers":
                    counter += plant.points * 4
            return counter

        @staticmethod
        def Total_managed() -> None:
            """
            displaying the number of managed gardens
            """
            print("Total gardens managed:", GardenManager.counter)

    @classmethod
    def create_garden_network(cls, garden: object) -> None:
        """
        adding each garden to the network
        """
        GardenManager.gardens += [garden]


class Plant:
    """
    The blueprint for generating Plants,
    and a parent class
    """
    def __init__(self, name: str, height: int) -> None:
        """
            initializing the plant's values
        """
        self.name = name
        self.height = height
        self.type = "regular"

    def grow(self, value: int) -> None:
        """
        growing the plant with a given value
        (by default set to 1 if none is given)
        """
        self.height += value
        print(f"{self.name} grew {value}cm")

    def display(self) -> str:
        """
        returns the plant's values
        """
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    a Blueprint that inherits form the previous class
    adding unique attributes
    """
    def __init__(self, name: str, height: int, state: str) -> None:
        """
        initializing the plant's values,
        calling super() to use the parent's constructor (__init__)
        """
        super().__init__(name, height)
        self.state = state
        self.type = "flowering"

    def display(self) -> str:
        """
        returns the plant's values
        """
        return f"{super().display()}, {self.state}"


class PrizeFlower(FloweringPlant):
    """
    a Blueprint that inherits form the previous class
    adding unique attributes
    """
    def __init__(self, name: str, height: int, state: str, points: int) -> None:
        """
        initializing the plant's values,
        calling super() to use the parent's constructor (__init__)
        """
        super().__init__(name, height, state)
        self.points = points
        self.type = "prize flowers"

    def display(self) -> str:
        """
        returns the plant's values
        """
        return f"{super().display()}, Prize points: {self.points}"


def main():
    print("=== Garden Management System Demo ===")
    print()
    alice = GardenManager("alice")
    Bob = GardenManager("bob")
    plants = [Plant("Oak Tree", 100),
              FloweringPlant("Rose", 25, "red flowers (blooming)"),
              PrizeFlower("Sunflower", 50, "yellow flowers (blooming)", 10),
              ]
    Bob_plant = PrizeFlower("Sunflower", 52, "yellow flowers (blooming)", 10)
    for plant in plants:
        alice.garden_stats.add_plant(plant)
    print()
    alice.garden_stats.growing_plants()
    alice.garden_stats.report()
    alice.garden_stats.results()
    print("Height validation test:", alice.garden_stats.height_check())
    Bob.garden_stats.add_plant(Bob_plant, 0)
    print(f"Garden scores - {alice.name.capitalize()}: "
          f"{alice.garden_stats.scores()}, Bob: {Bob.garden_stats.scores()}")
    GardenManager.GardenStats.Total_managed()


if __name__ == "__main__":
    main()
