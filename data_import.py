import numpy as np
import os

def create_body():
    body = []

    files_path_body = os.path.join("input_file", "czlon_input.txt")

    with open(files_path_body, 'r') as file:
        file.readline() #pomija pierwszy wiersz
        for line in file:
            elememts= line.strip().split(';')
            if not line.strip(): #zatrzymuje jak jest pusto
                break
            body.append(elememts)


    for row in body:
        print(row)

    return body 

def create_connection():
    connection = []

    files_path_connect = os.path.join("input_file", "para_input.txt")

    with open(files_path_connect, 'r') as file:
        file.readline()
        for line in file:
            elememts= line.strip().split(';')
            if not line.strip():
                break
            connection.append(elememts)


    for row in connection:
        print(row)
    return connection
