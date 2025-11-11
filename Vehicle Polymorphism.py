class BMW:
    def fuel_type(self):
        print("The BMW uses Petrol as its fuel type.")

    def max_speed(self):
        print("The BMW has a maximum speed of 250 km/h.")

class Ferrari:
    def fuel_type(self):
        print("The Ferrari uses High-Octane Petrol as its fuel type.")

    def max_speed(self):
        print("The Ferrari has a maximum speed of 340 km/h.")
        
bmw_car = BMW()
ferrari_car = Ferrari()

for car in (bmw_car, ferrari_car):
    car.fuel_type()
    car.max_speed()