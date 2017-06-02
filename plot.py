#!/usr/bin/python


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from setup import s

mCount = len(s.masses)

if (mCount != 2 and mCount != 3):
    raise Exception("Only 2 or 3 bodies supported. Provided %s." % mCount)

maxCntOfPoints = 25000
interval = 1
deltaT = 0.01
stepsPerPoint = 200
refToMass=False


def data_gen(t=0):
    cnt = 0
    while cnt < maxCntOfPoints:
        cnt += 1
        if (cnt % 100 == 0):
            print("%d of %d" % (cnt, maxCntOfPoints))
        t += 0.01
        for i in range(0, stepsPerPoint):
            s.step(deltaT)
        if (refToMass):
            if (mCount == 3):
                yield s.addVectors(s.masses[0].s, s.multipleVectorByConst(s.masses[0].s, -1)) + \
                      s.addVectors(s.masses[1].s, s.multipleVectorByConst(s.masses[0].s, -1)) + \
                      s.addVectors(s.masses[2].s, s.multipleVectorByConst(s.masses[0].s, -1))
            else:
                yield s.addVectors(s.masses[0].s, s.multipleVectorByConst(s.masses[0].s, -1)) + \
                      s.addVectors(s.masses[1].s, s.multipleVectorByConst(s.masses[0].s, -1))
        else:
            if (mCount == 3):
                yield s.masses[0].s + s.masses[1].s + s.masses[2].s
            else:
                yield s.masses[0].s + s.masses[1].s


def init():
    ax.set_ylim(-5, 5)
    ax.set_xlim(-5, 5)
    del xdata[:]
    del ydata[:]
    del x2data[:]
    del y2data[:]
    lines[0].set_data(xdata, ydata)
    lines[1].set_data(x2data, y2data)
    return lines


fig, ax = plt.subplots()

if (mCount == 3):
    lines = ax.plot([], [], [], [], [], [])
    x3data, y3data = [], []
else:
    lines = ax.plot([], [], [], [])

xdata, ydata, x2data, y2data = [], [], [], []
ax.grid()


def run(data):
    # update the data
    if (mCount == 3):
        x, y, x2, y2, x3, y3 = data
        x3data.append(x3)
        y3data.append(y3)
    else:
        x, y, x2, y2 = data

    xdata.append(x)
    ydata.append(y)

    x2data.append(x2)
    y2data.append(y2)

    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    ratio = 1.25

    if (mCount == 3):
        largerX = max(x, x2, x3)
        largerY = max(y, y2, y3)
        smallerX = min(x, x2, x3)
        smallerY = min(y, y2, y3)
    else:
        largerX = max(x, x2)
        largerY = max(y, y2)
        smallerX = min(x, x2)
        smallerY = min(y, y2)

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

    lines[0].set_data(xdata, ydata)
    lines[1].set_data(x2data, y2data)
    if (mCount == 3):
        lines[2].set_data(x3data, y3data)

    return lines[0],


ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=interval,
                              repeat=False, init_func=init)
plt.show()
