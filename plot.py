import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('497nmFM.txt')
input0 = data[:,0]
output0 = data[:,1]

plt.title("FM spectroscopy at 497 nm")
plt.xlabel("frequency (MHz)")
plt.xlim(-1500, 1500)
plt.ylim(-3, 3)
#plt.grid()
plt.ylabel("Lock in signal (V)")
plt.plot(input0, output0, linewidth=1, color="black")
plt.show()
