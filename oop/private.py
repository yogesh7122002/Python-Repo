class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    def full_name(self):
        return f"{self.__brand} : {self.model}"
    
    def get_brand(self):
        return self.__brand
    def fueltype(self):
        return "Petrol or Disel"

class ElectricCar(Car):
    def __init__(self, brand, model,battary_size):
        super().__init__(brand, model)
        self.battary_size = battary_size
        
    def fueltype(self):
        return "Electric"
        

tesla = ElectricCar("Tesla","any","123 kWh")
print(tesla.get_brand()) # but we have to make this attribute private
print(tesla.fueltype())

Aura = Car("Hundai","aura")
print("The Fuel type of Aura is",Aura.fueltype()) 
        
# tesla  = ElectricCar("Tesla","Tesla-Model-2","5000 kWh")
# print(f"{tesla.brand} : {tesla.model} : {tesla.battary_size}")
# print(tesla.full_name())

