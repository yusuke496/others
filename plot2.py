from numpy import exp,loadtxt,pi,sqrt
import matplotlib.pyplot as plt
from lmfit import Model

def ML(x,a0,x0,a1,x1,a2,x2,a3,x3,sig,wid) :
    return a0*(x-x0)/((x-x0)**2+sig**2)**2+a1*(x-x1)/((x-x1)**2+sig**2)**2+a2*(x-x2)/((x-x2)**2+sig**2)**2-(a3/(sqrt(2*pi)*wid))*exp(-(x-x3)**2/(2*wid**2))*2*(x-x3)/(2*wid**2)

data = loadtxt("C:/Users/yusuke/Documents/codes/python/497nmFM.txt")
x = data[:,0]
y = data[:,1]

gmodel = Model(ML)
result = gmodel.fit(y,x=x,a0=-20000,x0=1,a1=-1000,x1=-50,a2=-500,x2=1220,a3=-1000000,x3=1,sig=10,wid=500)
plt.title("FM spectroscopy at 497 nm")
plt.xlabel("frequency (MHz)")
plt.xlim(-1500, 1500)
plt.ylim(-3, 3)
#plt.grid()
print(result.fit_report())
plt.ylabel("Lock in signal (V)")
plt.plot(x, y, linewidth=1, color="black")
#plt.plot(x, result.init_fit, linewidth=1, color="blue")
plt.plot(x, result.best_fit, linewidth=1, color="red")
plt.show()
