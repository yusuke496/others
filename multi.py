from multiprocessing import Pool
from math import sqrt
import numpy as np
import time

def pr(n):
    for i in range(2, int(sqrt(n)+1)) :
            if n%i==0 :
                return 0
                break
    else : return n

if __name__ == "__main__":
    num=int(input("number of core="))
    nini=int(input("initial number="))
    nfin=int(input("final number="))
    start = time.clock()
    p = Pool(num)
    result=[]
    result=p.map( pr, range(nini,nfin) )
    result=np.sort(result)
    result=np.trim_zeros(result)
    t=time.clock()-start
    print(len(result),t)
