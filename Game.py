class Game:

    def __init__(self, gamer1,gamer2,matrix):
        self.gamer1=gamer1
        self.gamer2=gamer2
        self.map=matrix

    def startGame(self):

        print("Игра началась, делайте ход, в формате: номер столбца-номер строки, например, 0-1:")
        print("Если хотите остановить игру, наберите '10-10' \n ")
        while self.map.countMoves>=0:
            if self.map.countMoves%2!=0: #создаем очередность ходов игроков
                gamer=self.gamer1
            else:
                gamer=self.gamer2
            (xx, yy) = gamer.makeAMove() #получаем введенные игроком индексы матрицы
            if xx==10 and yy==10: #запланированнй выход из игры
                self.stopGame()
                break
            elif xx in [0,1,2] and yy in [0,1,2]: # проверяем, что сюда не просочилась 10
               self.map.add_sign(xx, yy, gamer.sign) # метод добавления знака в матрицу по заданным индексам
               self.map.show_matrix() # вывод матрицы с ходами игроков
               if self.map.checkIfVin(xx, yy, gamer.sign):
                   print(f"Игрок {gamer.name} выиграл.")
                   self.stopGame()
                   break
            else:
                print("Что-то пошло не так. Попробуйте еще раз")


    def stopGame(self):
        print("Игра окончена")

