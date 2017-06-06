from simulation import  Simulation
from simulation import  Mass

# mass
# initial location (x,  y)
# initial velocity (vx, vy)

m1 = Mass(100,
          [0,       20],
          [0.1,     0])
m2 = Mass(100,
          [0,       -20],
          [-0.1,    0])
m3 = Mass(0.1,
          [10,       40],
          [-0.2,       0])

m4 = Mass(1,
          [5, -50],
          [-0.1,       0.1])

s = Simulation([m1, m2, m3])



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
