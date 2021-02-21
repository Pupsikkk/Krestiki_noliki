fieldSize = 3
zeroTurn = True
my_field = [["-"] * 3 for i in range(fieldSize)]


# Да да, можно было проще. Но я захотел функцию которая сможет обрабатывать любые размерности


def draw_field(field):
    for i in range(fieldSize + 1):
        line = []
        for j in range(fieldSize):
            if i == 0:
                if j == 0:
                    line.append(" ")
                line.extend([f"{s}" for s in range(0, fieldSize)])
                break
            if j == 0:
                line.append(f"{i - 1}")
            line.append(field[i - 1][j])
        print(" ".join(line))


def turns_controller():
    global zeroTurn
    if zeroTurn:
        L = input("Ход нуля:").split()
        if not (len(L) != 2 or int(L[0]) > fieldSize - 1 or int(L[1]) > fieldSize - 1):
            if my_field[int(L[0])][int(L[1])] == "-":
                my_field[int(L[0])][int(L[1])] = "O"
                zeroTurn = False
            else:
                print("Поле занято. Попробуйте ещё раз!")
        else:
            print("Некорректный диапазон")
    else:
        L = input("Ход крестика:").split()
        if not (int(L[0]) > fieldSize - 1 or int(L[1]) > fieldSize - 1):
            if my_field[int(L[0])][int(L[1])] == "-":
                my_field[int(L[0])][int(L[1])] = "Х"
                zeroTurn = True
            else:
                print("Поле занято. Попробуйте ещё раз!")
        else:
            print("Некорректный диапазон")


def end_game_controller():
    global turnsCounter
    if (my_field[0][0] == my_field[0][1] == my_field[0][2] != "-" or
            my_field[1][0] == my_field[1][1] == my_field[1][2] != "-" or
            my_field[2][0] == my_field[2][1] == my_field[2][2] != "-" or
            my_field[0][0] == my_field[1][0] == my_field[2][0] != "-" or
            my_field[0][1] == my_field[1][1] == my_field[2][1] != "-" or
            my_field[0][2] == my_field[1][2] == my_field[2][2] != "-" or
            my_field[0][0] == my_field[1][1] == my_field[2][2] != "-" or
            my_field[2][0] == my_field[1][1] == my_field[0][2] != "-"):
        print("\n\n\nПобедил нолик!") if not zeroTurn else print("\n\n\nПобедил крестик!")
        return False
    if turnsCounter == 9:
        print("Ходы закончились! Победила дружба")
        return False
    turnsCounter += 1
    return True


def restart_game():
    if input("Если хотите начать заново введите 1, если хотите выйти введите 0: ") == "0":
        return True
    else:
        return False


# main
print("Вводите координаты вот так: 0 1 ; 3 2 ; 0 0 и тд.")

while True:
    turnsCounter = 0
    my_field = [["-"] * 3 for i in range(fieldSize)]
    while end_game_controller():
        draw_field(my_field)
        turns_controller()
    draw_field(my_field)
    if restart_game():
        break
