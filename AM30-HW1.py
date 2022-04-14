import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.signal import find_peaks_cwt

def equation(x, y):
    
    exponent = (x*x) + (y*y)
    exponent = exponent/100;
    exponent = -exponent
    return math.e**exponent
x = np.arange(0, (math.sqrt(5)/4), 0.01)
y = np.arange(0, (math.sqrt(5)/4), 0.01)
x = [-10 + 8*math.sqrt(5)*i for i in x]
y = [-10 + 16*math.sqrt(5)*i for i in y]
h = list()
found_max = 0
for ind in range(0, len(x)):
    h.append(equation(x[ind], y[ind]))
    if (equation(x[ind], y[ind]) > found_max):
        found_max = equation(x[ind], y[ind])
        print("X and Y at max: ", x[ind], y[ind])
print(x[0], x[len(x)-1])
print(y[0], y[len(y)-1])
print(max(h))
plt.plot(h)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) 
plt.ylabel("height")
plt.show()
        
