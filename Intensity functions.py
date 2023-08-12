#Question 2a
import numpy as np
import matplotlib.pyplot as plt

def func(m,o,x):
    return np.cos((m*o)-(x*np.sin(o)))

a=0.0
b=np.pi


def trapezium(a,b,m,x):
    N=10000
    h=(b-a)/N
    fab=0.5*(func(m, a, x)+func(m, b, x))
    extra=0
    for k in range(1,N):
        extra+=func(m, a+k*h, x)
    return h*(fab+extra)

def J(m,x):
    return (1/np.pi)*trapezium(a, b,m,x)

x=np.linspace(0,21,1000)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

plt.plot(x,J(0,x),label="$J_0(x)$")
plt.plot(x,J(1,x),label= "$J_1(x)$")
plt.plot(x,J(2,x),label ="$J_2(x)$")
plt.xlabel("x values",fontsize=15)
plt.ylabel("Bessel Function $J_m(x)$",fontsize=15)
plt.legend()
plt.savefig("Bessel Graph")
plt.show()

#Q2b
r=np.linspace(-25E-6,25E-6,10000)
lambda_val=550E-9
x_val=(np.pi*r)/(10*lambda_val)
I_0=1.0

def Intensity(x_val):
    return I_0*((2*J(1,x_val)/x_val))**2

plt.plot(r,Intensity(x_val))
plt.axhline(color='black', lw=0.5)
plt.axvline(color='black', lw=0.5)
plt.xlabel("Distance from the central fringe (m)",fontsize=10)
plt.ylabel("Intensity of Light (W/$m^2$)",fontsize=10)
plt.savefig("Diffraction Pattern")
plt.show()
