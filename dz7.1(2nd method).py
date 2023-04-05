import random
digits = []

for i in range(5):
    digits.append(random.randint(-10,50))
print(digits)


def min_num():
    min = digits[0]
    for i in digits:
        if i < min:
            min = i
    return min



def max_num():
    max = digits[0]
    for i in digits:
        if i > max:
            max = i
    return max


print('Min number: ',min_num())
print('Min number: ',max_num())



def positive():
    count = 0
    for i in digits:
        if i > 0:
            count +=1
    print(count)


print('Quantity of positive: ')
positive()

def negative():
    count = 0
    for i in digits:
        if i<0:
            count+=1
    print(count)


print('Quantity of negative:')
negative()