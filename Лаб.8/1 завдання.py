def max(number_1, number_2, number_3):
    if number_1 > number_2 > number_3:
        return number_1
    elif number_2 > number_1 > number_3:
        return number_2
    else:
        return number_3


x = int(input())
y = int(input())
z = int(input())
u = (max(x, y, z) + max((x + y), x*y, 4 * z)) / (max((max((x + y), x * y, x ** 2)) ** 2, 7, z ** 2))
print(u)