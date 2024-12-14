class car:
    def __init__(self,brand,fuel_type):
        self.brand=brand
        self.fuel_type=fuel_type
    def car_details(self,millage):
         print(f"This is {self.brand}car and is {self.fuel_type}car and has a millage of{millage}kmph")
car1=Car(brand"benz",fuel_type"disel")
car2=car(brand"porsche",fuel_type"petrol")
car1.car_details(16)
car2.car_details(8)