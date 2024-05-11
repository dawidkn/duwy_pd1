import numpy as np

def node_eq(S, Q, Rot, Connection):
    # print("wktory absolutne")
    # print(Q)
    # print("macierz rotacji")
    # print(Rot)
    # print("pary")
    # print(Connection)
    # print("wektroy_par")
    # print(S)
    f_time = 1 #funkcja zalezna od czasu
    eq_node = []
    index = 0
    s_zero = np.array([[0],[0]])
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
                print("eq result ground")
            else:
                print("posuw ground")
        
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
                print("eq result free")
            else:
                print("posuw free")
        
        index += 1
        
    print("wynik eq")
    print(eq_node)



   

    # Przykładowe punkty
    x1, y1 = 1, 2
    x2, y2 = 4, 6

    # Obliczenie odległości
    odleglosc =  npquit.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("Odległość między punktami:", odleglosc)

    #przeszukiwanie listy po indeksie z innej listy
    # a = [[1, 2, 0], [3, 4, 1], [5, 6, 0]]
    # b = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]

    # # Inicjalizacja listy c
    # c = []

    # # Iteracja przez listę a
    # for sublist in a:
    #     # Pobranie indeksu z listy a
    #     index_from_a = sublist[2]
        
    #     # Pobranie podlisty z listy b na podstawie indeksu z listy a
    #     sublist_from_b = b[index_from_a]
        
    #     # Dodanie wartości z indeksu 2 podlisty z listy b do listy c
    #     c.append(sublist_from_b[2])

    # print(c)


    # a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Lista do przechowywania macierzy

    #konwertowanie podlisty z list (z ominieciem pierwszego indeksu) na macierz
    # Iteracja przez pod-listy w liście a
    # lipo = 0
    # for sublist in a:
        
    #     # Tworzymy macierz 1x2 wykorzystując wartości z pod-listy na indeksach 1 i 2
    #     macierz = np.array([[sublist[1]], [sublist[2]]])
        
    #     # Dodajemy nowo utworzoną macierz do listy macierzy
    #     print(f"Macierz {int(lipo)+1}:")
    #     print(macierz)
    #     lipo += 1
