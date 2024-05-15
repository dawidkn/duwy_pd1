import numpy as np

def perpendicular(q1, q2, q3, q4):
    dx = q3 - q1
    dy = q4 - q2

    paralel = np.array([dx, dy])
    perpend = np.array([-dy, dx])

    return paralel, perpend

def function(rot, S):
    # Przykładowa funkcja
    om = np.array([[0, -1], [1,0]])
    f1 = np.dot(om, np.dot(rot, S)) #macierz
    return np.array(f1)

def jacobian(Q, eq_result, rot, S):
    m = int(len(Q))
    Fq = np.zeros((m,m))
    h = 1e-5
    
    J = np.zeros((m, m))
    J = function(rot, S)

    return J
        

def newrap(q,j):
    print(q)
    print(j)
    Nr = q - np.linalg.solve(q, j)
    # print(Nr)

def node_eq(S, Q, Rot, Connection):

    f_time = 1 #funkcja zalezna od czasu
    eq_node = []
    index = 0
    s_zero = np.array([[0],[0]])
    Fqjacob = []
    New_rap = []
    for row in S:
        rot_matrix = []
        r = []

        if Connection[index][1] == "G":
            q1 = Q[int(Connection[index][2])-1][0]
            q2 = Q[int(Connection[index][2])-1][1]

            rn = np.array([[q1], [q2]])

            so = np.array([[row[-2]], [row[-1]]])

            Roto = Rot[int(Connection[index][2])-1]

            if Connection[index][0] == "obrotowa":
                eq_result = s_zero - (rn + np.dot(Roto, so))
                eq_node.append(eq_result)

                eq_node.append(eq_result)
                Fqj = (jacobian(Q[int(Connection[index][1])-1], eq_result, Roto1, so1))
                New_rap.append(newrap(Q[int(Connection[index][2])-1], Fqj))
                Fqjacob.append(Fqj)

            else:
                U, V = perpendicular(0, 0, q1, q2)
                eq_result = s_zero - (rn + np.dot(Roto, so))*np.dot(Roto, U)
                eq_node.append(eq_result)
                Fqj = (jacobian(Q[int(Connection[index][1])-1], eq_result, Roto1, so1))
                New_rap.append(newrap(Q[int(Connection[index][2])-1], Fqj))
                Fqjacob.append(Fqj)
        else:
            q1 = Q[int(Connection[index][1])-1][0]
            q2 = Q[int(Connection[index][1])-1][1]
            q3 = Q[int(Connection[index][2])-1][0]
            q4 = Q[int(Connection[index][2])-1][1]

            rn1 = np.array([[q1], [q2]])
            rn2 = np.array([[q3], [q4]])

            so1 = np.array([[row[0]], [row[1]]])
            so2 = np.array([[row[-2]], [row[-1]]])

            Roto1 = Rot[int(Connection[index][1])-1]
            Roto2 = Rot[int(Connection[index][2])-1]


            if Connection[index][0] == "obrotowa":
                eq_result = (rn2 + np.dot(Roto2, so2)) - (rn1 + np.dot(Roto1, so1))

                eq_node.append(eq_result)
                Fqj1 = (jacobian(Q[int(Connection[index][1])-1], eq_result, Roto1, so1))
                Fqj2 = (jacobian(Q[int(Connection[index][2])-1], eq_result, Roto2, so2))
                New_rap.append(newrap(Q[int(Connection[index][1])-1], Fqj1))
                New_rap.append(newrap(Q[int(Connection[index][2])-1], Fqj2))
                Fqjacob.append(Fqj1)
                Fqjacob.append(Fqj2)

            else:
                U, V = perpendicular(q1, q2, q3, q4)

                eq_result = ((rn2 + np.dot(Roto2, so2)) - (rn1 + np.dot(Roto1, so1)))*np.dot(Roto2, U) - f_time
                eq_node.append(eq_result)
                Fqj1 = (jacobian(Q[int(Connection[index][1])-1], eq_result, Roto1, so1))
                Fqj2 = (jacobian(Q[int(Connection[index][2])-1], eq_result, Roto2, so2))
                New_rap.append(newrap(Q[int(Connection[index][1])-1], Fqj1))
                New_rap.append(newrap(Q[int(Connection[index][2])-1], Fqj2))
                Fqjacob.append(Fqj1)
                Fqjacob.append(Fqj2)


        index += 1
    print(eq_node)

    # print(Fqjacob)
    # print(New_rap)
        




   


