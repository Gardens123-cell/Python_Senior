class Student:
 #атрибут(name,surname,age)
 #Методы(def(display_name))
 #Функция внутри класса - метод
    name = 'Cavid'
    surname = 'Abdulzade'
    age = 18

    def display_info(self):
        print("Your name is: ",self.name)
        print("Your surname is: ",self.surname)
        print("Your age is: ",self.age)

student1=Student()

student1.display_info()
print(""
      "")
student2=Student()

student2.name = 'Ali'
student2.surname = 'Huseynzade'
student2.age = 14
student2.display_info()



print(""
      "")
print("class with init(2nd method)")
print(""
      "")

class Student2:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def display_info(self):
        print("Your name is: ", self.name)
        print("Your surname is: ", self.surname)
        print("Your age is: ", self.age)

student1 = Student2('Ali','Huseynzade',100)
student1.display_info()

student2 = Student2('Nadir','Dadashzade',101)
student2.display_info()

student3 = Student2('Ibo','Mirhashimov',102)
student3.display_info()



