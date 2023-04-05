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
        # self.__cardNo = cardNo

        if len(self.__cardNo) < 16:
            print('Card  must have at least 16 characters ')

        else:
            print('Successefully registered')


registr = Registrtion(input('Enter your name: '),input('Enter your surname: '),input('Enter your birthday: '),input('Enter your mail: '),input('Enter your card №: '))
registr.set_change('')

