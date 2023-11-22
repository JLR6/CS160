#laisons -Henry and Henry, synch - Jenny, reflector - Shireen
class Car:
    def __init__(self, model_name = "None assigned", doors =4, passengers = 5):
        self.make_model = model_name
        self.num_doors = doors
        self.max_passengers = passengers

    def set_make_model(self, model):
        self.make_model = model

    def get_make_model(self):
        return (self.make_model)
    
    def set_num_doors(self, number):
        self.num_doors = number

    def get_num_doors(self):
        return(self.num_doors)
    
    def set_max_passengers(self, number):
        self.max_passengers = number
    
    def get_max_passengers(self):
        return(self.max_passengers)
    
    def __str__(self):
        stringToReturn = "Make and Model: " + self.get_make_model() + "\n" + "Number of doors: " + str(self.get_num_doors()) + "\n" + "Maximum number of passengers: " + str(self.get_max_passengers())
        return(stringToReturn)


if __name__ =="__main__":
    car1 = Car()
    car1.set_make_model("Dodge Dart")
    car1.set_num_doors(5)
    car1.set_max_passengers(7)
    print(car1.get_make_model())
    print(car1.get_num_doors())
    print(car1.get_max_passengers())
    print(car1)