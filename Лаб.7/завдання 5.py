import random
n = int(input())
a = [[random.randint(-10,10) for i in range(n)]for j in range(n)]
c = []
for i in range(n):
    s = 0
    for j in range(n):
        if a[i][j]<0 and a[i][j]%2!=0:
            s += abs(a[i][j])
    c.append([i, s])
print(c,'\n')
c.sort(key = lambda item: item[1])
d = []
print(c,'\n')
for i in range(n):
    print(a[i])
print('\n\n')
for i in range(n):
    d.append([a[j][c[i][0]] for j in range(n)])
d = [[d[k][j] for k in range(n)] for j in range(n)]
for i in range(n):
    print(d[i])

        

