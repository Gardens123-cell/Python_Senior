# # c = 0
# class Person:
#     c = 0
#
#     def __init__(self,name):
#         self.name = name
#         # global c
#         Person.c+=1
#
#     def printing(self):
#         pass
#
#     def counter(self):
#
#         return Person.c
# john = Person('John Wick')
# Nicat = Person('Nicat')
# john.printing()
# Nicat.printing()
#
# print(Person.counter(''))
#


'2nd method'
class Person:
    c = 0

    def __init__(self,name):
        self.name = name
        self.c = 0

    def counter(self):
        self.c+=1
        return self.c

john = Person('John Wick')
Nicat = Person('Nicat')
john.counter()
Nicat.counter()

print(john.counter())