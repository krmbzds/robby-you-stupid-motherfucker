from Parameters import *
from Robby import *
from Grid import *


class Session:
    robby = None
    grid = None

    def __init__(self, robby, grid):
        self.robby = robby
        self.grid = grid
        self.grid.set_robby(self.robby)
        self.robby.set_grid(self.grid)

    def run(self):
        total_score = 0
        for i in range(NUM_ACTIONS_PER_SESSION):
            score = self.robby.move()
            total_score = total_score + score
        return total_score
