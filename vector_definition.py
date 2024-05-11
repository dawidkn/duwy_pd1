import math
import numpy as np
from scipy.misc import derivative
from sympy import symbols, diff

def absolute_vector(body,connection, step_time,time): #definiuje wektor abosolutny do środka ciężkośći
    for row in body:
        del row[0]
        
    body = np.array(body, dtype=np.float16)
    Rot = []
    Q = []

    for row in body:
        x = float(row[-2])
        y = float(row[-1])
        fi_rad = np.arctan2(float(row[2])-float(row[-2]), float(row[3])-float(row[-1]))
        roto = np.array([[np.cos(fi_rad), -np.sin(fi_rad)], [np.sin(fi_rad), np.cos(fi_rad)]])
        qo = [x,y]
        Rot.append(roto)
        Q.append(qo)

    S = []

    for row in connection:
        if row[1] == "G" :

            x = body[int(row[2]) - 1][-2]
            y = body[int(row[2]) - 1][-1]
            s0 = [0.0,0.0,np.abs(float(row[-2])-x),np.abs(float(row[-1])-y)]
            S.append(s0)

        elif row[1].isdigit() and row[2].isdigit():
            x1 = body[int(row[1]) - 1][-2]
            y1 = body[int(row[1]) - 1][-1]
            x2 = body[int(row[2]) - 1][-2]
            y2 = body[int(row[2]) - 1][-1]

            s0 = [np.abs(float(row[-2])-x1), np.abs(float(row[-1])-y1), np.abs(float(row[-2])-x2), np.abs(float(row[-1])-y2)]
            S.append(s0)
    return S, Q, Rot
