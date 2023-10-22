from math import factorial
from math import e
summ = 0
for i in range(0, 3):
    summ += (e**(-1)) / factorial(i)
    print((e**(-1)) / factorial(i))

print(1-summ)
