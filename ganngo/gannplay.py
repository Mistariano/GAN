#coding=utf8

__author__ = 'MisT'


from goplay.contrib import *
from ganeunet.contrib import *
import os

class GANNPlay(GoPlay):
    def __init__(self,size,nnb,nnw):
        GoPlay.__init__(self,size=size)
        self.nn_b=nnb
        self.nn_w=nnw


    def get_xy(self):
        if self.nextPlayer:
            color=GoPoint.BLACK
        else:
            color=GoPoint.WHITE
        inputs=[]
        for xx in range(1,self.MAX):
            for yy in range(1,self.MAX):
                if self.board[xx][yy].qi>=0:
                    if self.board[xx][yy].color==color:
                        inputs.append(1)
                    else:
                        inputs.append(2)
                else:
                    inputs.append(self.board[xx][yy].color)
                # else:
                #     if self.board[xx][yy].color==GoPoint.NULL
                #         inputs.append(0)
                #     else:
                #         inputs.append(3)
        print inputs
        if self.nextPlayer:
            ans = self.nn_b.workout(input=inputs)
        else:
            ans = self.nn_w.workout(input=inputs)
        max=-1
        index=-1
        for i in range(0,len(ans)):
            if not inputs[i]:
                if max<ans[i]:
                    max=ans[i]
                    index=i
        if max==-1:
            print 'isitover?'
            os.system('pause')
        self.x=index/self.size+1
        self.y=index%self.size+1
    def output(self):
        draw=self.draw()
        print
        print' ',
        for i in range(1,self.MAX):
            print 10+i,
        print
        cnt=1
        for i in draw:
            print cnt,
            cnt+=1
            for j in i:
                if j==1:
                    print u'○',
                if j==2:
                    print u'●',
                if j==0:
                    print '..',
            print
        self.output_qi()

        #os.system('pause')

    def output_qi(self):
        draw=self.draw()
        print
        print' ',
        for i in range(1,self.MAX):
            print i,
        print
        cnt=1
        for i in range(1,self.MAX):
            print i,
            for j in range(1,self.MAX):
                    print self.board[i][j].qi,
            print

if __name__=='__main__':
    nn1=GANueNet(3,[25,100,25])
    play=GANNPlay(size=5,nnb=nn1,nnw=nn1)
    play.loop()

