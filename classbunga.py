
class Bunga:
    ciri ="berkelopak"
    ciri2 = "bertangkai"
    @classmethod
    def umum(cls):
        return f"semua bunga {cls.ciri} dan {cls.ciri2}"
    def __init__(self,nama,kelopak,harga):
        self.nama    = nama
        self.kelopak = kelopak
        self.harga   = harga
    
    def kalimat(self):
        return f"Nama bunga {self.nama}, jumlah kelopak{self.kelopak}, harga bunga {self.harga}"

print(Bunga.umum())

daftar = []


'''
while True:
    nanya = input("apakah anda ingin mengisi daftar bunga?(y/n)= ")

    if nanya == "y":
        namab = input("masukkan nama bunga = ")
        kelopakb = int(input("masukkan jumlah kelopak bunga = "))
        hargab = float(input("masukkan harga bunga= "))
        kalimatb = Bunga(namab,kelopakb,hargab)
        daftar.append(kalimatb.kalimat())

    elif nanya == "n":
        print("BERIKUT DAFTAR BUNGA!")
        for a in daftar:
            print(a)
        break

    else:
        print("harus y/n ")
'''