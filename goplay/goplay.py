__author__ = 'MisT'

from gopoint import GoPoint

class GoPlay:

    def __init__(self, size):
        self.size = size
        self.MIN=0
        self.MAX=self.size+1
        # self.board=[[0 for j in range(0,size+2)]for i in range(0,size+2)]
        self.board=[[GoPoint(x=i,y=j,color=GoPoint.NULL) for j in range(0,self.MAX+1)]for i in range(0,self.MAX+1)]
        #print board
        for i in range(self.MIN,self.MAX+1):
            # self.board[self.MIN][i] = GoPlay.WALL
            # self.board[self.MAX][i] = GoPlay.WALL
            # self.board[i][self.MAX] = GoPlay.WALL
            # self.board[i][self.MIN] = GoPlay.WALL
            self.board[self.MIN][i].become_wall()
            self.board[self.MAX][i].become_wall()
            self.board[i][self.MAX].become_wall()
            self.board[i][self.MIN].become_wall()
        # self.group=[[[i,j]for j in range(1,self.MAX)]for i in range(1,self.MAX)]

    def loop(self):
        self.nextPlayer=True
        while not self.end():
            self.get_xy()
            # self.get_x()
            # self.get_y()
            self.move()
            # self.scan()
            self.output()
            self.nextPlayer=not self.nextPlayer

    def get_x(self):
        self.x=input('x:')

    def get_y(self):
        self.y=input('y:')

    def get_xy(self):
        self.get_x()
        self.get_y()

    def move(self):
        if self.nextPlayer:
            while\
                self.board[self.x][self.y].color!=GoPoint.NULL\
            and\
                self.board[self.x][self.y].color!=GoPoint.WHITE_FORBIDDENED\
            :
                print 'You can not move here'
                self.get_xy()
            color=GoPoint.BLACK

        else:
            while\
                self.board[self.x][self.y].color!=GoPoint.NULL\
            and\
                self.board[self.x][self.y].color!=GoPoint.BLACK_FORBIDDENED\
            :
                print 'You can not move here'
                self.get_xy()
            color=GoPoint.WHITE

        self.board[self.x][self.y].move(color=color)

        for i in [[self.x+1,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]:
            if self.board[i[0]][i[1]].color==color:
                self.group_union(g1=[self.x,self.y],g2=i)
            elif self.board[i[0]][i[1]].qi>0:
                self.board[i[0]][i[1]].qi-=1
                # print 'check',self.group_check(g=i)
                self.group_check(g=i)
        for i in [[self.x+1,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]:
            if self.board[i[0]][i[1]].qi<0:
                self.board[self.x][self.y].qi+=1
                # print'plus',i
        # print 'qi:',self.board[self.x][self.y].qi

    # def scan(self):
    #     pass

    def end(self):
        return False

    def group_find(self,g):
        if self.board[g[0]][g[1]].group==g:
            return g
        self.board[g[0]][g[1]].group=self.group_find(self.board[g[0]][g[1]].group)
        return self.board[g[0]][g[1]].group

    def group_union(self,g1,g2):
        group1=self.group_find(g=self.board[g1[0]][g1[1]].group)
        group2=self.group_find(g=self.board[g2[0]][g2[1]].group)
        self.board[group1[0]][group1[1]].group=group2
        self.board[group2[0]][group2[1]].member.append(group1)

    def group_check(self,g):
        g=self.group_find(g=g)
        queue=[g]
        i=0
        while i<len(queue):
            for t in self.board[queue[i][0]][queue[i][1]].get_member():
                queue.append(t)
            i+=1
        for group in queue:
            if self.board[group[0]][group[1]].qi>0:
                return 0
        for group in queue:
            self.board[group[0]][group[1]].die()
        return 1
    def draw(self):
        return [[self.board[i][j].output() for j in range(1,self.MAX)]for i in range(1,self.MAX)]

    def output(self):
        # for i in range(1,self.MAX):
        #     for j in range(1,self.MAX):
        #         #print self.board[i][j],
        #         self.board[i][j].output()
        #     print
        print self.draw()

if __name__ == '__main__':
    a=GoPlay(19)
    a.output()
    a.loop()

