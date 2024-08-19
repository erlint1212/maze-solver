from graphics import Point, Line

class Cell:
    def __init__(
            self,
            x1,
            x2,
            y1,
            y2,
            win,
            has_left_wall = True, 
            has_right_wall = True,
            has_top_wall = True,
            has_bottom_wall = True
            ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
        point11 = Point(self._x1 , self._y1)
        point12 = Point(self._x1, self._y2)
        point21 = Point(self._x2, self._y1)
        point22 = Point(self._x2, self._y2)
        line_list = []
        walls = [self.has_left_wall, self.has_right_wall, self.has_top_wall, self.has_bottom_wall]
        line_list.append(Line(point11, point12))
        line_list.append(Line(point21, point22))
        line_list.append(Line(point11, point21))
        line_list.append(Line(point12, point22))
        for i, l in enumerate(line_list):
            if walls[i]: 
                self._win.draw_line(l)
            else:
                self._win.draw_line(l, "white")

    def draw_move(self, to_cell, undo=False):
        fill_color = "gray"
        if not undo:
            fill_color = "red"
        point_og = Point((self._x1 + self._x2)/2 , (self._y1 + self._y2)/2)
        point_to = Point((to_cell._x1 + to_cell._x2)/2 , (to_cell._y1 + to_cell._y2)/2)
        line = Line(point_og, point_to)
        self._win.draw_line(line, fill_color)
