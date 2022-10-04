from math import *
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - (4 * a * c)
if d < 0:
    print('Нет корней')
elif d == 0:
    print(-b / (2 * a))
elif d > 0:
    k1 = (-b + sqrt(d)) / (2 * a)
    k2 = (-b - sqrt(d)) / (2 * a)
    if k1 > k2:
        print(k2, k1, sep='\n')
    else:
        print(k1, k2, sep='\n')
