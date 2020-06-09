import datetime

while True:
    nanya = input("apakah anda ingin menggunakan kalkulator umur?(y/n)= ")
    if nanya == "y":
        print("SELAMAT DATANG DI KALKULATOR UMUR")
        hari = int(input("silahkan masukkan tanggal(hari) lahir = "))
        bulan = int(input("silahkan masukkan bulan lahir         = "))
        tahun = int(input("silahkan masukkan tahun lahir         = "))

        sekarang = datetime.date.today()
        
        #kondisi sebelum ultah 
        if bulan >= sekarang.month and hari >= sekarang.day :
            print(f"tanggal lahir kamu adalah {hari}-{bulan}-{tahun}")
            print(f"sekarang adalah tanggal {sekarang.day}-{sekarang.month}-{sekarang.year}")
            print(f"umur {sekarang.year-tahun-1},kurang {hari-sekarang.day} hari dan {bulan-sekarang.month} bulan until your birthday")
        #kondisi belom ultah, tapi harinya uda ngelebihin tanggal sekarang
        elif bulan > sekarang.month and hari <= sekarang.day :
            print(f"tanggal lahir kamu adalah {hari}-{bulan}-{tahun}")
            print(f"sekarang adalah tanggal {sekarang.day}-{sekarang.month}-{sekarang.year}")
            print(f"umur {sekarang.year-tahun-1},kurang {sekarang.day-hari} hari dan {bulan-sekarang.month} bulan untill your birthday")

            
        #kondisi setelah ultah
        elif bulan <= sekarang.month and hari >= sekarang.day:
            print(f"tanggal lahir kamu adalah {hari}-{bulan}-{tahun}")
            print(f"sekarang adalah tanggal {sekarang.day}-{sekarang.month}-{sekarang.year}")
            print(f"umur {sekarang.year-tahun},lebih {abs((30-hari)+sekarang.day)} hari dan {sekarang.month-bulan-1} bulan dari your birthday")
        elif bulan <= sekarang.month and hari <= sekarang.day:
            print(f"tanggal lahir kamu adalah {hari}-{bulan}-{tahun}")
            print(f"sekarang adalah tanggal {sekarang.day}-{sekarang.month}-{sekarang.year}")
            print(f"umur {sekarang.year-tahun},lebih {sekarang.day-hari} hari dan {sekarang.month-bulan} bulan dari your birthday")
    elif nanya == "n":
        print("okeeeee")
        break
    else:
        print("harus y/n! ")


    
