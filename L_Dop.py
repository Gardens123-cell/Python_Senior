class Circle:

    def __init__(self,radius):
        self.radius = radius

    def Circumference(self):
        print("Circumference of Circle ", self.radius*2*3.14)

    def Square(self):
        print('Square of circle', self.radius**2*3.14)

Circumference1 = Circle(int(input('Radius(For Circumference):')))
Circumference1.Circumference()

Square1 = Circle(int(input('Radius(For Square): ')))
Square1.Square()



