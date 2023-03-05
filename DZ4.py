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




# class Human:
#     def __init__(self,name,age,surname):
#         self.name = name
#         self.__age = age
#         self.surname = surname
#     def show_info(self):
#         print("name:",self.name)
#         print("age:",self.__age)
#         print("surname:",self.surname)
#
#     def get_change(self):
#         return self.__age
#     def set_change(self,age):
#         self.__age = age
#
# human = Human("name","age","surname")
# human.show_info()
# # print(human.get_change())
# print(''
#       '')
# human.set_change(60)
# human.show_info()