import random
from enum import *
from Parameters import *


class Grid:
    matrix = None
    robby = None

    def __init__(self, matrix):
        self.matrix = matrix

    def set_robby(self, robby):
        self.robby = robby

    def __getitem__(self, r):
        return self.matrix[r]

    def pickup_can(self, r, c):
        self.matrix[r][c] = OBSTACLES.EMPTY

    # noinspection PyListCreation
    @staticmethod
    def get_random_grid():
        temp = [[OBSTACLES.WALL] * 12]

        for i in range(0, 10):
            row = []
            row.append(OBSTACLES.WALL)
            for j in range(0, 10):
                if SODA_CAN_PROBABILITY >= random.random():
                    row.append(OBSTACLES.CAN)
                else:
                    row.append(OBSTACLES.EMPTY)
            row.append(OBSTACLES.WALL)
            temp.append(row)

        temp.append([OBSTACLES.WALL] * 12)
        return Grid(temp)
