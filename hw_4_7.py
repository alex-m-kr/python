# Задание 4_7. yield
import math
def fact(n):
    lst = [i for i in range(1, n + 1)]
    for el in lst:
        yield math.factorial(el)

n = int(input('n: '))
for el in fact(n):
    print(el)
