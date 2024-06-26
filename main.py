from data_import import create_body, create_connection
import matplotlib.pyplot as plt
from body_draw import draw_figure
import connections
import vector_definition
from calculation import displacement

step_time = 0.02
time = 4
body = create_body()
connect = create_connection()
#draw_figure(body)

yt, xt = connections.moving_contact_chart(connect, time, step_time)


S, Q, Rot, eqN, extension, tracking, ismoving, isground, alleqN = vector_definition.absolute_vector(body, connect, step_time,time)


displacement(S, Q, Rot, eqN, extension, tracking, ismoving, time, step_time, connect, isground, alleqN)

# print(eqN)
# eq = calculation.node_eq(S, Q, Rot, connect)

