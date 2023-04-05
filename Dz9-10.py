class Registrtion:
    def __init__(self,name,surname,birthday,mail,cardNo):
        self.name = name
        self.surname = surname
        self.__birthday = birthday
        self.__mail = mail
        self.__cardNo = cardNo
    def get_change(self):
        return self.__mail
        return self.__birthday
        return self.__cardNo

    def set_change(self,cardNo):

        if len(self.__cardNo) < 16:
            print('Card  must have at least 16 characters ')

        if len(self.__cardNo) > 19:
            print('Card  must have at most 19 characters')

        if len(self.__birthday) < 4:
            print('Date must have at least 4 numbers')

        if '@' not in self.__mail and '.az' not in self.__mail and '.com' not in self.__mail and '.ru' not in self.__mail and '.cz' not in self.__mail and '.edu' not in self.__mail and '.net' not in self.__mail and '.org' not in self.__mail and '.co' not in self.__mail and '.us' not in self.__mail:
            print('Invalid email address')

        if len(self.name) == 1 and len(self.surname) == 1:
            print('Your name or surname is too short')

        else:
            print('Successfully registered')






registr = Registrtion(input('Enter your name: '),input('Enter your surname: '),input('Enter your birthday: '),input('Enter your mail: '),input('Enter your card №: '))
registr.set_change('')

