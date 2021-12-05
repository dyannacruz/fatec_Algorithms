# Exercício 10: Criar uma função que retorne o gráfico de uma função cosseno.

import numpy as np
import matplotlib.pyplot as plt
from math import radians

def graph_cos():
    plt.title("Gráfico da função cosseno")

    plt.grid(True)
    eixo_x = np.arange(0, 13, 0.1)

    eixo_y = np.cos(eixo_x)
    plt.plot(eixo_x, eixo_y)

    plt.show()

graph_cos()