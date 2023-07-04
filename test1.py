import multiprocessing
from joblib import Parallel, delayed
from time import time
from math import sqrt
def func0(n):
    return sum([i*n for i in range(100000)])
result=0
core=8
number=10000
start = time()
if __name__=='__main__' :
    result = Parallel(n_jobs=core)(delayed(func0)(n) for n in range(number))
    print(sum(result),time()-start,core)
