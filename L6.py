class Human:
    height = 170
    age = 20
    def hello(self):
        pass
class Student(Human):
    height = 160
    age = 18

class Worker(Human):
    height = 175
    age = 20

nick  = Student()
ann = Worker()

print(ann.height)
print(ann.age)

print(nick.age)
print(nick.height)
