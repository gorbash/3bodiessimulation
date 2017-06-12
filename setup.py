from simulation import  Simulation
from simulation import  Mass

# mass
# initial location (x,  y)
# initial velocity (vx, vy)

m1 = Mass(100,
          [0,       0],
          [0,     0])
m2 = Mass(3,
          [0.2,       4],
          [0,    -0.1])
m3 = Mass(10,
          [0,       60],
          [-2,       0])
m4 = Mass(10,
          [20, 40],
          [-2,       0])


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
