class Gamer:
    def __init__(self,sign,name):
        self.sign=sign
        self.name=name

    def makeAMove(self):

        print(f"Игрок {self.name}:")
        while True:
            try:
                x,y=map(int,input().split('-'))
                if x not in [0,1,2,10] or y not in [0,1,2,10]:
                    print("Что-то пошло не так, попробуйте еще раз")
                else:
                    break
            except:
                print("Ошибка ввода. Попробуйте еще раз")
        return x,y




