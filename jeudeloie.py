from glob import glob
from random import *
from unittest import result


tbl_game = []
player = 10

def create_board():
    for i in range(30):
        case_rdm = randint(1,5)
        tbl_game.append(case_rdm)
    return print(tbl_game)

def diceRolling():
    print("Vous lancez les dés...")
    result = randint(1,12)
    print("Vous avancez de:", result, "cases")
    return result

start = 0

def move():
    global start
    tbl_game[start + resultatDice] += player
    start = resultatDice
    print(tbl_game)

create_board()
print("Joueur:1")
resultatDice = diceRolling()
move()
resultatDice = diceRolling()
move()
resultatDice = diceRolling()
move()