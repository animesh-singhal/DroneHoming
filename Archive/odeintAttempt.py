from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

def odes(x, t):
    
    # assign each ODE to a vector element
    X = x[0]
    Y = x[1]
    Alpha = x[2]
    Alpha = math.atan2(np.sin(Alpha),np.cos(Alpha))

    # constants
    v = 1        # cm/s
    Xdes = 40    # cm 
    Ydes = 30      # cm
    kAlpha = 2   # k > (v/Radius) = 2
    
    bearing = math.atan2((Ydes-Y),(Xdes-X)) 
    relbearing = Alpha-bearing
    relbearing = math.atan2(np.sin(relbearing), np.cos(relbearing))

    # define each ODE
    dXdt = v*np.cos(Alpha) 
    dYdt = v*np.sin(Alpha)
    dAlphadt = -kAlpha*np.sign(relbearing)   #np.sign is signum function
    
    #print("t: "+str(t)+"; Alpha: "+str(Alpha)+"; Alpha_dot: "+str(dAlphadt))
    
    return [dXdt, dYdt, dAlphadt]

# initial conditions
x0 = [0, 0, 0]


# declare a time vector (time window)
t = np.linspace(0,10,101)
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


