class SecurePlant:
    def __init__(self, name, height, plant_age):
        self.__name = name
        self.__height = height
        self.__plant_age = plant_age

    def set_height(self, value):
        self.__height = value

    def set_age(self, value):
        self.__age = value

    def get_height(self, value):
        return self.__height

    def get_age(self, value):
        return self.__age
