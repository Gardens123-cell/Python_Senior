Student_list = [input('Enter name of the 1st student: '),input('2nd: '),input('3rd: '),input('4th: ')]

def adding(name):
    Student_list.append(name)
    print('Name added successfully ')
    print(Student_list)

def remove(name):
    if name in Student_list:
        Student_list.remove(name)
        print('Name removed successfully')
        print(Student_list)
    else:
        print("Error 404 Not Found(student is not on the list")

def replacing(oldName,Newname):
    if oldName in Student_list:
        Student_list.remove(oldName)
        Student_list.append(Newname)
        print(Student_list)
    else:
        print("Error 404 Not Found(student is not on the list")

print(Student_list)

adding(input('Enter name of the student you want to add: '))

remove(input('Enter name of the student you want to remove: '))

replacing(input('Enter the name of the old student: '),input('Enter the name of the new student: '))


