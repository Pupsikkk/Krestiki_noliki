field_size = 3
counter = 0
zeroTurn = True


def draw_field(received_field):
    first_line = [" "]
    first_line.extend([i for i in range(field_size)])
    print(*first_line)
    for i in range(field_size):
        print(f"{i} " + " ".join(received_field[i]))


def turns_controller(received_field):
    while True:
        inp_inf = input("Ваш ход: ").split()
        if len(inp_inf) != 2:
            print("Введите две координаты")
            continue
        if not (inp_inf[0].isdigit() and inp_inf[0].isdigit()):
            print("Используйте числа")
            continue
        x, y = map(int, inp_inf)
        if not (0 <= x < field_size and 0 <= y < field_size):
            print("Некорректный диапазон")
            continue
        if received_field[x][y] != "-":
            print("Поле занято")
            continue
        global zeroTurn
        received_field[x][y] = "O" if zeroTurn else "X"
        zeroTurn = not zeroTurn
        break


def end_game_check(received_field):
    def check_line(a1, a2, a3):
        if a1 == a2 == a3 != "-":
            return True

    for i in range(field_size):
        if check_line(received_field[i][0], received_field[i][1], received_field[i][2]) or \
                check_line(received_field[0][i], received_field[1][i], received_field[2][i]) or \
                check_line(received_field[0][0], received_field[1][1], received_field[2][2]) or \
                check_line(received_field[2][0], received_field[1][1], received_field[0][2]):
            print("Победил О!!!") if not zeroTurn else print("Победил X!!!")
            return True
    global counter
    if counter == 8:
        print("Ходы закончились! Победила дружба")
        return True

    counter += 1
    return False


def restart_check():
    if input("Если хотите начать заново введите 1, если хотите выйти введите 0: ") == "1":
        return True
    else:
        return False


print("Вводите координаты вот так: 0 1 ; 3 2 ; 0 0 и тд.")
field = [["-"] * field_size for _ in range(field_size)]
while True:
    draw_field(field)
    turns_controller(field)
    if end_game_check(field):
        draw_field(field)
        if restart_check():
            field = [["-"] * field_size for _ in range(field_size)]
            counter = 0
        else:
            break
