from scipy.integrate import odeint
import numpy as np
import math
import matplotlib.pyplot as plt

def odes(x, t):
    
    # assign each ODE to a vector element
    X = x[0]
    Y = x[1]
    Alpha = x[2]

    # constants
    v = 10        # cm/s
    Xdes = 4      # cm 
    Ydes = 3      # cm
    kAlpha = 10    # k > (v/Radius) = 2
   
    bearing = math.atan2((Ydes-Y),(Xdes-X)) 
    print(bearing)

    # define each ODE
    dXdt = v*np.cos(Alpha) 
    dYdt = v*np.sin(Alpha)
    #dAlphadt = -kAlpha*np.sign(Alpha-bearing)   #np.sign is signum function
    dAlphadt = -kAlpha*(Alpha-bearing)   
    
    #print("t: "+str(t)+"; Alpha: "+str(Alpha)+"; Alpha_dot: "+str(dAlphadt))

    return [dXdt, dYdt, dAlphadt]

# initial conditions
x0 = [0, 0, 0]

# test the defined odes
print(odes(x=x0,t=0))

# declare a time vector (time window)
t = np.linspace(0,10,100)

x = odeint(odes,x0,t)

X = x[:,0]
Y = x[:,1]
Alpha = x[:,2]

# plot the results
figure, axis = plt.subplots(2, 2)

# Y vs X 
axis[0, 0].plot(X, Y)
axis[0, 0].set_title("Y vs X")
  
# Alpha with time
axis[1, 0].plot(t, Alpha)
axis[1, 0].set_title("Alpha vs t")
  
# Y with time
axis[0, 1].plot(t, Y)
axis[0, 1].set_title("Y vs t")
  
# X with time
axis[1, 1].plot(t, X)
axis[1, 1].set_title("X vs t")
  
# Combine all the operations and display
plt.show()


