class Car:
    car_year = 2000

    def car(self):
        print("Car's model: ",self.model)
        print("Car's color: ",self.color)
        print("Car's color: ",self.engine)



class Car2(Car):
    car_year = 2010

    def car(self):
        print("Car's model: ",self.model)
        print("Car's color: ",self.color)
        print("Car's color: ",self.engine)



car1 = Car()
print(car1.car_year)
car1.model = input("Enter car's model: ")
car1.color = input("Enter car's color: ")
car1.engine =input("Enter car's engine: ")
print('1st car:'
      '')
car1.car()

print(''
      '')

car2 = Car2()
print(car2.car_year)
car2.model = input("Enter 2nd car's model: ")
car2.color = input("Enter 2nd car's color: ")
car2.engine = input("Enter 2nd car's engine: ")
print('2nd car:'
      '')
car2.car()












