#!/usr/bin/python
from math import sqrt


class Mass:
    def __init__(self, mass, s, v):
        self.s = list(map(lambda x: float(x), s))
        self.v = list(map(lambda x: float(x), v))
        self.mass = float(mass)

    def __str__(self):
        return "mass = %f s = [%f %f] v = [%f %f]" % (self.mass, self.s[0], self.s[1], self.v[0], self.v[1])


class Simulation:
    G = 0.1

    def __init__(self, masses):
        self.masses = masses

    def __str__(self):
        return "Simulation got %d masses" % len(self.masses)

    def step(self, deltaT):
        #print('Running simulation step for deltaT = %f' % deltaT);
        netForces = self.calculateNetForces()
        #print('Net forces: %s' % netForces)
        accelarations = self.calculateAccelerations(netForces)
        #print('Accelerations: %s' % accelarations)
        self.calculateAndUpdateV(accelarations, deltaT)
        self.calculateAndUpdateS(deltaT)


    def calculateVectorLen(self, forceVec):
        ret = 0
        for el in forceVec:
            ret += el*el
        return sqrt(ret)

    def calculateForce(self, mass, source):
        r = self.addVectors(source.s, self.multipleVectorByConst(mass.s, -1))
        rLen = self.calculateVectorLen(r)
        if rLen == 0:
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
        for index in range(0, len(add1)):
            ret.append(add1[index] + add2[index])
        return ret

    def calculateNetForce(self, mass, others):
        ret = [0, 0]
        for m in others:
            #print('calculating netforce for %s from %s' % (mass, m))
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
        for i in range(0, len(self.masses)):
            acceleration = self.multipleVectorByConst(netForces[i], 1 / (self.masses[i].mass))
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



