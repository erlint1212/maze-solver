from cell import *
from time import sleep

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win
        ):
        self.x1 = x1 
        self.y1 = y1 
        self.num_rows = num_rows 
        self.num_cols = num_cols 
        self.cell_size_x = cell_size_x 
        self.cell_size_y = cell_size_y 
        self.win = win
        self._cells = [[None]*num_cols for i in range(num_rows)]
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                cell = Cell(
                        self.x1 + self.cell_size_x * (j),
                        self.x1 + self.cell_size_x * (j + 1),
                        self.y1 + self.cell_size_y * i,
                        self.y1 + self.cell_size_y * (i + 1),
                        self.win
                        )
                self._cells[i][j] = cell
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(0.05)


