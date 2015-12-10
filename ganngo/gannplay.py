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
            unfrbidn=GoPoint.WHITE_FORBIDDENED
            color=GoPoint.BLACK

        else:
            unfrbidn=GoPoint.BLACK_FORBIDDENED
            color=GoPoint.WHITE
        inputs=[]
        for xx in range(1,self.MAX):
            for yy in range(1,self.MAX):
                if self.board[xx][yy].qi>0:
                    if self.board[xx][yy].color==color:
                        inputs.append(1)
                    else:
                        inputs.append(2)
                else:
                    if self.board[xx][yy].color==GoPoint.NULL\
                    or self.board[xx][yy].color==unfrbidn:
                        inputs.append(0)
                    else:
                        inputs.append(3)
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
        self.x=index/self.size+1
        self.y=index%self.size+1
    def output(self):
        draw=self.draw()
        for i in draw:
            for j in i:
                if j==1:
                    print u'○',
                if j==2:
                    print u'●',
                if j==0:
                    print '..',
            print
        os.system('pause')

if __name__=='__main__':
    nn1=GANueNet(3,[49,100,49])
    play=GANNPlay(size=7,nnb=nn1,nnw=nn1)
    play.loop()

