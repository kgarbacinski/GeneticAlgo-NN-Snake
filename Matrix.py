from __future__ import annotations
from typing import *
import random


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[[] for _ in range(cols)] for _ in range(rows)]

    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = random.uniform(-1, 1)

    def print(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j] + " ")
            print('\n')
        print('\n')

    def add_input_bias(self):
        self.matrix.append([[1]])

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
