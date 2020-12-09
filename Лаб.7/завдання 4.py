from random import randint
n = int(input("Кількість рядків і стопців   = "))
Matrix = [[randint(-100,100) for j in range(n)] for i in range(n)]
for i in range(n):
    print(Matrix[i])

print("       ")
for j in range(n):
    if j % 2 != 0:
        el = []
        for i in range(n):
            el.append(Matrix[i][j])
        el = sorted(el,reverse = True)
        for i in range(n):
            Matrix[i][j] = el[i]
for i in range(n):
    print(Matrix[i])

