import math
import numpy as np
import matplotlib.pyplot as plt

def con_def(connect):
    c_rot = []
    c_mov = []

    for row in connect:
        if row[0] == "obrotowa":
            del row[0]
            c_rot.append(row)

        elif row[0] == "postepowa":
            del row[0]
            c_mov.append(row)
        else:
            print("blad danych")
    return c_mov, c_rot

def moving_line_connectors(connect, step_time, time):
    moving_connect, rotation_connect = con_def(connect)

    omega = [10,10] #w stopniach
    fi = [30,80] #w stponiach
    l = [0.3,0.6]
    a = [0.25,0.35]
    y = []
    x = np.arange(0, time, step_time)

    for i in range(len(moving_connect)):

        ome_rand = np.random.uniform(5,45)      #dla testu!!!!!!!!!!!!!!!!!
        fi_rand = np.random.uniform(12,85)      #dla testu!!!!!!!!!!!!!!!!!!!1
        l_rand = np.random.uniform(0.2,0.9)     #dla testu!!!!!!!!!!!!!!!!!
        a_rand = np.random.uniform(0.15,0.7)    #dla testu!!!!!!!!!!!!!!!
        # index = i % len(a) #to pozwala mi korzystać tylko z dwóch indeksów w tablicach zmiennych jak postępowych mam więcej
        # yo = l[index]+a[index]*np.sin(omega[index]*x+fi[index]) # to samo co wyżej
        yo = l_rand+a_rand*np.sin(ome_rand*x+fi_rand)     # dla testu!!!!!!!!!!!!!!!!!!
        y.append(yo)
        plt.plot(x, yo)
        
    # omega_rad = np.radians(omega)
    # fi_rad = np.radians(fi)


    plt.title('przemieszczenie tloka')
    plt.xlabel('time')
    plt.ylabel('[mm]')
    plt.legend()
    # plt.show()
    return x, y, moving_connect, rotation_connect



