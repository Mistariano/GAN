__author__ = 'MisT'

from neunet.neuralnet import NeuralNet
from ganuelayer import GANueLayer

class GANueNet(NeuralNet):
    def change(self,probability,max):
        cnt=0
        for i in self.nls:
            cnt+=i.change(probability=probability,max=max)
        return cnt

    def setit(self):
        self.nls.append(GANueLayer(N=self.per_L[0],I=self.per_L[0]))
        for i in range(1,self.num):
            self.nls.append(GANueLayer(N=self.per_L[i],I=self.per_L[i-1]))

        if self.cnt==-1:
            self.cnt=self.per_L[0]*(self.per_L[0]+1)
            for i in range(1,self.num):
                self.cnt+=self.per_L[i]*(self.per_L[i-1]+1)