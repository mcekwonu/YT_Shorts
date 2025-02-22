#
# www.youtube.com/@mersthub_mentors
#

import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO
m = GEKKO(remote=True)

Nt = 51
m.time = np.linspace(0, 1, Nt)
tf = np.zeros_like(m.time)
tf[-1] = 1
tf = m.Param(tf)

u = m.MV(lb=-4, ub=10)
u.STATUS = 1
x1 = m.Var(value=0)
x2 = m.Var(value=-1)
x3 = m.Var(value=-m.sqrt(5))
x4 = m.Var(value=0)

m.options.IMODE = 6
m.options.NODES = 4
m.options.SOLVER = 3

m.Equations([x1.dt() == x2,
             x2.dt() == -x3 * u + 16 * tf - 8,
             x3.dt() == u,
             x4.dt() == x1 ** 2 + x2 ** 2 + 0.0005*(x2+16*tf-0.1*x3*u**2)**2])

m.Minimize(x4 * tf)
m.solve()

plt.figure()
plt.plot(m.time, u, "go", label="u")
plt.xlim(xmin=0)
plt.xlabel("Time")
plt.ylabel("Values")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("manipulated_var.png", dpi=600)

plt.figure()
plt.plot(m.time, x1.value, "r>", label=r"$x_1$")
plt.plot(m.time, x2.value, "bo", label=r"$x_2$")
plt.plot(m.time, x3.value, "k*", label=r"$x_3$")
plt.plot(m.time, x4.value, "g^", label=r"$x_4$")
plt.xlim(xmin=0)
plt.xlabel("Time")
plt.ylabel("Values")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("decision_var.png", dpi=600)

plt.show()

