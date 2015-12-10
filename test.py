__author__ = 'MisT'

from contrib import *


nn1=GANueNet(3,[2,2,2])
# nn1.test()
# print '======'
# nn2=GANueNet(3,[2,2,2])
# nn2.test()
# print '======'
# nn3=merge(nn1,nn2,getGene(18))
# nn3.test()
# print nn3.change(probability=0.1,max=0.1)
# nn3.test()
print nn1.workout([1,0])