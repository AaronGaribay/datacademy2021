import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
def f(m, x, b):
    return m*x + b

res = 100
m = 10
b = 5

x = np.linspace(-10.0, 10.0, num=res)
y = f(m, x, b)
fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()