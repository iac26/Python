# -*- coding: utf-8 -*-
#TTT

#game
from copy import deepcopy
from random import choice
from random import randint

table = [[" " for x in range(3)] for y in range(3)]
memory = []
play = []
possibleMoves = []

xvict = 0


def victoryTest():
    while True:
        if table[0][0] == table[0][1] == table[0][2]:
            vict = table[0][0]
            break
        elif table[1][0] == table[1][1] == table[1][2]:
            vict = table[1][0]
            break
        elif table[2][0] == table[2][1] == table[2][2]:
            vict = table[2][0]
            break
        elif table[0][0] == table[1][0] == table[2][0]:
            vict = table[0][0]
            break
        elif table[0][1] == table[1][1] == table[2][1]:
            vict = table[0][1]
            break
        elif table[0][2] == table[1][2] == table[2][2]:
            vict = table[0][2]
            break
        elif table[0][0] == table[1][1] == table[2][2]:
            vict = table[0][0]
            break
        elif table[0][2] == table[1][1] == table[2][0]:
            vict = table[0][2]
            break
        else:
            vict = ' '
            break
    return vict

def save():
    fl = open("TTTmemory", "w")
    fl.write(str(len(memory)))
    fl.write("\n")
    for p in range(len(memory)): #plays
        for t in range(len(memory[p])):
            for r in range(len(memory[p][t][0])):
                for c in memory[p][t][0][r]:
                    fl.write(c)
            for co in memory[p][t][1]:
                fl.write(str(co))
            fl.write(str(memory[p][t][2]))
            fl.write("\n")
        fl.write(":")
    fl.close()

def load():
    row = []
    tab = []
    lin = []
    pla = []
    fl = open("TTTmemory", "r")
    l = fl.readline()
    memlen = int(l[:-1])
    for le in range(memlen):
        e = False
        while True:
            for r in range(3):
                for i in range(3):
                    s = fl.read(1)
                    if s == ":":
                        e = True
                        break
                    row.append(s)
                if e:
                    break
                tab.append(deepcopy(row))
                row = []
            if e:
                break
            lin.append(deepcopy(tab))
            cx = int(fl.read(1))
            cy = int(fl.read(1))
            lin.append([cx,cy])
            s = int(fl.read(1))
            lin.append(s)
            tab = []
            s = fl.read(1)
            pla.append(deepcopy(lin))
            lin = []
        memory.append(deepcopy(pla))
    fl.close()


def entry(x, y, s):
    if table[x][y] == ' ':
        table[x][y] = s
        return True
    else:
        return False
def size():
    c = 0
    for x in range(3):
        for y in range(3):
            if table[x][y] != ' ':
                c = c + 1
    return c

def gui():
    print "-------------"
    print "|",table[0][0],"|",table[1][0],"|",table[2][0],"|"
    print "-------------"
    print "|",table[0][1],"|",table[1][1],"|",table[2][1],"|"
    print "-------------"
    print "|",table[0][2],"|",table[1][2],"|",table[2][2],"|"
    print "-------------"

def player(t = "x"):
    while True:
        x = input("enter col(0-2): ")
        y = input("enter row(0-2): ")
        if entry(x, y, t):
            break
        else:
            print "this case is already full!"
    return [x,y]

def machine(s = 'x',rnd = False):
    wd = 0
    while True:
        wd = wd + 1
        if bestMoves():
            move = bestMove()
        else:
            move = [randint(0,2),randint(0,2)]
        if wd > 9:
            move = [randint(0,2),randint(0,2)]
        if rnd:
            move = [randint(0,2),randint(0,2)]
        if entry(move[0], move[1], s):
            return move[0], move[1]
            break


def storeT(x,y):
    t = deepcopy(table)
    play.append([t, [x,y], 0])

def storeS(s):
    for i in range(len(play)):
        play[i][2] = s

def storeP():
    p = deepcopy(play)
    memory.append(p)


def bestMoves():
    rand = True
    s = size()
    for m in range(len(memory)):
        try:
            if memory[m][s][0] == table:
                p = s+1
                try:
                    possibleMoves.append(memory[m][p])
                except:
                    pass
        except:
            rand = False
    if len(possibleMoves) < 1:
        rand = False
    return rand

def bestMove():
    for move in possibleMoves:
        if move[2] > 0:
            return move[1]
        else:
            return [randint(0,2), randint(0,2)]
            break

def worstMoves():
    pass


def pVp(s = "o", o = "x"): #s = starting player , o = opponent
    table = [[" " for x in range(3)] for y in range(3)]
    play = []
    print "New Game",s,"Vs",o,"!"
    storeT(0,0)
    while True:
        print s,"Plays!"
        gui()
        a = player(s)
        storeT(a[0], a[1])
        if size() == 9:
            print "Tie!"
            break
        v = victoryTest()
        if v != ' ':
            gui()
            print "player",v,"won!!"
            break
        print o,"Plays!"
        gui()
        a = player(o)
        storeT(a[0], a[1])
        if size() == 9:
            print "Tie!"
            break
        v = victoryTest()
        if v != ' ':
            gui()
            print "player",v,"won!!"
            break
    if v == "x":
        storeS(1)
        storeP()
    elif v == "o":
        storeS(0)
    else:
        storeS(0)


def mVm():
    table = [[" " for x in range(3)] for y in range(3)]
    play = []
    print "mVm!"
    storeT(0,0)
    while True:
        gui()
        a = machine("o", True)
        storeT(a[0], a[1])
        if size() == 9:
            print "Tie!"
            break
        v = victoryTest()
        if v != ' ':
            gui()
            print "o Won!"
            break
        gui()
        a = machine("x")
        storeT(a[0], a[1])
        if size() == 9:
            print "Tie!"
            break
        v = victoryTest()
        if v != ' ':
            gui()
            print "x Won!"
            break
    if v == "x":
        storeS(1)
        storeP()
    elif v == "o":
        storeS(0)
    else:
        storeS(0)

def pVm():
    table = [[" " for x in range(3)] for y in range(3)]
    play = []
    print "pVm!"
    storeT(0,0)
    while True:
        gui()
        a = player("o")
        storeT(a[0], a[1])
        if size() == 9:
            print "Tie!"
            break
        v = victoryTest()
        if v != ' ':
            gui()
            print "o Won!"
            break
        gui()
        a = machine()
        storeT(a[0], a[1])
        if size() == 9:
            print "Tie!"
            break
        v = victoryTest()
        if v != ' ':
            gui()
            print "x Won!"
            break
    if v == "x":
        storeS(1)
        storeP()
    elif v == "o":
        storeS(0)
    else:
        storeS(0)
