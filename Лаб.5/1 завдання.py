#Знайти суму sinx
import math
n = int(input("Введіть значення n= "))
x = float(input("Введіть значення x = "))
S = 0
i = 1
while i<=n:
    S+=(math.sin(x))**i
    i+=1
print("Сума={0}".format(S))


