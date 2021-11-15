#Jaden
#11/12/2021
# This program prints  out the name, make, model, color, and type of car.
class car:

    def __init__(self, model, year, color, type, manufacturer):
         self.model = model
         self.year = year
         self.color = color
         self.type = type
         self.manufacturer = manufacturer

    def get_type(self):
        return self.type

    def get_model(self):
         return self.model

    def get_year(self):
         return self.year

    def get_color(self):
         return self.color

    def fullspecs(self):
         return self.model + ' ' + str(self.year) + ' ' + self.color + '  ' + self.type + ' '+ self.manufacturer

car1 = car("Mustang GT", 2021, "Blue", "Sports", "Ford")
car2 = car("Demon", 2018, "Black", "Sports", "Dodge")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())