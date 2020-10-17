import numpy as np
from matplotlib.pylab import plt
def projectile(angle, v0, time, cd=0):
    t = np.linspace(0,time,300)
    dt = t[1] - t[0] #s
    g = 9.8 # m/s2
    m = 1 # kg
    v0 = v0 # m/s
    vx = v0*np.cos(angle)
    vy = v0*np.sin(angle)
    y0 = 0
    x0 = 0
    vg = 0
    vy_list=[vy]
    vx_list=[vx]
    y_list = [y0]
    x_list = [x0]
    ax=0
    ay= -g
    acdy=0;
    acdx=0;

    for i in range(1, len(t)):
        fd=cd*v0**2
        tan=abs(vy/vx);
        fdy=fd*np.sin(np.arctan(tan))
        fdx=fd*np.cos(np.arctan(tan))
        acdx=-fdx;
        if (vy>0):
            acdy=-fdy*dt
        else:
            acdy=fdy*dt
        vg = ay * dt
        vy=vy+vg+acdy
        y0 += vy* dt
        if (vx>0):
            vx=vx+(acdx*dt)
        else :
            vx=0
        x0 += vx * dt
        if y0 > 0:
            y_list.append(y0)
            x_list.append(x0)
            vy_list.append(vy)
            vx_list.append(vx)
            v0=(vx**2+vy**2)**(0.5)
        else:
            break
    return x_list, y_list,vx_list,vy_list




x_list1,y_list1,vx_list,vy_list=projectile(np.pi/3,100,30)

plot1=plt.figure(1)
plt.plot(x_list1,y_list1)
plt.xlabel("x")
plt.ylabel("y")
x_list2,y_list2,vx_list2,vy_list2=projectile(np.pi/4,60,25)
plt.plot(x_list2,y_list2)
plt.title("Combine graph of two different projectiles without drag force")
plt.show()
range2=max(x_list2)
print (range2)


plot2=plt.figure(2)
x_list3,y_list3,vx_list3,vy_list3=projectile(np.pi/3,30,30,0.005)
plt.plot(x_list3,y_list3)
plt.xlabel("x")
plt.ylabel("y")
plt.title ("Graph of projectile with drag force")
plt.show()

t = np.linspace(0,30,300)
t=t[0:len(vx_list3)]
fig, (ax1,ax2)=plt.subplots(1,2)
ax1.plot(vx_list3,t)
ax2.plot(vy_list3,t)
ax1.set(xlabel="time", ylabel="x-component of velocity")
ax2.set(xlabel="time", ylabel="y-component of velocity")
fig.suptitle("x and y component of velocity vs time")
plt.show()




