class Human:
    def __init__(self,name):
        self.name = name

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self,human):
        self.passengers.append(human)
    def print_passengers_names(self):
        if self.passengers!=[]:
            print(f'Names of {self.brand} car passengers: ')
            for i in self.passengers:
                print(i.name)
        else:print(f'There are no passengers in {self.brand}, car')

artur = Human('Artur')
john = Human('John')
Ali = Human('Ali')

car = Auto(input('Car brand: '))
car.add_passenger(artur)
car.add_passenger(john)
car.add_passenger(Ali)
car.print_passengers_names()



#
# passengers = ['John', 'Hitler', 'Stalin']
# print(passengers)
# for i in passengers:
#     print(i)