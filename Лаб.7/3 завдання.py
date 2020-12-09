from random import randint
def matrix_view(a):
    for i in a:
        print(i)
n = int(input("Кількість рядків і стовпців = "))
matrix = [[randint(-100,100) for j in range(n)] for i in range(n)]
matrix_view(matrix)
new_matrix = [[matrix[i][j] for i in range(n)] for j in range(n)]
print("Транспонована матриця:")
matrix_view(new_matrix)

