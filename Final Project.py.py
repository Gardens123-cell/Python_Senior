import sys


class Person:
    def __init__(self,whoareu):
        self.whoareu = whoareu



    def UareStudent(self):
        if self.whoareu =='Student':
            Student()
            logpass = Student()

            logpass.login_page()

            logpass1 = Student()

            logpass1.name = input('Enter your name: ')
            logpass1.surname = input('Enter your surname: ')
            logpass1.fathername = input('Enter your fathername: ')
            logpass1.phonenum = input('Enter your phonenum: ')

            logpass1.infoaboutstud()

            logpass1.delete(input("\nEnter dz  that you want to delete(if you do not want type 1): "))
            logpass1.upload(input("\nEnter dz  that you want to upload (if you do not want type 1): "))
            logpass1.reupload(input("\nEnter dz  that you want to reupload (if you do not want type 1): "))
            logpass1.rate(int(input('\nRate teacher from 1-5: ')))




        elif self.whoareu=='Teacher':
            Teacher()

            teachlogpass = Teacher()
            teachlogpass.login_page_teacher()

            teachlogpass1 = Teacher()
            teachlogpass1.name = input('Enter your name: ')
            teachlogpass1.surname = input('Enter your surname: ')
            teachlogpass1.fathername = input('Enter your fathername: ')
            teachlogpass1.phonenum = input('Enter your phonenum: ')
            teachlogpass1.infoabout_teach()

            teachlogpass1.chceckingHws()
        else:
           print ('You entered incorrect name')
           sys.exit()





class Student:
    login = 'Dada_m4rt'
    password = 'qwerty'

    def login_page(self):

        a = input('Enter your login: ')
        b = input('Enter your password: ')
        if a==self.login and b==self.password:
            print('\nSuccessfully logged in\n')


        else:
            print('Invalid Password or login')
            sys.exit()


    def infoaboutstud(self):
        if self.name == 'Nadir' and self.surname == 'Dadashzade' and self.fathername=='Elshan' and self.phonenum=='0555555555':
            print('\nYou are a student')
            print('\nYour name is: ',self.name)
            print('Your surname is: ',self.surname)
            print('Your fathername is: ',self.fathername)
            print('Your phonenum is: ',self.phonenum)
            print('Your login is: ',self.login)
            print('Your password is: qwe***')
        else:
            print('Invalid name,surname,fathername or phonenum')
            sys.exit()
    def delete(self,delete):
        self.delete = delete
        if self.delete=='1':
            pass
        else:
            print('Successfuly deleted\n')

    def upload(self,upload):
        self.upload = upload
        if self.upload=='1':
            pass
        else:
            print('Successfuly uploaded\n')

    def reupload(self,reupload):
        self.reupload =reupload
        if self.reupload =='1':
            pass
        else:
            print("Successfully reuploaded\n")

    def rate(self,rate):
        self.rate =rate
        if self.rate >= 1 and self.rate <= 5:
            print('Successfully rated, thanks')
        else:
            print('Unavailable')
            sys.exit()



class Teacher:


    login = 'Teacher1'
    password = 'qwerty11'
    def login_page_teacher(self):
        a1 = input('Enter your login: ')
        b1 = input('Enter your password: ')

        if a1=='Teacher11' and b1=='qwerty11':
            print('Successfully logged in')
        else:
            print('Invalid Password or login')
            sys.exit()


    def infoabout_teach(self):
        if self.name=='Nazim' and self.surname=='Qurbanov' and self.fathername=='Imran' and  self.phonenum=='055 255 55 55':
            print('\nYou are a teacher')
            print('\nYour name is: ',self.name)
            print('Your surname is: ',self.surname)
            print('Your fathername is: ',self.fathername)
            print('Your phonenum is: ',self.phonenum)
            print('Your login is: ',self.login)
        else:
            print('Invalid name,surname,fathername or phonenum')
            sys.exit()

    def chceckingHws(self):
        HWs = ['Dz1', 'Dz2', 'Dz4', 'Dz5', 'Dz7', 'Dz12', 'Dz13']

        print('\nAvailable HWs:',HWs)

        a = input('Enter name of the HW you want to check: ')

        if a in HWs:
           pass
        else:
            print('Error 404 not found >- there is no such HW ')
            sys.exit()
        b = int(input(f'\nRate {a} from 1-12: '))
        if b >=1 and b<=12:
            print(f'Successfully rated: {b}')
        else:
            print('Error 404 not found >-<')
            sys.exit()
        c = input(f"\nComment {a}(if you don't want, type 1): ")
        if c=='1':
            pass
        else:
            print('Comment posted')
            sys.exit()


person = Person(input('Are you a Student or a Teacher: '))
person.UareStudent()

