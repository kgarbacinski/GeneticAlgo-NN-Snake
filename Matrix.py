from __future__ import annotations
from typing import *
import random
import math


def sigmoid_fun(x: int):
    return 1 / (1 + float(pow(math.e, -x)))


class Matrix:
    def __init__(self, no_rows: int, no_cols: int):
        self.no_rows = no_rows
        self.no_cols = no_cols
        self.matrix = [[[] for _ in range(no_cols)] for _ in range(no_rows)]

    def calc_dot_product(self, matrix_b: Matrix) -> Matrix:
        product = Matrix(self.no_rows, matrix_b.no_cols)

        for i in range(self.no_rows):
            for j in range(product.no_cols):
                sum = 0
                for k in range(self.no_cols):
                    sum += self.matrix[i][k] * matrix_b.matrix[k][j]

                product.matrix[i][j] = sum

        return product

    def apply_activation(self) -> Matrix:
        output = Matrix(self.no_rows, self.no_cols)

        for i in range(self.no_rows):
            for j in range(self.no_cols):
                output.matrix[i][j] = sigmoid_fun(self.matrix[i][j])

        return output

    def randomize(self):
        for i in range(self.no_rows):
            for j in range(self.no_cols):
                self.matrix[i][j] = random.uniform(-1, 1)

    def print(self):
        for i in range(self.no_rows):
            for j in range(self.no_cols):
                print(self.matrix[i][j] + " ")
            print('\n')
        print('\n')

    def add_bias(self):
        self.matrix.append([1])

    def do_crossover(self, other_matrix: Matrix) -> Matrix:
        child_matrix = Matrix(self.no_rows, self.no_cols)

        end_row = int(random.uniform(0, self.no_rows - 1))
        end_column = int(random.uniform(0, self.no_cols - 1))

        for i in range(self.no_rows):
            for j in range(self.no_cols):
                if i < end_row or (i == end_row and j <= end_column):
                    child_matrix.matrix[i][j] = self.matrix[i][j]
                else:
                    child_matrix.matrix[i][j] = other_matrix.matrix[i][j]

        return child_matrix

    def mutate(self, mutation_rate):
        for i in range(self.no_rows):
            for j in range(self.no_cols):
                rand_value = random.random()

                if rand_value < mutation_rate:
                    # uniform method
                    self.matrix[i][j] += random.uniform(-1, 1)

    def to_array(self):
        array = [[[] for _ in range(self.no_cols)] for _ in range(self.no_rows)]

        for i in range(self.no_rows):
            for j in range(self.no_cols):
                array[i * self.no_cols + j] = self.matrix[i][j]

        return array

    def from_array(self, array: list):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = array[i * self.cols + j]

    @staticmethod
    def one_column_matrix_from_array(array: list) -> Matrix:
        one_col_matrix = Matrix(len(array), 1)

        for i in range(len(array)):
            one_col_matrix.matrix[i][0] = array[i]

        return one_col_matrix
