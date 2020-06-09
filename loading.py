import time
lod = 4
pol = 4
print("this is a game! ")
while lod <= 12:
    for x in range(pol):
        lod += 1
        print("loading"+"."*x)
        time.sleep(1)
        

   
