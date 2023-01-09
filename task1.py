# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint as r


def takecandy():
    taken_candy = int(
        input(f"Игрок сколько конфет хочешь забрать от 1 до 28? "))
    while taken_candy < 1 or taken_candy > 28:
        taken_candy = int(input(f"Игрок попробуй еще раз. От 1 до 28! "))
    return taken_candy


def botik(candy):
    random = r(1, 29)
    if candy > 29 and candy < 58:
        random = candy - 29
    return random


name = "Игрок"
bot = "Бот"
candy = 2021
step = r(0, 2)
print(f"{name if step == 1 else bot} Ходит первым!")
while candy > 28:
    taken = takecandy() if step == 1 else botik(candy)
    candy -= taken
    step += 1 if step < 1 else -1
    print(f"{bot if step == 1 else name} взял {taken} конфет. Осталось {candy}.")
print(f'Победил: {name if step == 1 else bot}, забрав все себе.')