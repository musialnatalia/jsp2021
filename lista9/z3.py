import numpy as np
import matplotlib.pyplot as plt

#v0 = float(input("Podaj prędkość początkową v0 [m/s]: "))
#a = float(input("Podaj kąt rzutu alpha w stopniach: "))
v0=30
a=50
a = a*np.pi/180.
g = 9.81

t = 2*v0*np.sin(a)/g
z = v0**2/g * np.sin(2*a)
h = v0**2*np.sin(a)**2/(2*g)

tim = np.linspace(0,t,100)


vx = v0*np.cos(a)
vy = abs(v0*np.sin(a) - g*tim)
x = vx*tim
y = v0*np.sin(a)*tim-g*tim**2/2.

print('Czas lotu: '+str(t)+' s \nZasięg rzutu: '+str(z)+' m \nMaksymalna wysokość: '+str(h)+' m')

fig = plt.figure(figsize=(12,10))

ax1 = fig.add_subplot(131)
ax1.title.set_text(r'Prędkość pozioma $v_x$ i pionowa $v_y$')
ax1 = plt.plot(tim,np.full(tim.shape,vx),label=r'$v_x$')
ax1 = plt.plot(tim,vy,label=r'$v_y$',color='red')
ax1 = plt.legend(loc='best')
ax1 = plt.xlabel('Czas [s]')
ax1 = plt.ylabel('Prędkość [m/s]')

ax2 = fig.add_subplot(132)
ax2.title.set_text('Położenie')
ax2 = plt.plot(tim,x,color='black')
ax2 = plt.xlabel('Czas [s]')
ax2 = plt.ylabel('Odległość [m]')

ax3 = fig.add_subplot(133)
ax3.title.set_text('Tor rzutu')
ax3 = plt.plot(tim,y,color='darkgreen')
ax3 = plt.xlabel('Czas [s]')
ax3 = plt.ylabel('Wysokość [m]')
plt.suptitle('Rzut ukośny',fontsize=20)
plt.show()
