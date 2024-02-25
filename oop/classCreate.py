class Car:
    def __init__(self,brand,model):
        self.brand  = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} : {self.model}"
    
# Ineritance 

class ElectricCar(Car):
    def __init__(self, brand, model,battary_size):
        super().__init__(brand, model)
        self.battary_size = battary_size

# Inheritance
tesla  = ElectricCar("Tesla","Tesla-Model-2","5000 kWh")
print(f"{tesla.brand} : {tesla.model} : {tesla.battary_size}")
print(tesla.full_name())


# mycar = Car("Yogesh","2002")
# print(mycar.model,":",mycar.brand)
# print(mycar.full_name())
    