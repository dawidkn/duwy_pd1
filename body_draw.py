import matplotlib.pyplot as plt


def draw_figure(data): 
    name = []
    typ = []
    x = []
    y = []
    cog_x = []
    cog_y = []
    figure = []

    for row in data:
         #* jest do tego że popierwszych dwóch zmiennych przypisuje już nastepne dane w wierszu do point
        getname, getfigure_type, *points = row
        point = [float(z) for z in points]
        coordinate_x = []
        coordinate_y = []
        cogxo = []
        cogyo = []
        for i in range(len(point)):
            if i == 0 or i % 2 == 0:
                coordinate_x.append(point[i])
            else:
                coordinate_y.append(point[i])
        cogxo.append(coordinate_x[-1])
        del coordinate_x[-1]
        cogyo.append(coordinate_y[-1])
        del coordinate_y[-1]

        x.append(coordinate_x)
        y.append(coordinate_y)
        cog_x.append(cogxo)
        cog_y.append(cogyo)
        typ.append(getfigure_type)
        name.append(getname)


    for j in range(len(x)):  # Iteracja przez indeksy j (odpowiadające każdej figurze)
        print("zew")
        print(j)
        for i in range(len(x)):  # Iteracja przez indeksy i (odpowiadające listom cog_x i cog_y)
            print("wew")
            print(i)

            print("nazwa")
            print(typ[i])
            # Dodaj te wypisy do kodu, aby śledzić rozmiary list i indeksy
            # print(f"i: {i}, j: {j}, len(cog_x): {len(cog_x)}, len(cog_y): {len(cog_y)}")
            # print(f"cog_x[j][i]: {cog_x[i][j]}, cog_y[j][i]: {cog_y[i][j]}")
            
            plt.plot(x[j], y[j], label=f"czlon {name[j]}")  # Zmiana name[i] na name[j]
            plt.scatter(cog_x[j], cog_y[j], color='red', label=f"Środek ciężkości {name[j]}")  # Zmiana name[i] na name[j]
            figure.append(plt.gca())
            plt.clf()
    for polts in figure:
        polts.set_xlabel('X')
        polts.set_ylabel('Y')
        # polts.set_title('Analiza kinematyczna')
        # polts.legend()
        polts.grid(True)
        plt.show()

