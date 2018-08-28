# -*- coding: utf-8 -*-
# using python 2.7.13
import random
import math


def initialization():
    global w13, w14, w23, w24, w35, w45, theta3, theta4, theta5, alpha
    w13 = random.random()
    w14 = random.random()
    w23 = random.random()
    w24 = random.random()
    w35 = random.random()
    w45 = random.random()
    theta3 = random.random()
    theta4 = random.random()
    theta5 = random.random()
    alpha = random.random()


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def y3_and_y4(x1, x2):
    y3 = sigmoid(x1 * w13 + x2 * w23 - theta3)
    y4 = sigmoid(x1 * w14 + x2 * w24 - theta4)
    return y3, y4


def y(y3, y4):
    return sigmoid(y3 * w35 + y4 * w45 - theta5)


def error(yd, y):
    return yd - y


def weight_trian(n, a, b):
    global alpha
    t_w1 = alpha * a * n
    t_w2 = alpha * b * n
    t_theta = alpha * -1 * n
    return t_w1, t_w2, t_theta


def renew(t_w13, t_w14, t_w23, t_w24, t_w35, t_w45, t_theta3, t_theta4, t_theta5):
    global w13, w14, w23, w24, w35, w45, theta3, theta4, theta5
    w13 = w13 + t_w13
    w14 = w14 + t_w14
    w23 = w23 + t_w23
    w24 = w24 + t_w24
    w35 = w35 + t_w35
    w45 = w45 + t_w45
    theta3 = theta3 + t_theta3
    theta4 = theta4 + t_theta4
    theta5 = theta5 + t_theta5


if __name__ == '__main__':
    global w13, w14, w23, w24, w35, w45, theta3, theta4, theta5, alpha
    initialization()
    print w13, w14, w23, w24, w35, w45, theta3, theta4, theta5, alpha
    se = 0
    l = []
    train_set = [[1, 1, 0], [0, 1, 1], [1, 0, 1], [0, 0, 0]]
    i = 0
    while True:
        # print "第{}個週期".format(i)
        # print
        for j in train_set:
            x1 = j[0]
            x2 = j[1]
            y3, y4 = y3_and_y4(x1, x2)
            y5 = y(y3, y4)
            err = error(j[2], y5)
            n5 = y5 * (1 - y5) * err
            t_w35, t_w45, t_theta5 = weight_trian(n5, y3, y4)
            n3 = y3 * (1 - y3) * n5 * w35
            n4 = y4 * (1 - y4) * n5 * w45
            t_w13, t_w23, t_theta3 = weight_trian(n3, x1, x2)
            t_w14, t_w24, t_theta4 = weight_trian(n4, x1, x2)
            renew(t_w13, t_w14, t_w23, t_w24, t_w35, t_w45, t_theta3, t_theta4, t_theta5)
            se = round(se + math.pow(err, 2), 4)
        l.append(se)
        if se <= 0.001:
            print w13, w14, w23, w24, w35, w45, theta3, theta4, theta5, alpha

            break
        se = 0
        i += 1
    print "{}次".format(i)
    for i in l:
        print i
