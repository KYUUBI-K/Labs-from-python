

matrix = [[2, -2, 3], [2, 5, 8], [3, 8, -2]]
k = 3
for i in range(k):
    print(matrix[i])
for i in range(k):
    for j in range(k):
        if matrix[i][j] < 0:
            el = []
            for n in range(k):
                el.append(matrix[n][i])
                if el == matrix[i]:
                    print("сума  {0} стовпця: {1}".format(i+1, sum(el)))
                    break



