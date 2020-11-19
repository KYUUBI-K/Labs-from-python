n = int(input("Задайте вимір векторів: "))
a = [float(input("Введіть елементи для вектора a:")) for i in range(n)]
b = [float(input("Введіть елементи для вектора b:")) for i in range(n)]
c = [float(input("Введіть елементи для вектора c:")) for i in range(n)]
print("Елементи вектора а={0}".format(a))
print("Елементи вектора b={0}".format(b))
print("Елементи вектора c={0}".format(c))
ab = 0
ac = 0
for i in range(len(a)):
    ab += 2 * a[i] * b[i]
    ac += 3 * a[i] * c[i]
print("a*b = {0}".format(ab))
print("a*c = {0}".format(ac))
S = ab - ac
print("Сума = {0}".format(S))
