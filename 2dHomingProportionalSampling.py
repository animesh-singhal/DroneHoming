from scipy.integrate import odeint
import numpy as np
import math
import matplotlib.pyplot as plt

def odes(x, t):
    
    # assign each ODE to a vector element
    X = x[0]
    Y = x[1]
    Alpha = x[2]
   
    # Bearing already calculated previously
    
    # define each ODE
    dXdt = v*np.cos(Alpha) 
    dYdt = v*np.sin(Alpha)
    #dAlphadt = -kAlpha*np.sign(Alpha-bearing)   #np.sign is signum function
    dAlphadt = -kAlpha*(Alpha-bearing)   
    
    #print("t: "+str(t)+"; Alpha: "+str(Alpha)+"; Alpha_dot: "+str(dAlphadt))

    return [dXdt, dYdt, dAlphadt]

# constants
v = 10        # cm/s
Xdes = 4      # cm 
Ydes = 3      # cm
kAlpha = 10    # k > (v/Radius) = 2

# parameters related to time
simTime = 10 #sec
sampleTime = 1 #sec
iterPerSampleTime = 10

# initial conditions
X_init = 0
Y_init = 0
Alpha_init = 0
xInitial = np.array([[X_init, Y_init, Alpha_init]])

xSol = xInitial 
tSol = [0]

for i in range (0, simTime, sampleTime): 
    delTime = [i, i+sampleTime] 
    
    x0 = xSol[-1,:]      #last row of xSol matrix
    
    X = x0[0]
    Y = x0[1]
    
    bearing = math.atan2((Ydes-Y),(Xdes-X)) 
    
    t = np.linspace(i, i+sampleTime, iterPerSampleTime)   # i <= t <= i+sampleTime 
    
    xInterval = odeint(odes,x0,t)                        # xInterval will include x(@i) and x(@i+sampleTime)
    
    # While appending solutions to master arrays, removing 1st elements as they'll be appended as the 'last element of previous iteration'
    xSol = np.vstack((xSol, xInterval[1:,:]))  #stacking new solutions (except the first row) over previous solutions
    tSol = np.hstack((tSol, t[1:]))            #stacking new array without its first element to the previous array

X = xSol[:,0]
Y = xSol[:,1]
Alpha = xSol[:,2]


# plot the results
figure, axis = plt.subplots(2, 2)

# Y vs X 
axis[0, 0].plot(X, Y)
axis[0, 0].set_title("Y vs X")
  
# Alpha with time
axis[1, 0].plot(tSol, Alpha)
axis[1, 0].set_title("Alpha vs t")
  
# Y with time
axis[0, 1].plot(tSol, Y)
axis[0, 1].set_title("Y vs t")
  
# X with time
axis[1, 1].plot(tSol, X)
axis[1, 1].set_title("X vs t")
  
# Combine all the operations and display
plt.show()


