#This is a program to calculate problem 3.8
"""
Nonlinear Pendulum
"""
import numpy as np
from pylab import *
from math import *
theta=[]
w=[]#omega
t=[]
theta_=[]#theta of linear pendulum
w_=[]#omega of linear pendulum
"""
input
"""
#parameter
g=9.8 #local gravitational acceleration of Earth(m*s^(-2))
l=1 #(m)
theta0=pi*float(input('theta0(degree)='))/180
theta.append(theta0)
w0=float(input('omega0(rad/s)='))
w.append(w0)
t.append(0.0)
time=16*pi*sqrt(l/g)
dt=float(input('time step='))
#linear pendulum
theta_.append(theta0)
w_.append(w0)
'''
calculation
'''
f=open('problem3.8.txt','w')
for i in range(int(time/dt)):
    w.append(w[i]+dt*(-g/l*sin(theta[i])))
    theta.append(theta[i]+dt*w[i+1])
    t.append(t[i]+dt)
    w_.append(w_[i]+dt*(-g/l*theta_[i]))
    theta_.append(theta_[i]+dt*w_[i+1])
    print t[-1],theta[-1],theta_[-1]
    print >> f,t[-1],theta[-1],theta_[-1]
f.close()
'''
plot
'''
plot(t,theta,color='blue')
plot(t,theta_,'--',color='red')
legend(('nonlinear pendulum','linear pendulum'),'upper right')
title('Nonlinear Pendulum and Linear Pendulum',fontsize=20)
xlabel('t(s)')
xlim(0,t[-1])
ylabel('theta(rad)')
savefig('problem3.8.png')
show()
#Phase diagram
plot(w,theta,color='blue')
plot(w_,theta_,'--',color='red')
legend(('nonlinear pendulum','linear pendulum'),'upper right')
title('phase diagram',fontsize=20)
xlabel('omega(rad/s)')
ylabel('theta(rad)')
savefig('problem3.8 phase diagram.png')
show()
