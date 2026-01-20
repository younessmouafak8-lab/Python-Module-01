class Plant:
    def __init__(self, name, height, plant_age):
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def get_info(self):
        print(f"{self.name} ({self.height}cm, {self.plant_age} days old)")


def main():
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


if __name__ == "__main__":
    main()
