from math import sqrt
a, b = float(input()), float(input())
c1 = (a + b) / 2
c2 = sqrt(a * b)
c3 = 2 * (a * b) / (a + b)
c4 = sqrt((a**2 + b**2) / 2)
print(c1, c2, c3, c4, sep='\n')
