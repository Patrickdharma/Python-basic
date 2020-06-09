#buat kalkulator, masukin angka pertama dan kedua 
# pilihan tambah kurang kali bagi
satu = int(input("masukkan angka pertama= "))
dua  = int(input("masukkan angka kedua= "))
if satu and dua:
    print("tekan 1 untuk tambah")
    print("tekan 2 untuk kurang")
    print("tekan 3 untuk kali")
    print("tekan 4 untuk bagi")
    pilihan = int(input("masukkan pilihan= "))
    if pilihan == 1:
        print(f"jawabannya adalah {satu+dua}!")
    elif pilihan == 2:
        print(f"jawabannya adalah {satu-dua}!")
    elif pilihan == 3:
        print(f"jawabannya adalah {satu*dua}!")
    elif pilihan == 4:
        print(f"jawabannya adalah {satu/dua}!")
    else:
        print("invalid answer!")

        
