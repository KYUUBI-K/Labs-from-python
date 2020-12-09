from random import randint
n = int(input("Кількість рядків   = "))
m = int(input("Кількість  стовпців = "))
Matrix = [[randint(-100,100) for j in range(n)] for i in range(m)]
for i in range(m):
        print(Matrix[i])
positiveEl = 1
for i in range(m):
        for j in range(i):
                if Matrix[i][j]>0:
                        positiveEl*=Matrix[i][j]
print(positiveEl)