class Password:
    def __init__(self,password1):
        self.password1 = password1

class Checking_the_password:
    def __init__(self,password):
         self.password = password

    def add_password(self, password):
        self.passwords.append(password)

    def Checking(self,password2):
        commonpassword = ['12345', 'qwerty' , 'password']
        specsim = ['_', '-', '@', '!', '#', '/', '?', '~']
        if len(self.password.password1)<4:
            print('Password is too short')
        elif self.password.password1.lower() in commonpassword:
                print('Password is common ')
        if not any(symb.isdigit() for symb in password2):
            print('Your password must contain at least 1 number')
        if not any(symb.isupper() for symb in password2):
            print('Your password must contain at least 1 capital letter')
        if not any(symb in specsim for symb in password.password1):
             print('Your password must contain special symbols')
        else:
            print('You can use this password')


password = Password(input('Enter your password: '))
checking = Checking_the_password(password)
password2 = (input('Re-enter your password: '))
checking.Checking(password2)