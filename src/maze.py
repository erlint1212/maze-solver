from cell import *
from time import sleep
from random import seed, choice

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed = None
        ):
        if seed != None:
            # Good for debugging
            seed(seed)
        self.x1 = x1 
        self.y1 = y1 
        self.num_rows = num_rows 
        self.num_cols = num_cols 
        self.cell_size_x = cell_size_x 
        self.cell_size_y = cell_size_y 
        self.win = win
        self._cells = [[None]*num_cols for i in range(num_rows)]
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

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
        sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_right_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []
            if i - 1 >= 0:
                if self._cells[i-1][j].visited == False:
                    to_visit.append(("Top", self._cells[i-1][j]))
            if i + 1 <= self.num_rows - 1:
                if self._cells[i+1][j].visited == False:
                    to_visit.append(("Bottom", self._cells[i+1][j]))
            if j - 1 >= 0:
                if self._cells[i][j-1].visited == False:
                    to_visit.append(("Left", self._cells[i][j-1]))
            if j + 1 <= self.num_cols - 1:
                if self._cells[i][j+1].visited == False:
                    to_visit.append(("Right", self._cells[i][j+1]))

            if to_visit == []:
                return

            try:
                rand = choice(to_visit)
            except:
                print(to_visit)

            match rand[0]:
                case "Right":
                    self._cells[i][j].has_right_wall = False
                    self._break_walls_r(i, j+1)
                case "Left":
                    self._cells[i][j].has_left_wall = False
                    self._break_walls_r(i, j-1)
                case "Top":
                    self._cells[i][j].has_top_wall = False
                    self._break_walls_r(i-1, j)
                case "Bottom":
                    self._cells[i][j].has_bottom_wall = False
                    self._break_walls_r(i+1, j)
            self._draw_cell(i,j)




                    



