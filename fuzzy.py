# -*- coding: utf-8 -*-
# using python 2.7.13
import random
from matplotlib import pyplot as plt


class Karamah:
    def __init__(self, l):
        self.a, self.b = self.__equation(l)

    def __equation(self, l):
        t = (l[0] * 1) - (l[2] * 1)
        tx = (l[1] * 1) - (l[3] * 1)
        ty = (l[0] * l[3]) - (l[1] * l[2])
        a = float(float(tx) / float(t))
        b = float(float(ty) / float(t))
        return a, b

    def equation2(self, a, b, x):
        y = a * x + b
        if y >= 1:
            y = 1
        elif y <= 0:
            y = 0
        return y


def show():
    lines = plt.plot([0, 15, 30], [1, 1, 0], [20, 50, 50, 70], [0, 1, 1, 0], [60, 90, 100], [0, 1, 1])
    plt.setp(lines, color='b', linewidth=1.0)
    plt.axis([0, 100, 0, 1.2])
    plt.show()


def show2():
    lines = plt.plot([0, 60], [1, 0], [40, 100], [0, 1])
    plt.setp(lines, color='r', linewidth=1.0)
    plt.axis([0, 100, 0, 1.2])
    plt.show()


def show3(z1, z2, z3):
    print z1, z2, z3
    lines = plt.plot([z1 - 0.01, z1], [0, 1], [z2 - 0.01, z2], [0, 1], [z3 - 0.01, z3], [0, 1])
    plt.setp(lines, color='b', linewidth=1.0)
    plt.axis([0, 1, 0, 1])
    plt.show()


def rule(x, y):
    l = [15, 1, 30, 0]
    A1 = Karamah(l)
    l = [20, 0, 50, 1]
    A2 = Karamah(l)
    l = [50, 1, 70, 0]
    A21 = Karamah(l)
    l = [60, 0, 90, 1]
    A3 = Karamah(l)
    l = [0, 1, 60, 0]
    B1 = Karamah(l)
    l = [40, 0, 100, 1]
    B2 = Karamah(l)
    show()
    show2()
    if x in range(60, 91) or y in range(0, 61):
        temp = A3.equation2(A3.a, A3.b, x)
        temp2 = B1.equation2(B1.a, B1.b, y)
        z1 = max(temp, temp2)
    else:
        z1 = 0

    if x < 50:
        if x in range(20, 50) and y in range(40, 101):
            temp = A2.equation2(A2.a, A2.b, x)
            temp2 = B2.equation2(B2.a, B2.b, y)
            z2 = min(temp, temp2)
        else:
            z2 = 0
    else:
        if x in range(50, 71) and y in range(40, 101):
            temp = A21.equation2(A21.a, A21.b, x)
            temp2 = B2.equation2(B2.a, B2.b, y)
            z2 = min(temp, temp2)
        else:
            z2 = 0
    if x in range(0, 30):
        z3 = A1.equation2(A1.a, A1.b, x)
    else:
        z3 = 0
    show3(z1, z2, z3)
    return z1, z2, z3


def wa(z1, z2, z3):
    total = z1 * 15 + z2 * 45 + z3 * 80
    try:
        print float(int(float(total / (z1 + z2 + z3)) * 100) / 100)
    except:
        print "error"


if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    print x, y
    z1, z2, z3 = rule(x, y)
    print z1, z2, z3
    wa(z1, z2, z3)
