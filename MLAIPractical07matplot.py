import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0,5.0,0.2)
print(t)

plt.plot(t,t,'r*-',t,t+3,'bs-',t,t+6,'bo',t,t+6,'r-')
#plt.plot(t,t+6,marker='s',markerfacecolor='red',markersize=5,linestyle='dashed',color='blue')

plt.show()