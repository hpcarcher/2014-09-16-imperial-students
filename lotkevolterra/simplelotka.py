import numpy as np
from matplotlib import pyplot as plt
a = 1.0
b = 0.1
c = 1.5
d = 0.75
def dX_dt(X, t):
   return np.array([ a*X[0] - b*X[0]*X[1] , -c*X[1] + d*b*X[0]*X[1] ])
t = np.linspace(0, 20, 2000)
X_initial = np.array([20, 4])
from scipy import integrate
X = integrate.odeint(dX_dt, X_initial, t)
prey = X[:, 0]
predators = X[:, 1]
fig = plt.figure()
plt.plot(t, prey, 'r-', label='Prey')
plt.plot(t, predators, 'b-', label='Predators')
plt.grid()
plt.legend(loc='best')
plt.xlabel('time')
plt.ylabel('population')
plt.title('Evolution of predator and prey populations')
plt.show()
