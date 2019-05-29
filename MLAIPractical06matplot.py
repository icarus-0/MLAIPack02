import matplotlib.pyplot as plt

x = [2,3,4,5,6,7]
y = [4,9,16,25,36,49]

plt.plot(x,y,marker='s',markerfacecolor='red',markersize=15,linestyle='dashed',color='blue')

plt.title("number with squr")

plt.xlabel("---------x",fontsize=14,color='blue')
plt.ylabel("-----------y",fontsize=14,color='red')

plt.axis([1,8,3,50])

plt.grid(True)
plt.annotate('square of 5',xytext=(3,40),xy=(5,25),arrowprops=dict(facecolor='black',shrink=.1))

plt.show()
