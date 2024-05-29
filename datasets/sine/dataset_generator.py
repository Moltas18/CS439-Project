import matplotlib.pyplot as plt
import numpy as np

num_steps = 10000
n = 4 #periods

X = np.linspace(0, n*2*np.pi, num=num_steps, endpoint=True)
Y = np.sin(X)

np.savetxt("sin.csv", Y, delimiter=",")

# np.savetxt("sin.csv", a, delimiter=",")

plt.plot(X,Y)
plt.show()