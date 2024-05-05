import numpy as np
import os

files_path_body = os.path.join("input_file", "czlon_input.txt")
file_body = open(files_path_body, 'r')

files_path_connector = os.path.join("input_file", "para_input.txt")
file_connect = open(files_path_connector, 'r')

l=1
for line in file_body:
    print(f"linia {l}: {line}", end='')
    l +=1
file_body.close()

l=1
for line in file_connect:
    print(f"linia {l}: {line}", end='')
    l +=1
file_connect.close()