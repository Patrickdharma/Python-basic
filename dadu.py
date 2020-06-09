import random
while True:
    nanya = input("mau main dadu(y/n)= ")
    if nanya == "y":
        angka = random.randrange(1,7)
        print(f"you have rolled {angka}")
    elif nanya == "n":
        print("yasuda...")
        break
    else:
        print("YES OR NO!!!!")