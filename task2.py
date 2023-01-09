# Создайте программу для игры в ""Крестики-нолики"".

from random import randint as rnd
field = list(range(1, 10))
valid = list(map(str, range(0,10)))
print(valid)
wins_line = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def draw_field():
    print('-------------')
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|',
              field[2 + i * 3], "|")
    print('-------------')
    print()


def takeinput(token):
    while True:
        value = input(f'Номер поля, где разместить: {token} ? ')
        if value not in valid or value =='':
            print('Неправильный номер :) ')
            continue
        value = int(value)
        if str(field[value - 1]) in 'XO':
            print('Поле занято!!!')
            continue
        field[value - 1] = token
        break


def checkwin():
    for each in wins_line:        
        if (field[each[0]]) == (field[each[1]]) == (field[each[2]]):
            return True
    return False


count = 0
simbols = ('X', 'O') if rnd(0, 100) % 2 else ('O', 'X')
flag = True
while flag:
    draw_field()   
    takeinput(simbols[count % 2])
    if checkwin():
        draw_field()
        print(simbols[count % 2], 'Ты победил!!!')
        flag = not flag
    else:
        count += 1
        if count > 8:
            draw_field()
            print('Ничья!')
            flag = not flag

