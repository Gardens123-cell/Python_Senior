# first_input=input('Type Celsius or Fahrenheit: ')
# if first_input=='Celsius':
#     print('°C')
# elif first_input=='Fahrenheit':
#     print('°F')
#
# if first_input=='Celsius':
#   Celsius1=input('Enter degree in °C: ')
#
# elif first_input == 'Fahrenheit':
#     Celsius1 = input('Enter degree in °F: ')

class temp:
    degree =  int(input('1. Type degree in °C: '))

    def show_info(self):
        print('1. Temp in °F: ',self.degree*9/5+32)

    degree2 = int(input('2. Type degree in °F°: '))

    def showinfo2(self):
        print('2. Temp in °C : ', self.degree2 * 5/9 - 32 * 5/9)

temp1 = temp()

temp1.show_info()

temp2 = temp()

temp2.showinfo2()





