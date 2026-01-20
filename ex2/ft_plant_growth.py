class Plant:
    def __init__(self, name, height, plant_age):
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self):
        self.height += 1

    def age(self):
        self.plant_age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def main():
    day_1 = 25
    print("=== Day 1 ===")
    Rose = Plant("Rose", day_1, 30)
    Rose.get_info()
    for i in range(1, 7):
        Rose.age()
        Rose.grow()
    print(f"=== Day {i+1} ===")
    Rose.get_info()
    day_7 = Rose.height - day_1
    print(f"Growth this week: +{day_7}cm")


if __name__ == "__main__":
    main()
