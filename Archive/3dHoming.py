from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def odes(x, t):
    # constants
    v = 1
    AlphaDes = 45.0*np.pi/180.0
    kAlpha = 1
    BetaDes = 30.0*np.pi/180.0
    kBeta = 1
    
    # assign each ODE to a vector element
    X = x[0]
    Y = x[1]
    Z = x[2]
    Alpha = x[3]
    Beta = x[4]

    # define each ODE
    dXdt = v*np.cos(Alpha)*np.cos(Beta) 
    dYdt = v*np.sin(Alpha)*np.cos(Beta)
    dZdt = v*np.sin(Beta)
    #dAlphadt = -k*np.sign(Alpha-theta)   #np.sign is signum function
    dAlphadt = -kAlpha*(Alpha-AlphaDes)
    dBetadt = -kBeta*(Beta-BetaDes)

    return [dXdt, dYdt, dZdt, dAlphadt, dBetadt]

# initial conditions
x0 = [0, 0, 0, 0, 0]

# test the defined odes
print(odes(x=x0,t=0))
#print("Desired yaw: "+str(45.0*np.pi/180.0))

# declare a time vector (time window)
t = np.linspace(0,100,1000)
x = odeint(odes,x0,t)


X = x[:,0]
Y = x[:,1]
Z = x[:,2]
Alpha = x[:,3]
Beta = x[:,4]


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

