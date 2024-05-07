import matplotlib.pyplot as plt


def draw_figure(data):
    for row in data:
        name, figure_type, *point = row #* jest do tego że popierwszych dwóch zmiennych przypisuje już nastepne dane w wierszu do point
        if figure_type == "WIELOBOK":
            x = [point[i] for i in range(0, len(point), 2)] + [point[0]]
            y = [point[i] for i in range(1, len(point), 2)] + [point[1]]
            # cog_x = (x[0] + x[2]) / 2
            # cog_y = (y[0] + y[2]) / 2
            plt.plot(x, y, label=f"czlon {name}")
            # plt.scatter(cog_x, cog_y, color='red')
        elif figure_type == "LINIA":
            x = [point[i] for i in range(0, len(point), 2)] + [point[0]]
            y = [point[i] for i in range(1, len(point), 2)] + [point[1]] 
            # cog_x = (x[0] + x[2]) / 2
            # cog_y = (y[0] + y[2]) / 2
            plt.plot(x, y, label=f"czlon {name}")
            # plt.scatter(cog_x, cog_y, color='red')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Analiza kinematyczna')
    plt.legend()
    plt.grid(True)
    plt.xlim(-1, 7)  # zakres
    plt.show()

