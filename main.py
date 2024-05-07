from data_import import create_body, create_connection
import matplotlib.pyplot as plt
from body_draw import draw_figure

body = create_body()

connect = create_connection()

draw_figure(body)

