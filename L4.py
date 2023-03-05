# class Car:
#     def __init__(self,model,engine,year):
#         self.__model = model
#         self.engine = engine
#         self.year = year
#     def show_info(self):
#         print("Model: ",self.__model)
#         print("Engine: ",self.engine)
#         print("Year: ",self.year)
# car1 = Car("Mercedes W140","W8",1999)
# car1.show_info()

#свойства изменения аттрибута это - get() называется геттер
#для изменения значения аттрибута это -set() называется сеттер

class Car:
    def __init__(self,model,engine,year):
        self.__model = model
        self.__engine = engine
        self.__year = year
    def show_info(self):
        print("Model: ",self.__model)
        print("Engine: ",self.__engine)
        print("Year: ",self.__year)

    def get_change(self):
        return self.__model

        return self.__engine

    def set_change(self,model,engine,year):
            self.__model = model
            self.__year = year
            self.__engine = engine


car1 = Car("Mercedes W140","W8",1999)
car1.show_info()

# print(car1.get_change())
print(''
      '')
car1.set_change("Prius","Hybrid", 2008)
car1.show_info()

