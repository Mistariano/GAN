__author__ = 'MisT'

from neunet.neuralnode import NeuralNode
import random

class GANeuNode(NeuralNode):
    def change(self,probability,max):
        cnt=0
        for i in range(0,self.num+1):
            if random.uniform(0,1)<probability:
                print self.weight[i]
                self.weight[i]+=random.uniform(-max,max)
                print self.weight[i]
                if self.weight[i]<0:
                    self.weight[i]=0
                if self.weight[i]>1:
                    self.weight[i]=1
                cnt+=1
        return cnt
