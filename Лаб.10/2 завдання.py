
class monitor:
    def __init__(self, creater, production_date, purchase_date, type, h, w,):
        self.creater = creater
        self.production_date = production_date
        self.purchase_date = purchase_date
        self.type = type
        self.h = h
        self.w = w
        self.__hi = 0
        self.__wi = 0
    @property

    def hi(self):
        return self.h
    @hi.setter
    def hi(self,value):
        if value > 0:
            self.__hi = value
        else:
            raise Exception("False")
    @property

    def wi(self):
        return self.w

    @wi.setter
    def wi(self, value):
        if value > 0:
            self.__wi = value
        else:
            raise Exception("False")


    def age_m(self, current_year):
        print(f"Вік монітору: {current_year - self.production_date} роки")

    def can_disp(self):
        if self.__hi<= self.h and self.__wi<= self.w:
            print("Без маштабування можна")
        else:
            print('Без маштабування не можна')

    def koef(self):
        k1 = self.h/self.__hi
        k2 = self.w/self.__wi
        print(f"Коефіціенти ({k1},{k2})")





M1 = monitor("Asus", 2016, 2019, "1920*1080",20,19)
M1.age_m(2020)
M1.hi = 19
M1.wi =20
M1.can_disp()
M1.koef()

