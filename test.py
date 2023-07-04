import numpy as np
import matplotlib.pyplot as plt
import time
i=0
iend=int(input("input iend:"))
x=np.array([i for i in range(0,iend)])
y=np.array([0 for i in range(0,iend)])
t1=np.array([0.0 for i in range(0,iend)])
t2=np.array([0.0 for i in range(0,iend)])
def fib(n) :
	if n < 2 :
		return n
	else :
		return fib(n-1) + fib(n-2)

start_time=time.perf_counter()
for i in range(1,iend+1):
	print(fib(i))
	time1=time.perf_counter()-start_time
	t1[i-1]=time1

i=0
i1=0
i2=1
i3=0

start_time=time.perf_counter()
y[0]=i2
time2=time.perf_counter()-start_time
t2[0]=time2
print(y[0])
for i in range(1,iend):
	i3=i1+i2
	i1=i2
	i2=i3
	y[i]=i3
	time2=time.perf_counter()-start_time
	t2[i]=time2
	print(i3)

#print('time diffeence :',time1-time2)
plt.plot(x,t1-t2)
#plt.ylim(0,100)
plt.show()
