from scipy.integrate import solve_ivp
import numpy as np
import math
import matplotlib.pyplot as plt

def odes(t, x):
    
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

    # define each ODE
    dXdt = v*np.cos(Alpha) 
    dYdt = v*np.sin(Alpha)
    diff = math.atan2(Alpha-bearing,1)
    dAlphadt = -kAlpha*np.sign(diff)   #np.sign is signum function
    #dAlphadt = -kAlpha*(Alpha-bearing)   
    
    print(str(t)+" sec")
    #print("t: "+str(t)+"; Alpha: "+str(Alpha)+"; Alpha_dot: "+str(dAlphadt))

    return [dXdt, dYdt, dAlphadt]

# initial conditions
x0 = [0, 0, 0]

# test the defined odes
print(odes(x=x0,t=0))

print("Desired yaw: "+str(45.0*np.pi/180.0))

# declare a time vector (time window)
#t = np.linspace(0,1,100)

#sol = solve_ivp(odes, (0, 100), x0, t_eval=np.linspace(0, 100, 100))
sol = solve_ivp(odes, (0, 100), x0)
x=sol.y
X = x[0]
Y = x[1]
Alpha = x[2]

print(len(X))
#print(X)
#print(Y)
#for i in range(len(X)):
#    print(str(X(i))+", "+str(Y(i))+"\n")


t = sol.t

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
plt.axis("scaled")
plt.show()


