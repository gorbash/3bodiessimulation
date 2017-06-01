from simulation import  Simulation
from simulation import  Mass


m1 = Mass(1, [0, 8], [-0.3, 0.1])
m2 = Mass(20, [0, 0], [0.1, 0])
m3 = Mass(1, [1, 30], [0,0])
s = Simulation([m1, m2, m3])