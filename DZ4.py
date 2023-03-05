class Person:
    def __init__(self,age,height,weight):
        self.age = age
        self.__height = height
        self.weight = weight
    def show_info(self):
        print("Age: ",self.age)
        print("Height: ",self.__height)
        print("Weight: ",self.weight)

    def get_change(self):
        return self.__height

    def set_change(self,age,height,weight):
            self.age = age
            self.__height = height
            self.weight = weight


Person1 = Person("Mercedes W140","W8",1999)
Person1.show_info()

# print(car1.get_change())
print(''
      '')
Person1.get_change()
print(Person1.get_change())




