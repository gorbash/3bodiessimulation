from simulation import  Simulation
from simulation import  Mass


m1 = Mass(1,                    # mass
          [0,       2],         # initial location (x,  y)
          [0.1,     0])         # initial velocity (vx, vy)
m2 = Mass(1,
          [0,       -2],
          [-0.1,    0])
m3 = Mass(1,
          [0,       30],
          [-0.01,     -0.01])

s = Simulation([m1, m2, m3])