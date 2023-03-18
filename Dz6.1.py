class Coffee_machine:
    def info(self):
        print("Coffee machine's brand: Philips Domestic Appliances")
        print('Price: €305.99')
        print("Colour: Black")
        print("Capacity: 1.7lt")
        print('Power / Wattage: 1500 watts')
        print('Material: Plastic')


class Blender(Coffee_machine):
    def info(self):
        print(''
              '')
        print("Blender's brand: Enfmay")
        print('Price: €89.99')
        print('Colour: Black')
        print('Capacity: 2lt')
        print('Power / Wattage: 2000 watts')
        print('Material: Titanium')



class  MeatGrinder(Coffee_machine):
    def info(self):
        print(''
              '')
        print("MeatGrinder's brand: Bosch Hausgeräte")
        print('Price: €158.99')
        print('Colour: Silver')
        print('Capacity: 4.3lt ')
        print('Power / Wattage: 800 watts')
        print('Material: Stainless steel')

a = Coffee_machine()
a.info()

b = Blender()
b.info()

c = MeatGrinder()
c.info()