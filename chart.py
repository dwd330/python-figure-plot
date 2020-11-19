import matplotlib.pyplot as plt
import numpy as np
import math

#speed
n=16
f=0.9
r=4
qr=math.sqrt(r)

#symetric speedup
s=1/((1-f)/qr + (f*r)/(qr*n))
print(s)

#asymetric speedup
s2=  (1-f)/qr + f/(qr+n-r)
print(1/s2) 

#dynmic speedup
s3=  (1-f)/qr + f/n
print(1/s3) 


#plot 1:
R1 = np.array([1, 2, 16]) #x_axis

#AT F=0.5
x1 = np.array([1.8, 2.5,4])
#AT F=0.9
x2 = np.array([6.4, 6.6, 4,])
#AT F=0.975
x3 = np.array([11.6, 9.6, 4])

plt.subplot(1, 2, 1)
plt.plot(R1, x1 ,label="f=0.5")
plt.plot(R1, x2, linestyle = 'dashed' ,label="f=0.9")
plt.plot(R1, x3 ,label="f=0.975")
plt.title("n=16")
plt.xlabel("BCEs ")
plt.ylabel("speed")

plt.legend()


#plot 2:
R2 = np.array([16, 32, 256])  #x_axis

#AT F=0.5
x1 = np.array([7.5, 10,16 ])
#AT F=0.9
x2 = np.array([25.6, 26.6, 16])
#AT F=0.975
x3 = np.array([46.5, 38.5, 16])

plt.subplot(1, 2, 2)
plt.plot(R2, x1,label="f=0.5")
plt.plot(R2, x2 ,linestyle = 'dashed' ,label="f=0.9")
plt.plot(R2, x3 ,label="f=0.975")
plt.title("n=256")
plt.xlabel("BCEs ")
plt.ylabel("speed")
plt.legend()

plt.show()