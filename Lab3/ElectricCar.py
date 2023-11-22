import Car
class ElectricCar(Car.Car):
    def __init__(self, make_model = "None assigned", num_doors = 4, max_passengers = 5):
        super().__init__( make_model, num_doors, max_passengers)
    def __str__(self) -> str:
        return(str(super().__str__())+ "\nELECTRIC CAR")
        
if __name__=="__main__":
     electricCar1 = ElectricCar()
     print(electricCar1)
     electricCar1.set_make_model("Toyota Prius")
     print(electricCar1)
