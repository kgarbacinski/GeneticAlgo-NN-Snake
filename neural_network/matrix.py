from __future__ import annotations
from typing import List
import random
import math

def sigmoid_fun(x: float) -> float:
    return 1 / (1 + math.exp(-x))

class Matrix:
    def __init__(self, no_rows: int, no_cols: int):
        self.no_rows = no_rows
        self.no_cols = no_cols
        self.matrix = [[0.0 for _ in range(no_cols)] for _ in range(no_rows)]

    def calc_dot_product(self, matrix_b: Matrix) -> Matrix:
        if self.no_cols != matrix_b.no_rows:
            raise ValueError("Incompatible matrices for dot product")
        product = Matrix(self.no_rows, matrix_b.no_cols)
        for i in range(self.no_rows):
            for j in range(product.no_cols):
                product.matrix[i][j] = sum(self.matrix[i][k] * matrix_b.matrix[k][j] for k in range(self.no_cols))
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

    def add_bias(self):
        self.matrix.append([1.0])

    def do_crossover(self, other_matrix: Matrix) -> Matrix:
        child_matrix = Matrix(self.no_rows, self.no_cols)
        end_row = random.randint(0, self.no_rows - 1)
        end_column = random.randint(0, self.no_cols - 1)
        for i in range(self.no_rows):
            for j in range(self.no_cols):
                if i < end_row or (i == end_row and j <= end_column):
                    child_matrix.matrix[i][j] = self.matrix[i][j]
                else:
                    child_matrix.matrix[i][j] = other_matrix.matrix[i][j]
        return child_matrix

    def mutate(self, mutation_rate: float):
        for i in range(self.no_rows):
            for j in range(self.no_cols):
                if random.random() < mutation_rate:
                    self.matrix[i][j] += random.uniform(-1, 1)

    def to_array(self) -> List[float]:
        return [self.matrix[i][j] for i in range(self.no_rows) for j in range(self.no_cols)]

    def from_array(self, array: List[float]):
        for i in range(self.no_rows):
            for j in range(self.no_cols):
                self.matrix[i][j] = array[i * self.no_cols + j]

    @staticmethod
    def one_column_matrix_from_array(array: List[float]) -> Matrix:
        one_col_matrix = Matrix(len(array), 1)
        for i in range(len(array)):
            one_col_matrix.matrix[i][0] = array[i]
        return one_col_matrix