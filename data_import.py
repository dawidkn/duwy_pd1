import numpy as np
import os

# files_path_body = os.path.join("input_file", "czlon_input.txt")
# file_body = open(files_path_body, 'r')

# files_path_connector = os.path.join("input_file", "para_input.txt") #łączy podfolder
# file_connect = open(files_path_connector, 'r')

# l=1
# for line in file_body:
#     if not line.strip():
#         break
#     print(f"linia {l}: {line}", end='')
#     l +=1
# file_body.close()

# for line in file_connect:
#     if not line.strip():
#         break
#     print(f"linia {l}: {line}", end='')
#     l +=1


# file_connect.close()

def create_body():
    body = []

    files_path_body = os.path.join("input_file", "czlon_input.txt")

    with open(files_path_body, 'r') as file:
        file.readline() #pomija pierwszy wiersz
        for line in file:
            elememts= line.strip().split(';')

            body.append(elememts)


    for row in body:
        print(row)

    return body 

def create_connection():
    connection = []

    files_path_connect = os.path.join("input_file", "para_input.txt")

    with open(files_path_connect, 'r') as file:
        file.readline() #pomija pierwszy wiersz
        for line in file:
            elememts= line.strip().split(';')
            if not line.strip(): #zatrzymuje jak jest pusto
                break
            connection.append(elememts)


    for row in connection:
        print(row)
    return connection
