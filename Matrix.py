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
                print(self.matrix[i][j] + ' ')
            print('\n')
        print('\n')

    @classmethod
    def fromArray(cls, arr: list):
        for i in range(cls.rows):
            for j in range(cls.cols):
                cls.matrix[i][j] = arr[i * cls.cols + j]
