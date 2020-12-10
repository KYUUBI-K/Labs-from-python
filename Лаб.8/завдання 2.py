from random import randint
from math import sqrt
from math import acos
from math import degrees
def cos(a,b):
    d = 0
    for i in range(len(a)):
        d +=a[i]*b[i]
    a1 = 0
    b1 = 0
    for i in range(len(a)):
        a1 += (a[i]**2)
        b1 += (b[i]**2)
    a1 = sqrt(a1)
    b1 = sqrt(b1)
    cos =d/(a1*b1)
    return cos


n = int(input())
a = [randint(-10,10) for i in range(n)]
print(f"a:{a}")
b = [randint(-10,10) for i in range(n)]
print(f"b:{b}")
print(cos(a,b))
degr = degrees(acos(cos(a,b)))
print(f"Градусів:{degr}")
if degr == 90:
    print("Трикутник - прямокутний")
elif degr < 90:
    print("Трикутник - гострокутний")
else:
    print("Трикутник - тупокутній")
