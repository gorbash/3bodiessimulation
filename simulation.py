#!/usr/bin/python
from math import sqrt


class Mass:
    def __init__(self, mass, s, v):
        self.s = list(map(lambda x: float(x), s))
        self.v = list(map(lambda x: float(x), v))
        self.mass = float(mass)

    def __str__(self):
        return "mass = %0.2f s = [%0.3f %0.3f] v = [%0.3f %0.3f] |v|=%0.3f" % (self.mass, self.s[0], self.s[1], self.v[0], self.v[1], calculateVectorLen(self.v))

def calculateVectorLen(forceVec):
    ret = 0
    for el in forceVec:
        ret += el*el
    return sqrt(ret)

class Simulation:
    G = 0.1
    totalTime=0
    steps = 0

    def __init__(self, masses):
        self.masses = masses
        self.reportState()

    def __str__(self):
        return "Simulation got %d masses" % len(self.masses)

    def step(self, deltaT):
        netForces = self.calculateNetForces()
        accelarations = self.calculateAccelerations(netForces)
        self.calculateAndUpdateV(accelarations, deltaT)
        self.calculateAndUpdateS(deltaT)
        self.totalTime += deltaT
        self.steps += 1
        if (self.steps%50000 == 0):
            print("Total time: %s steps: %s" % (self.totalTime, self.steps))
            self.reportState()


    def calculateForce(self, mass, source):
        r = self.addVectors(source.s, self.multipleVectorByConst(mass.s, -1))
        rLen = calculateVectorLen(r)
        if rLen == 0:
            print("Got the same location for %s and %s" % (mass, source))
            return [0, 0]
        forceValue = (self.G*(mass.mass * source.mass)) / (rLen*rLen)
        ret = [(r[0] * forceValue)/rLen, (r[1] * forceValue)/rLen]
        return ret


    def multipleVectorByConst(self, vect, value):
        ret = []
        for el in vect:
            ret.append(el * value)
        return ret

    def addVectors(self, add1, add2):
        ret = []
        for (a1, a2) in zip(add1, add2):
            ret.append(a1 + a2)
        return ret

    def calculateNetForce(self, mass, others):
        ret = [0, 0]
        for m in others:
            force = self.calculateForce(mass, m)
            ret = self.addVectors(ret, force)
        return ret

    def calculateNetForces(self):
        ret = []
        for i in range(0, len(self.masses)):
            mass = self.masses[i]
            rest = self.masses[:i] + self.masses[i + 1:]
            ret.append(self.calculateNetForce(mass, rest))
        return ret

    def calculateAccelerations(self, netForces):
        ret = []
        for (f, m) in zip(netForces, self.masses):
            acceleration = self.multipleVectorByConst(f, 1 / (m.mass))
            ret.append(acceleration)
        return ret

    def calculateAndUpdateV(self, accelerations, deltaT):
        for (mass, acc) in zip(self.masses, accelerations):
            deltaV = self.multipleVectorByConst(acc, deltaT)
            mass.v = self.addVectors(mass.v, deltaV)

    def calculateAndUpdateS(self, deltaT):
        for mass in self.masses:
            deltaS = self.multipleVectorByConst(mass.v, deltaT)
            mass.s = self.addVectors(mass.s, deltaS)

    def reportState(self):
        for mass in self.masses:
            print(mass)




