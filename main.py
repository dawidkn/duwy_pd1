from data_import import create_body, create_connection
import matplotlib.pyplot as plt
from body_draw import draw_figure
import connections
import vector_definition
import calculation

step_time = 0.5
time = 4
body = create_body()
connect = create_connection()
#draw_figure(body)
moving_x, moving_y, moving_connect, rotation_connect = connections.moving_line_connectors(connect, step_time, time)

S, Q, Rot = vector_definition.absolute_vector(body, connect, step_time,time)

eq = calculation.node_eq(S, Q, Rot, connect)

