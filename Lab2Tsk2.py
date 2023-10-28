import random
ver = 0
win = 0
while ver == 0:
    player = int(input("1 - Камень; 2 - Ножницы; 3 - Бумага\n"))
    if player == 1 or player == 2 or player == 3:
        ver = 1
    else:
        while player not in [1, 2, 3]:
            print("Неверное значение, попробуйте еще раз")
            player = int(input("1 - Камень; 2 - Ножницы; 3 - Бумага\n"))
        if player == 1 or player == 2 or player == 3:
            ver = 1
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
    cont = int(input("Для продолжения игры нажмите '1'. В ином случае игра завершится.\n"))
    if cont == 1:
        ver = 0
