# # 1-dastur
# class Talaba:
#     def __init__(self, ism, familiyasi):
#         self.ism = ism
#         self.familiyasi = familiyasi
#     def tanishtir(self):
#         return f"Ism :{self.ism}, {self.familiyasi}"


# class Tajriba(Talaba):
#     def __init__(self, ism, familiyasi, t_yil):
#         super().__init__(ism, familiyasi)
#         self.t_yil = t_yil
#     def tanishtir1(self):
#         print(f"Ism: {self.ism}\nFamiliyasi: {self.ism}\nTugilgan yili: {self.t_yil}")

# ad = Tajriba('ag', 'jhgd', 2006)

# ad.tanishtir1()

# # 2-dastur
# class Odam:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
    
#     def tanishtir(self):
#         return f"{self.ism}, {self.yosh}"


# class Dasturchi(Odam):
#     def __init__(self, ism, yosh, tajriba):
#         super().__init__(ism, yosh)
#         self.tajriba = tajriba
#     def tanishtir1(self):
#         return f"{self.ism}, {self.yosh}, {self.tajriba}"

# b = Dasturchi('maqsadbek', 16, 'yaxshi') 
# print(b.tanishtir1())

# # 3-dastur
# class Manzil:
#     def __init__(self, viloyat, tuman, kocha, uy):
#         self.viloyat = viloyat
#         self.tuman = tuman
#         self.kocha = kocha
#         self.uy = uy
#     def get_manzil(self):
#         return f"{self.viloyat.capitalize()}, {self.tuman.capitalize()}, {self.kocha.capitalize()}, {self.uy.capitalize()}"


# class Talaba:
#     def __init__(self, ism, familiya, t_yil, manzil):
#         self.ism = ism
#         self.familiya = familiya
#         self.t_yil = t_yil
#         self.manzil = manzil
#     def get_info(self):
#         return f"Ismi {self.ism.capitalize()}\nFamiliya {self.familiya.capitalize()}\nTug'ilgan yili {self.t_yil} yil\nManzil {self.manzil.get_manzil()}"

# man = Manzil("andijon", "paxtaobod", "oltin yo'l", "73")
# a = Talaba("maqsadbek", "ibrohimjonov", 2006,  man)
# print(a.get_info())