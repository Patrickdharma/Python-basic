ayam = input("punya ayam(Y/N)=" )
tepung = input("punya tepung(Y/N)=")
if ayam == "Y" and tepung == "Y":
    print("bisa menggoreng ayam!")
elif ayam == "Y" and tepung == "N":
    print("tidak bisa menggoreng ayam, hanya memiliki ayam")    
elif ayam == "N" and tepung == "Y":
    print("tidak bisa menggoreng ayam, hanya memiliki tepung")
elif ayam == "N" and tepung == "N":
    print("beli bahan dulu !")
else:
    print("invalid input")

