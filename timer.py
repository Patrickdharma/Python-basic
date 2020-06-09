import time
try:
    detik = int(input("masukkan detik= "))
    menit = int(input("masukkan menit= "))
    jam   = int(input("masukkan jam= "))
    total = detik + menit*60 + jam*3600
    for x in range(total,-1,-1):
        time.sleep(1)
        print(x)
    print("time's up!")
except ValueError:
    print("harus Integer!")

