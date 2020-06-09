'''
class Patrick:
    def __init__(self,name,age,gender,school):
        self.name = "Patrick"
        self.age  = 18
        self.gender = "male"
        self.school = "Kanisius"
    def sekolah(self):
        return f"sekolah saya ada di {self.school}"

orang = Patrick()
print(orang.sekolah())

#bikin class, rumus persegi, ada panjang sama lebar, bikin functinonya buat nge kaliin
#buat function buat ngali lebar sama panjang

class Persegi:
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar   = lebar
    def rumus(self):
        return f"persegi dengan panjang {self.panjang} meter dan lebar {self.lebar} meter memiliki luas sebesar {self.panjang*self.lebar} meter"

a = int(input("masukkan panjang persegi pertama= "))
b = int(input("masukkan lebar persegi pertama = "))

persegi1 = Persegi(a,b)

print(persegi1.rumus())
'''


class Bunga:
    def __init__(self,nama,kelopak,harga):
        self.nama    = nama
        self.kelopak = kelopak
        self.harga   = harga
    
    def kalimat(self):
        return f"Nama bunga {self.nama}, jumlah kelopak{self.kelopak}, harga bunga {self.harga}"
daftar = []

while True:
    nanya = input("apakah anda ingin mengisi daftar bunga?(y/n)= ")

    if nanya == "y":
        namab = input("masukkan nama bunga = ")
        kelopakb = int(input("masukkan jumlah kelopak bunga = "))
        hargab = float(input("masukkan harga bunga= "))
        kalimatb = Bunga(namab,kelopakb,hargab)
        daftar.append(kalimatb)

    elif nanya == "n":
        print("BERIKUT DAFTAR BUNGA!")
        for a in daftar:
            print(a)
        break

    else:
        print("harus y/n ")
