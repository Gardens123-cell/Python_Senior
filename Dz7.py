class Human:
    def __init__(self, name, age, average):
        self.name = name
        self.age = age
        self.average = average
class MyClass:
    def __init__(self, name):
        print('Students in class: ',name)
        self.name = name
        self.students_list = []
    def append_students(self,stud):
        self.students_list.append(stud)


    def remove_students(self,stud):

        name=input('Enter name of the student you want to delete: ')
        for stud in self.students_list:
            if stud.name==name:
                self.students_list.remove(stud)
                break

        else:
            print('Error 404 Not Found: Student is not in the class')

    def printing(self):
        for i in self.students_list:
            print(i.name,i.age,i.average)

artur = Human("Artur", 15, 7.5)
Bob = Human("Bob", 13, 5.5)
John = Human("John",14,8)
Biden = Human('Biden', 14, 4.5)

b = MyClass(input('Class: '))
b.append_students(artur)
b.append_students(Bob)
b.append_students(John)
b.append_students(Biden)
b.printing()
b.remove_students(artur)

for stud in b.students_list:
    print(f'{stud.name}')




