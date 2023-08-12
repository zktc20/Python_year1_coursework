#1b COMPUTING COURSEWORK APRIL 2022
import numpy as np
import matplotlib.pyplot as plt

def dev_p(x):
    return (np.exp(x)*(5-x))-5

xvalues=np.linspace(-1,5,100)
yvalues=dev_p(xvalues)

plt.axhline(0, color='black',lw=0.5)
plt.plot(xvalues,yvalues)
plt.xlabel("x values",fontsize=12)
plt.ylabel("dp/dx",fontsize=12)
plt.savefig("q1 graph")
plt.show()



error=10**-10

def dev_p(x):
    return (np.exp(x)*(5-x))-5


def secdev_p(x):
    return (4-x)*np.exp(x)
            
def newtonraphson(x0):
    error=10**(-10)
    for i in range(1000):
        xn = x0 - (dev_p(x0)/secdev_p(x0))
        if abs(xn-x0)<error:
            break
        x0=xn
    return xn

print(newtonraphson(4.5))

h=6.626E-34
c=299792458
k= 1.3806503E-23

constant=((h*c))/(k*newtonraphson(4.5))
print(constant)
