# importing modules
from random import choice, random

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.misc import derivative
from sympy import Symbol, limit, oo


class CalculusFunction:
    def __init__(self, func=None) -> None:
        self.function = func if func is not None else self.function

    def function(self, x):
        """
        Returns the class main function
        """
        return 4 * x**2 + x + 1

    def deriv(self, x):
        """
        Returns derivative of the main function
        """
        return derivative(self.function, x)

    def intg(self, x):
        """
        Returns a function integral
        """
        try:
            return [quad(self.function, 0, y) for y in x]
        except TypeError:
            return quad(function, 0, x)

    def limit(self, x, target_limit=oo):
        """
        Returns the limit of the main function
        """
        return limit(function, x, target_limit)


class Plotter:
    def __init__(self, start=-6, stop=6) -> None:
        self.board = plt
        self.plotted_graphs = 0
        self.start = start
        self.stop = stop

    @property
    def inputs(self):
        return np.linspace(self.start, self.stop)

    def draw_graph(self, coord_x=None, coord_y=None, color=None, label=None):
        if not color:
            self.color = choice(list("bgrcmyk"))

        if not label:
            label = "Function_" + str(self.plotted_graphs)

        if not coord_x:
            coord_x = self.inputs

        self.board.plot(coord_x, coord_y, color=self.color, label=label)

    def display(self):
        # changing limits of y-axis
        plt.gca().spines["left"].set_position(
            "zero",
        )
        # changing limits of x-axis
        plt.gca().spines["bottom"].set_position(
            "zero",
        )
        plt.legend(loc="upper left")
        plt.grid(True)
        self.board.show()


funcs = CalculusFunction()
plotter = Plotter()

plotter.draw_graph(
    coord_y=funcs.function(plotter.inputs), label="Main function"
)
plotter.draw_graph(coord_y=funcs.deriv(plotter.inputs), label="Derivative")
plotter.draw_graph(coord_y=funcs.intg(plotter.inputs), label="Integral")

plotter.display()
