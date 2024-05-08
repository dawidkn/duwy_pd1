import math
import numpy as np

def absolute_vector(body,connection, step_time,time): #definiuje wektor abosolutny do środka ciężkośći
    Q = [] # wektory początkowe
    for row in body:
        x = float(row[-2])
        y = float(row[-1])
        fi_rad = np.arctan2(y, x)
        fi_deg = np.degrees(fi_rad)
        Qo = [x,y,fi_deg]
        Q.append(Qo)
    # print(Q)
    S = []

    for row in connection:
        if row[1] == "G" or row[2] == "G":
            print("na razie nie wiem")
        elif row[1].isdigit() and row[2].isdigit():
            for i in range(len(body)):
                print(len(body))
        else:
            print("bledne dane")
            break
