from HW3.Game import Game
from HW3.Gamer import Gamer
from HW3.Map import Map

'''
● Контекст
Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
время реализовать её. Два игрока по очереди ставят крестики
и нолики на игровое поле. Игра завершается когда кто-то
победил, либо наступила ничья, либо игроки отказались
играть.
● Задача
Написать игру в “Крестики-нолики”. Можете использовать
любые парадигмы, которые посчитаете наиболее
подходящими. Можете реализовать доску как угодно - как
одномерный массив или двумерный массив (массив массивов).
Можете использовать как правила, так и хардкод, на своё
усмотрение. Главное, чтобы в игру можно было поиграть через
терминал с вашего компьютера.

mas = [[1,2,3],[4,2,7],[5,2,3]]

'''
if __name__ == '__main__':

    nameGamer1=input("Введите имя первого игрока:")
    gamer1=Gamer('x',nameGamer1)
    nameGamer2=input("Введите имя второго игрока:")
    gamer2=Gamer('0',nameGamer2)
    map1=Map()
    game1=Game(gamer1,gamer2,map1)
    map1.show_matrix()
    game1.startGame()

