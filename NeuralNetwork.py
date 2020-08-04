from Matrix import *
from math import e


def sigmoid(x: float)->float:
    return 1 / (1 + pow(float(e), -x))


class NeuralNetwork:
    def __init__(self, input_nodes: int, hidden_nodes: int, output_nodes: int):
        # Set no. nodes
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_ndoes = output_nodes

        # Make matrices of weights
        self.weights_ih = Matrix(hidden_nodes, input_nodes + 1) # 1 is for bias
        self.weights_hh = Matrix(hidden_nodes, hidden_nodes + 1) # 1 is for bias
        self.weights_ho = Matrix(hidden_nodes, hidden_nodes + 1) # 1 is for bias

        # Set random weights with initialization
        self.weights_ih.randomize()
        self.weights_hh.randomize()
        self.weights_ho.randomize()


