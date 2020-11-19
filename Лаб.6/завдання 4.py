import math
n = int(input("n = "))
a = [float(input("a[{0}] = ".format(i)))for i in range(n)]
print("Масив a ={0}".format(a))
b = []
c = []
for i in range(len(a)):
    if math.fabs(a[i]) <= 1:
        b.append(a[i])
    else:
        c.append(a[i])
b+=c
a=b
print("Перетворений масив a ={0}".format(a))