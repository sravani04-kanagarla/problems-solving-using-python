class vehicle:
    def start(self):
        print("vehicle has started")
class Car(vehicle):
    def drive(self):
        print("Car is driving")
car = Car
car.start()
car.drive()