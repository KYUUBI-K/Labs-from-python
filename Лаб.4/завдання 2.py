a = float(input("Введіть значення a:"))
b = float(input("Введіть значення b:"))
c = float(input("Введіть значення c:"))
#min(a,b)+(max(b,c))**2
if a<b and b>c:
    print(a+b**2)
elif a<b and b<c:
    print(a+c**2)
elif a>b and b>c:
    print(b+b**2)
else:
    print(b+c**2)

