import math
import numpy as np

def S_vector(Q, Connect, tracking, ismoving):
    S=[]
    for i in range(len(Connect)):
        if tracking[i][0] == 0:
            so = np.array([[0.0],[0.0]])
            S.append(so)

            so = np.array([[((Q[tracking[i][1]-1][0]) - Connect[i][0])], [(Q[tracking[i][1]-1][1] - Connect[i][1])]])
            S.append(so)
        else:
            so = np.array([[((Q[tracking[i][0]-1][0]) - Connect[i][0])], [(Q[tracking[i][0]-1][1] - Connect[i][1])]])
            S.append(so)
            so = np.array([[((Q[tracking[i][1]-1][0]) - Connect[i][0])], [(Q[tracking[i][1]-1][1] - Connect[i][1])]])
            S.append(so)
          
    return S
        

def absolute_vector(body,connection, step_time,time): #definiuje wektor abosolutny do środka ciężkośći
    for row in body:
        del row[0]
    Rot = []
    Q = []

    for row in body:
        x = float(row[-2])
        y = float(row[-1])
        # fi_rad = np.arctan2(float(row[2])-float(row[-2]), float(row[3])-float(row[-1])) # zmiana kątów zgodnie z kierunkiem czlonu
        fi_rad = 0 # tworzenie macierzy obrotów początkowych ale z zerami, czyli uklady wspolrzednych sa obrocone o zero

        roto = np.array([[np.cos(fi_rad), -np.sin(fi_rad)], [np.sin(fi_rad), np.cos(fi_rad)]])
        qo = [x,y]
        Rot.append(roto) #macierz rotacji
        Q.append(qo) #definicja wektora absolutnego

    tracking = []
    ismoving = []
    i = 0

    for row in connection:
        
        if row[1] == "G":
            row[1] = 0
        tracking.append([int(row[1]),int(row[2])])
        if row[0] =="postepowa":
            ismoving.append(i)
        del row[0]
        del row[0]
        del row[0]
        row[:] = list(map(float, row))
        i +=1

    S = S_vector(Q, connection, tracking, ismoving) #definicja wektora S
    equation = node_eq(S, Q, Rot, ismoving, tracking) #definicja wektora FI d


    return S, Q, Rot


def node_eq(S, Q, Rot, ismoving, tracking):
    # print("track")
    # print(tracking)
    # print("rot")
    # print(Rot)
    # print("S")
    # print(S)
    # print("q")
    # print(Q)
    j = 0
    eqN = []
    Qrotate = [np.array([sublist[1], sublist[0]]).reshape(2, 1) for sublist in Q] #przerobienie listy list Q na liste macierzy Q i zrotowanie

    for i in range(len(S)//2):
        if i in ismoving:
            print("rownanie dla postepowej")
        else:
            # print("rownanie dla obrotowej")
            if tracking[i][0] == 0:
                Qr = Qrotate[tracking[i][1]-1]
                eqo = np.array([[0],[0]])-(Qr + np.dot(Rot[tracking[i][1]-1],S[j+1]))
                eqN.append(eqo)
            else:
                Qr1 = Qrotate[tracking[i][0]-1]
                Qr2 = Qrotate[tracking[i][1]-1]
                eqo = (Qr1 + np.dot(Rot[tracking[i][0]-1],S[j])) - (Qr2 + np.dot(Rot[tracking[i][1]-1],S[j+1]))
                eqN.append(eqo)
                # print(eqo)
        # print("J" + str(i))
        # print(S[j])
        # print(S[j+1])
        j +=2
    print(eqN)
    # eq_result = (rn2 + np.dot(Roto2, so2)) - (rn1 + np.dot(Roto1, so1))