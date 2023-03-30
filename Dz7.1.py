import random
list = [random.randint(-100,100) for i in range(50)]
print(list)

pos = 0
neg = 0

num = 0

max = max(list)
min = min(list)

for num in list:
    if num>0:
        pos +=1

    else:
        neg +=1

print("Positive numbers in the list: ", pos)
print("Negative numbers in the list: ", neg)