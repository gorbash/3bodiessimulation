from simulation import  Simulation
from simulation import  Mass

# mass
# initial location (x,  y)
# initial velocity (vx, vy)

m1 = Mass(1,
          [5,       0],
          [0.01,     -0.01])
m2 = Mass(1,
          [-5,       0],
          [-0.01,    0])
m3 = Mass(1,
          [0,       5],
          [0.01,       0.2])

s = Simulation([m1, m2])



# ladne
#m1 = Mass(1,
#          [0,       2],
#          [0.1,     0])
#m2 = Mass(3,
#          [0,       -2],
#          [-0.1,    0])
#m3 = Mass(2,
#          [0,       30],
#          [0.05,       0])
