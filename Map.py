
class Map:
    def __init__(self):
        self.matrix=[['_','_','_'],['_','_','_'],['_','_','_']]
        self.countMoves=9
    def add_sign(self,i,j,sign):
        if self.matrix[i][j]=='_':
            self.matrix[i][j]=sign
            self.countMoves-=1
        else:
            print("Такой ход невозможен, попробуйте еще раз")


    def show_matrix(self):
        for i in self.matrix:
            for j in i:
                print(j, end=' ')
            print()

    def checkIfVin(self, ii, jj, sign):
        flag=False
        if ii==jj:
            if (self.matrix[0][0]==sign and self.matrix[2][2]==sign and self.matrix[1][1]==sign)or(self.matrix[1][1]==sign and self.matrix[2][0]==sign and self.matrix[0][2]==sign):
                flag=True
                return flag
        if (ii==0 and jj==2) or (ii==2 and jj==0):
            if self.matrix[0][2]==sign and self.matrix[2][0]==sign and self.matrix[1][1]==sign:
                flag=True
                return flag

        if self.matrix[ii][0]==sign and self.matrix[ii][1]==sign and self.matrix[ii][2]==sign:
            flag = True
            return flag
        if self.matrix[0][jj]==sign and self.matrix[1][jj]==sign and self.matrix[2][jj]==sign:
            flag = True
            return flag
        return flag
