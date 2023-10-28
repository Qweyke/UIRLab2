import random

ver = 0
win = 0
player = 0
game = 0


def check():
    global ver
    global player
    player = int(input("1 - Камень; 2 - Ножницы; 3 - Бумага\n"))

    if player == 1 or player == 2 or player == 3:
        ver = 1
    else:
        while player not in [1, 2, 3]:
            print("Неверное значение, попробуйте еще раз")
            player = int(input("1 - Камень; 2 - Ножницы; 3 - Бумага\n"))
        if player == 1 or player == 2 or player == 3:
            ver = 1


def play_round(player):
    global win

    choices = {1: "Камень", 2: "Ножницы", 3: "Бумага"}
    comp = random.randint(1, 3)

    print("(Вы) - ", choices[player])
    print("(ИИ) - ", choices[comp])

    if player == comp:
        win = 0
    elif (player == 1 and comp == 2) or (player == 2 and comp == 3) or (player == 3 and comp == 1):
        win = 1
    elif (player == 1 and comp == 3) or (player == 2 and comp == 1) or (player == 3 and comp == 2):
        win = 2

    if win == 0:
        print("НИЧЬЯ")
    elif win == 1:
        print("ПОБЕДА ЧЕЛОВЕЧЕСТВА")
    else:
        print("ПОБЕДА БЕЗДУШНОЙ МАШИНЫ")
    return win


while game == 0:
    variant = int(input("Выберите тип игры: 1 - Турнир; 2 - Обычная.\n"))
    if variant == 1:
        pc = 0
        human = 0
        game = 1
        count = int(input("Выберите кол-во раундов \n"))
        while count >= 1:
            check()
            win1 = play_round(player)
            count -= 1
            ver = 0
            if win == 1:
                human += 1
            if win == 2:
                pc += 1
        if human > pc:
            print(f"Вы победили со счетом {human} : {pc}")
        if human < pc:
            print(f"ИИ победил со счетом {pc} : {human}")
        if human == pc:
            print(f"Ничья со счетом {pc} : {human}")

    if variant == 2:
        while ver == 0:
            check()
            win2 = play_round(player)
        game = 1
        ver = 0

    cont = int(input("Для продолжения игры нажмите '1'. В ином случае игра завершится.\n"))
    if cont == 1:
        game = 0
