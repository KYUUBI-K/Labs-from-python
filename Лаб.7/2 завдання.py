from math import sin
from  math import fabs
n = int(input("Кількість рядків і стовпців = "))
a = []
for i in range(1,n+1):
    b = []
    for j in range(1,n+1):
        b.append(sin(((i**2) - (j**2))/n))
    a.append(b)
for i in range(n):
    print(a[i])
print("      ")
a = [[abs(el) for el in a[i]] for i in range(len(a))]
for i in range(n):
    print(a[i])
c =[max(el)for el in a]
d = max(c)
print(f"найбільший елемент по модулю ={d}")
index = c.index(d)
print(f"index: {index}")





