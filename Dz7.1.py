import random
list = [random.randint(-100,100) for i in range(100)]
print(list)

pos = 0
neg = 0
zero = 0

num = 0

max = max(list)
min = min(list)

for num in list:
    if num>0:
        pos +=1

    else:
        neg +=1

    if num==0:
        zero +=1

print(('Max number: '),max)
print('Min number: ',min)
print("Positive numbers in the list: ", pos)
print("Negative numbers in the list: ", neg)
print('Zeros: ',zero)