import math
import numpy as np
import matplotlib.pyplot as plt

def con_def(connect):
    c_mov = []

    for row in connect:
        if row[0] == "postepowa":
            c_mov.append(row)

    if len(c_mov) == 0:
        return 0
    else:
        return len(c_mov)

def moving_contact_chart(connect, time, step_time):
    move_l = con_def(connect)
    data, x = input_moving_cof(connect, time, step_time)
    yt = []
    for i in range(move_l):
        y = []
        for j in range(len(x)):
            index = i % len(data[0]) #to pozwala mi korzystać tylko z dwóch indeksów w tablicach zmiennych jak postępowych mam więcej
            yo = data[2][index]+data[3][index]*np.sin(data[0][index]*x[j]+data[1][index]) # to samo co wyżej
            y.append(yo)
        yt.append(y)
        plt.plot(x, y)
        
    # omega_rad = np.radians(omega)
    # fi_rad = np.radians(fi)
    plt.title('wykres wymuszen')
    plt.xlabel('time')
    plt.ylabel('[mm]')
    plt.legend()
    # plt.show()
    return yt, x

def input_moving_cof(connect, time, step_time):
    omega = [10,10] #w stopniach
    fi = [30,80] #w stponiach
    l = [0.3,0.6]
    a = [0.25,0.35]
    
    data = [omega, fi, l, a]
    x = []
    xo = 0
    while xo <= time:
        x.append(xo)
        xo += step_time
    return data, x

# def moving_line_connectors(connect, step_time, time):

#     return x, y, moving_connect, rotation_connect



