class straight_in_flatness:
    def __init__(self,a = 0,b = 0, c = 0):
        self.a = a
        self.b = b

    def input(self):
        n = 3
        print("задайте  коєфіцієнти: ")
        self.a = [int(input("коєфіцієнт a[{0}]=  ".format(i))) for i in range(1,n+1)]
        self.b = [int(input("коєфіцієнт b[{0}]=  ".format(i))) for i in range(1, n+1)]

    def print_koef(self):
        print(f"straight_in_flatness \n пряма a: {self.a}, \n пряма b :{self.b}")

    def parallelism(self,b):
        if self.a[0]/self.b[0] == self.a[1]/self.b[1] == self.a[2]/self.b[2]:
            print("Прямі а і b паралельні")
        else:
            print("Прямі а і b не паралельні")


    def point_of_intersection(self,b):
        d = self.a[0]*self.a[1]*self.b[1]
        x = (self.a[0]*self.b[2]-self.b[1]*self.a[2])/d
        y = (self.b[0]*self.a[2]-self.a[0]*self.b[2])/d
        print(f'Прямі перетинаються у точці({x};{y})')
    def belonging(self):
        x = float(input("x: "))
        y = float(input("y: "))
        if self.a[0]*x+self.a[1]*y+self.a[2] == 0:
            print('Точка належить')
        else:
            print('Точка не належить')




a = straight_in_flatness()
b = straight_in_flatness()
a.input()
a.print_koef()
a.point_of_intersection(b)
a.parallelism(b)
a.belonging()

