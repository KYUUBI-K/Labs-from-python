#Знайти найбільшу сторону
from math import sqrt
x1 = float(input('Введіть значення x1='))
y1 = float(input('Введіть значення y1='))
x2 = float(input('Введіть значення x2='))
y2 = float(input('Введіть значення y2='))
x3 = float(input('Введіть значення x3='))
y3 = float(input('Введіть значення y3='))
AB = sqrt((x2-x1)**2+(y2-y1)**2)
BC = sqrt((x3-x2)**2+(y3-y2)**2)
AC = sqrt((x3-x1)**2+(y3-y1)**2)
if AB>BC and AB>AC:
    print("AB-Найбільша сторона")
elif BC>AB and BC>AC:
    print("BC-Найбільша сторона")
else:
    print("AC-Найбільша сторона")

