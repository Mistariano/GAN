__author__ = 'MisT'

def merge(nn1,nn2,g):
    tar=nn1
    cur1=0
    cur2=0
    cur3=0
    for i in range(0,tar.cnt):
        if cur3>tar.nls[cur1].nns[cur2].num:
            cur3=0
            cur2+=1
        if cur2>=tar.nls[cur1].num:
            cur2=0
            cur1+=1
        if g&1:
            tar.nls[cur1].nns[cur2].weight[cur3]=nn2.nls[cur1].nns[cur2].weight[cur3]
        g>>=1
    return tar