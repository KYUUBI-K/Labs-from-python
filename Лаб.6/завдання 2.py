import math
n = int(input('n: '))
x = float(input('x: '))
a = [math.sin(x) * math.cos(x)]
for i in range(n-1):
    a.append(a[i] + ((-1)**(i+3)) * math.sin((i+2)*x) * math.cos((math.factorial(i+2))*x))
A=a
print(A)
b = min(A)
c = a.index(b)
print("Індекс найменшого елемента A = {0}".format(c))
