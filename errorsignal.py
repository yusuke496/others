import numpy as np
from scipy import integrate
import scipy
import matplotlib.pyplot as plt
import math
from numpy import exp,loadtxt,pi,sqrt

data = loadtxt("errorsignal.txt")
x = data[:,0]
y = data[:,1]

plt.xlabel("time (sec)")
plt.ylabel("error signal (V)")
plt.plot(x,y,linewidth=0.5,color="black")
#plt.ylim(-5,5)
#plt.xlim(0,40)
#plt.legend(loc='upper right')
plt.show()
