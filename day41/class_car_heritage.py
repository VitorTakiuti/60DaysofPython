class Vehicle:
    def __init__(self, brand, model, max_speed):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
    
    def start_engine(self):
        print(f"Car was started, the model is {self.model} and the brand is {self.brand}!")
        
    def acceleration(self):
        print(f"The {self.model} is accelerating to reach the maximum speed that is {self.max_speed}!")
        
    def turn_on_lights(self):
        print(f"The {self.model} of {self.brand} turned on the lights")
        
class Car(Vehicle):
    def __init__(self, brand, model, max_speed, doors):
        super().__init__(brand, model, max_speed)
        self.doors = doors
        
    def open_doors(self):
        print(f"The {self.doors} doors of the model {self.model}/{self.brand} are open" )

#Testing the code

#my_vehicle = Vehicle(brand="Honda", model="Civic", max_speed=280)
#my_vehicle.acceleration()
#my_vehicle.start_engine()

my_car = Car(brand="Honda", model="Civic", max_speed=280, doors=4)
my_car.acceleration()
my_car.start_engine()
my_car.turn_on_lights()
my_car.open_doors()