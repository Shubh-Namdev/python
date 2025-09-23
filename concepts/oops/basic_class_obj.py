
class Car :

    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    @staticmethod
    def car_description() :
        return "car description"

    def get_brand(self) :
        return self.__brand
    
    @property
    def model(self) :
        return self.__model

    def full_name(self) :
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self) :
        return "Petrol/Diesel"
    


car = Car("Tata", "Safari")
# print(car.brand)
# print(car.model)
# print(car.full_name())


class ElectricCar(Car) :

    def __init__(self, brand, model, battery_size) :
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electricity"


tesla = ElectricCar("Tesla", "Model S", "80kwh")
# print(tesla.full_name())
# print(tesla.get_brand())

#polymorphism
# print(car.fuel_type())
# print(tesla.fuel_type())

#class variable
print(Car.total_cars)
print(car.car_description())
print(tesla.car_description())

#decorators
print(car.model)

print(isinstance(car, Car))
print(isinstance(tesla, Car))