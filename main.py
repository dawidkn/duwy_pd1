import numpy as np

import csv


def importBody(fileBody):
    body = []
    with open(fileBody, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        next(csvreader)  # Pominięcie nagłówków
        for row in csvreader:
            if row[1] == 'linia':
                czlon = {
                    'numer': int(row[0]),
                    'typ': row[1],
                    'punkty': [(row[i], float(row[i+1]), float(row[i+2])) for i in range(2, len(row), 3)]
                }
                dane_czlonow.append(czlon)
            elif row[1] == 'wielobok':
                czlon = {
                    'numer': int(row[0]),
                    'typ': row[1],
                    'punkty': [(row[i], float(row[i+1]), float(row[i+2])) for i in range(2, len(row)-3, 3)],
                    'srodek_ciezkosci': (row[-3], float(row[-2]), float(row[-1]))
                }
                dane_czlonow.append(czlon)
            else:
                print("Nieznany typ czlonu:", row[1])
            
    return dane_czlonow, dane_par


fileBody = 'czlon_input.csv'
fileConnect = "para_input.csv"

body = importBody(fileBody)
