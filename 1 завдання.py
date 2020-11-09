#знайти площу(S) і периметр ромба(P)
import math
side_of_the_rhombus = float (input("Сторони ромба ="))
angle = float(input("Кут= "))
S = (side_of_the_rhombus**2)*(math.sin(angle))
P= side_of_the_rhombus*4
print('Площа = {0}, Периметр = {1}'.format(S,P))