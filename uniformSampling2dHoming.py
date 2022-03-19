from scipy.integrate import solve_ivp
import numpy as np
import math
import matplotlib.pyplot as plt

#def odes(x, t):
def odes(t, x):
    
    # assign each ODE to a vector element
    X = x[0]
    Y = x[1]
    Alpha = x[2]
    Alpha = math.atan2(np.sin(Alpha),np.cos(Alpha))
    
    # Bearing already calculated previously
    
    # define each ODE
    dXdt = v*np.cos(Alpha) 
    dYdt = v*np.sin(Alpha)
    dAlphadt = -kAlpha*np.sign(relbearing)   #np.sign is signum function
        
    #print("t: "+str(t)+"; Alpha: "+str(Alpha)+"; Alpha_dot: "+str(dAlphadt))
    return [dXdt, dYdt, dAlphadt]

# constants
v = 10        # cm/s
Xdes = 20      # cm 
Ydes = 70      # cm
kAlpha = 2    # k > (v/Radius) = 2

# parameters related to time
simTime = 20 #sec
sampleTime = 1 #sec
iterPerSample = 10

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
    Alpha = x0[2]
    
    bearing = math.atan2((Ydes-Y),(Xdes-X)) 
    relbearing = Alpha-bearing
    relbearing = math.atan2(np.sin(relbearing), np.cos(relbearing))
    
    tEval=np.linspace(i, i+sampleTime, iterPerSample+1)
    print(tEval)
    sol = solve_ivp(odes, (i, i+sampleTime), x0, t_eval=tEval)
    xInterval=sol.y                      # xInterval will include x(@i) and x(@i+sampleTime)
    xInterval=np.transpose(xInterval)    # each row should have a new set of values of x,y,alpha
    
    tInterval=sol.t                      # i <= t <= i+sampleTime
        
    # While appending solutions to master arrays, removing 1st elements as they'll be appended as the 'last element of previous iteration'
    xSol = np.vstack((xSol, xInterval[1:,:]))    #stacking new solutions (except the first row) over previous solutions
    tSol = np.hstack((tSol, tInterval[1:]))      #stacking new array without its first element to the previous array

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


