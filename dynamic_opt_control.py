#
# www.youtube.com/@mersthub_mentors
#


import json as json
import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO

m = GEKKO()
m.time = np.linspace(0,20,41)

# Parameters
mass = 500
b = m.Param(value=50)
K = m.Param(value=0.8)

# Manipulated variable
p = m.MV(value=0, lb=0, ub=100)
p.STATUS = 1
p.DCOST = 0.1
p.DMAX = 20

# Controlled Variable
v = m.CV(value=0)
v.STATUS = 1
m.options.CV_TYPE = 2
v.SP = 40
v.TR_INIT = 1
v.TAU = 5

# Process model
m.Equation(mass*v.dt() == -v*b + K*b*p)

m.options.IMODE = 6
m.solve(disp=True)

# get additional solution information
with open(f"{m.path}//results.json") as f:
    results = json.load(f)

plt.figure()
plt.subplot(2,1,1)
plt.plot(m.time,p.value,"b-",label="MV Optimized")
plt.legend()
plt.ylabel("Input")

plt.subplot(2,1,2)
plt.plot(m.time,results["v1.tr"], "k-", label="Reference Trajectory")
plt.plot(m.time, v.value, "r--", label="CV Response")
plt.ylabel("Output")
plt.xlabel("Time")
plt.legend(loc="best")
plt.show()