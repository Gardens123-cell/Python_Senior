class numbers:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def show_info(self):
        print(max(self.a,self.b,self.c,self.d))
        print(min(self.a,self.b,self.c,self.d))
        print((self.a + self.b + self.c + self.d)/4)

Num1=int((input('Enter 1st number: ')))
Num2=int((input('Enter 2nd number: ')))
Num3=int((input('Enter 3rd number: ')))
Num4=int((input('Enter 4th number: ')))

Numall = numbers(Num1,Num2,Num3,Num4)

Numall.show_info()



