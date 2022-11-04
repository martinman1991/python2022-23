import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 16])
ypoints = np.array([0, 25])

plt.plot(xpoints, ypoints)
plt.plot([10,20,12],[32,10,12])
plt.show()

x=[0,50,50,0,0]
y=[0,0,50,50,0]
