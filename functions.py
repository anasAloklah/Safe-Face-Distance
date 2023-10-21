from math import sqrt,pow
import os
def distanceBetweenTowPoint(x1,y1,x2,y2):
    d= sqrt(pow((x1-x2),2)+pow((y1-y2),2))
    return d
def convertInchToCm(inch_value):
    cm_value=inch_value*2.54
    return cm_value
def taskIsRun(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    for i in range(len(r)):
        if name in r[i]:
            return True
    return False
