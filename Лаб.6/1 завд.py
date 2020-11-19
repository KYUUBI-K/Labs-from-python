n = int(input('Введіть значення n= '))
a = []
d = 1
a = [float(input("a[{0}]=  ".format(i))) for i in range(0,n)]
print("вектор a ={0}".format(a))

for i in range(len(a)):
    if a[i]<0:
        d *= a[i]
print("добуток всіх від'ємних елементів списку a = {0}".format(d))
