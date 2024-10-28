hod = 2

win_rotation = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

win = 0

a__ = ["-","-","-","-","-","-","-","-","-"]
a = [1,2,3,4,5,6,7,8,9]
dostypnie_hodi = [1,2,3,4,5,6,7,8,9]
rar = 3
def print_board():
    print("===", dostypnie_hodi, "===")
    for i in range(rar):
        print("  ",a__[i*rar], a__[1+i*rar], a__[2+i*rar],"                  ", a[i*rar], a[1+i*rar], a[2+i*rar])

def enter_X(h):
    if h not in dostypnie_hodi:
        print("Это место занято или недоступно, введи другое значение")
        h = int(input("Новое значение: "))
        enter_X(h)
    else:
        a[int(h)-1] = "x"
        a__[int(h) - 1] = "x"
        dostypnie_hodi.remove(h)
        print("==========Доступные ходы============")

def enter_0(h):
    if h not in dostypnie_hodi:
        print("Это место занято или недоступно, введи другое значение")
        h = int(input("Новое значение: "))
        enter_0(h)
    else:
        a[int(h)-1] = "o"
        a__[int(h) - 1] = "o"
        dostypnie_hodi.remove(h)
        print("==========Доступные ходы============")

def win__():
    global win
    global win_rotation
    for G in win_rotation:
        if (a[G[0]] == a[G[1]] and a[G[1]] == a[G[2]]):
            print("Победу одержал", a[G[0]], "!")
            win += 1
            break

def XXX():
    global hod
    print("====================================")
    h = int(input("Ход крестика: "))
    enter_X(h)
    print_board()
    win__()
    if win == 1:
        hod += 10

def OOO():
    global hod
    print("====================================")
    h = int(input("Ход нолика: "))
    enter_0(h)
    print_board()
    win__()
    if win == 1:
        hod += 10

def nomer_hoda():
    global hod
    if hod % 2 == 0:
        XXX()
        hod += 1
    else:
        OOO()
        hod += 1

def pravila():
    print("")
    print("=============Памятка================")
    print("Слева находится игровая доска")
    print("Справа для удобства находится пронумерованная игровая доска")
    print("")

def start_():
    pravila()
    print("==========Доступные ходы============")
    print_board()
    while hod < 11:
        nomer_hoda()

    print("Игра окончена")

start_()