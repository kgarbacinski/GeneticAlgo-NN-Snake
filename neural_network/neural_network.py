from __future__ import annotations
from neural_network.matrix import Matrix

class NeuralNetwork:
    def __init__(self, input_nodes: int, hidden_nodes: int, output_nodes: int):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.weights_ih = Matrix(hidden_nodes, input_nodes + 1)
        self.weights_hh = Matrix(hidden_nodes, hidden_nodes + 1)
        self.weights_ho = Matrix(output_nodes, hidden_nodes + 1)

        self.weights_ih.randomize()
        self.weights_hh.randomize()
        self.weights_ho.randomize()

    def get_output(self, input_layer_array: list) -> list:
        input_layer_matrix = Matrix.one_column_matrix_from_array(input_layer_array)
        input_layer_matrix.add_bias()

        ih_weights_output = self.weights_ih.calc_dot_product(input_layer_matrix)
        ih_weights_output_activated = ih_weights_output.apply_activation()
        ih_weights_output_activated.add_bias()

        hh_weights_output = self.weights_hh.calc_dot_product(ih_weights_output_activated)
        hh_weights_output_activated = hh_weights_output.apply_activation()
        hh_weights_output_activated.add_bias()

        ho_weights_output = self.weights_ho.calc_dot_product(hh_weights_output_activated)
        outputs = ho_weights_output.apply_activation()

        return outputs.to_array()

    def do_crossover(self, other_DNA: NeuralNetwork) -> NeuralNetwork:
        child_DNA = NeuralNetwork(self.input_nodes, self.hidden_nodes, self.output_nodes)
        child_DNA.weights_ih = self.weights_ih.do_crossover(other_DNA.weights_ih)
        child_DNA.weights_hh = self.weights_hh.do_crossover(other_DNA.weights_hh)
        child_DNA.weights_ho = self.weights_ho.do_crossover(other_DNA.weights_ho)
        return child_DNA

    def mutate(self, mutation_rate: float):
        self.weights_ih.mutate(mutation_rate)
        self.weights_hh.mutate(mutation_rate)
        self.weights_ho.mutate(mutation_rate)
