#!/usr/bin/python


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from setup import s

mCount = len(s.masses)


maxCntOfPoints = 10000
interval = 1
deltaT = 0.0000001
stepsPerPoint = 100000
refToMass = True


def data_gen(t=0):
    cnt = 0
    while cnt < maxCntOfPoints:
        cnt += 1
        if (cnt % 100 == 0):
            print("%d of %d" % (cnt, maxCntOfPoints))
        t += 0.01
        for i in range(0, stepsPerPoint):
            s.step(deltaT)

        ret = []

        if (refToMass):
            ret = [0, 0]
            reference = s.multipleVectorByConst(s.masses[0].s, -1)
            for m in s.masses[1:]:
                ret += s.addVectors(m.s, reference)
        else:

            for m in s.masses:
                ret += m.s

        yield ret


def init():
    ax.set_ylim(-5, 5)
    ax.set_xlim(-5, 5)
    for i in range(0, mCount):
        del xData[i][:]
        del yData[i][:]
        lines[i].set_data(xData[i], yData[i])
    return lines


fig, ax = plt.subplots()

initList = []
xData = []
yData = []
for ind in range(0, mCount):
    initList.append([])
    initList.append([])

lines = ax.plot(*initList)

for i in range(0, mCount):
    xData.append([])
    yData.append([])

ax.grid()


def run(data):
    # update the data
    tmpXData = []
    tmpYData = []
    for i in range(0, mCount):
        x = data[2*i]
        y = data[2*i+1]
        tmpXData.append(x)
        tmpYData.append(y)
        xData[i].append(x)
        yData[i].append(y)

    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    ratio = 1.25

    largerX = max(tmpXData)
    largerY = max(tmpYData)
    smallerX = min(tmpXData)
    smallerY = min(tmpYData)

    if largerX >= xmax:
        ax.set_xlim(xmin, ratio * xmax)
        ax.figure.canvas.draw()
    if smallerX <= xmin:
        ax.set_xlim(ratio * xmin, xmax)
        ax.figure.canvas.draw()

    if largerY >= ymax:
        ax.set_ylim(ymin, ratio * ymax)
        ax.figure.canvas.draw()
    if smallerY <= ymin:
        ax.set_ylim(ratio * ymin, ymax)
        ax.figure.canvas.draw()

    for i in range(0, mCount):
        lines[i].set_data(xData[i], yData[i])
    return lines[0],


ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=interval,
                              repeat=False, init_func=init)
plt.show()
