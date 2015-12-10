__author__ = 'MisT'

import random


def getGene(n):
    ans=0
    for i in range(0,n):
        ans+=random.randrange(0,2)
        ans<<=1
    return ans
