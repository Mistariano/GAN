__author__ = 'MisT'

from neunet.neurallayer import NeuralLayer
from ganeunode import GANeuNode

class GANueLayer(NeuralLayer):
    def change(self,probability,max):
        cnt=0
        for i in self.nns:
            cnt+=i.change(probability=probability,max=max)
        return cnt

    def setit(self):
        self.nns=[]
        for i in range(0,self.num):
            self.nns.append(GANeuNode(self.inputs))