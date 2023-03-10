class Person:
    quntity = 0
    def __init__(self,age,height,weight):
        self.age = age
        self.height = height
        self.weight = weight
        Person.quntity+=1
    def show_info(self):
        print("Age: ",self.age)
        print("Height: ",self.height)
        print("Weight: ",self.weight)

    def get_count(self):
        return Person.quntity



Person1 = Person(1,'1cm','1kg')
Person2 = Person(1,'1cm','1kg')
Person3 = Person(1,'1cm','1kg')
Person4 = Person(1,'1cm','1kg')



print(''
      '')
print(Person.get_count(''))




