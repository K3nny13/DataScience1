import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,10,20)
y = x ** 2




# Labelling
# plt.xlabel("X label")
# plt.ylabel("Y label")

# adding multiple plots
# plt.subplot(1,2,1)
# plt.plot(x,y,'r')
#
# plt.subplot(1,2,2)
# plt.plot(y,x,'b')

# Object Orientated
fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x, y)
axes2.plot(y, x)

# OO Titles
axes1.set_title("Large Plot")
axes2.set_title("Small Plot")

# OO labels
axes2.set_xlabel("X Label")
axes2.set_ylabel("Y Label")

# displaying the plot
plt.show()
