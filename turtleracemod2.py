import turtle
import random
import threading
#fungsi players
def ply1():
    print(f"sekarang adalah giliran {player1}")
    jawaban = int(input(f"berapa {pertanyaan1} + {pertanyaan2}= "))
    answir = int(pertanyaan1) + int(pertanyaan2)
    if jawaban == answir:
        point = random.randrange(1,100)
        print(f"benar sekali, anda mendapatkan point sebanyak {point}!")
        turt1.forward(point)
    else:
        print("oops salah")

def ply2():
    print(f"sekarang adalah giliran{player2}")
    pertanyaan1 = random.randrange(1,55)
    pertanyaan2 = random.randrange(55,101)
    jawaban = int(input(f"berapa {pertanyaan1} + {pertanyaan2}= "))
    answir2 = int(pertanyaan1) + int(pertanyaan2)
    if jawaban == answir2:
        point2 = random.randrange(1,100)
        print(f"benar sekali, anda mendapat point sebanyak {point2}")
        turt2.forward(point2)
    else:
        print("oops salah")


#bikin background timer


screen = turtle.getscreen()
#bikin karakter
turt1 = turtle.Turtle()
turt2 = turt1.clone()
turt1.shape("turtle")
turt2.shape("turtle")
turt1.color("green")
turt2.color("red")
turt1.penup()
turt2.penup()
turt1.goto(-200,100)
turt2.goto(-200,-100)

#bikin circle turt1
turt1.goto(300,60)
turt1.pendown()
turt1.circle(40)
turt1.penup()
turt1.goto(-200,100)
#bikin circle turt2
turt2.goto(300,-140)
turt2.pendown()
turt2.circle(40)
turt2.penup()
turt2.goto(-200,-100)

#bikin dadu
#bikin gamesnya
player1  = input("masukkan nama player 1 = ")
player2  = input("masukkan nama player 2 = ")
print("selamat datang di game balapan turtle")
while True:
    if turt1.pos() >= (300,100):
        print("SELAMAT PLAYER_1 ANDA MENANG!!")
        break
    elif turt2.pos() >= (300,100):
        print("SELAMAT PLAYER_2 ANDA MENANG")
        break
    else:
        #soal untuk player 1
        pertanyaan1 = random.randrange(1,55)
        pertanyaan2 = random.randrange(55,101)
        ply1()
        #soal untuk player 2
        ply2()


        






