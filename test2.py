from time import time
from math import sqrt
def func0(n):
    return sum([i*n for i in range(100000)])
result=0
start = time()
number=10000
for i in range(number):
    result=result+func0(i)
print(result,time()-start)
