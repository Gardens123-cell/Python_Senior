class Car:
    def __init__(self,model,style,year,color,engine,fuel,mileage,drivetrain,transmission,range):
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.mileage = mileage
        self.fuel = fuel
        self.style = style
        self.drivetrain  = drivetrain
        self.transmission  = transmission
        self.range = range
    def display_info(self):
        print("Car's Model: ", self.model)
        print('Style: ',self.style)
        print('Year: ', self.year)
        print('Color: ', self.color)
        print('Engine : ', self.engine)
        print('Fuel: ',self.fuel)
        print('Mileage: ',self.mileage)
        print('Drivetrain: ', self.drivetrain)
        print('Transmission: ', self.transmission)
        print('Range in kilometres: ',self.range)
Car=Car('Lexus LX 500d','Offroader / SUV',2023,'Sonic Titanium','V6  / 3.3L / 300hp','Petrol','0km','4WD','10-speed shiftable, automatic','740km')
Car.display_info()



