from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__runing = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__runing = True
        while self.__runing:
            self.redraw()
        print("window closed...")


    def close(self):
        self.__runing = False

    def draw_line(self, Line, fill_color="black"):
        Line.draw(self.__canvas, fill_color)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
                self.point1.x, 
                self.point1.y, 
                self.point2.x, 
                self.point2.y,
                fill = fill_color,
                width = 2
        )
        
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

    def draw(self):
        point11 = Point(self._x1 , self._y1)
        point12 = Point(self._x1, self._y2)
        point21 = Point(self._x2, self._y1)
        point22 = Point(self._x2, self._y2)
        line_list = []
        if self.has_left_wall:
            line_list.append(Line(point11, point12))
        if self.has_right_wall:
            line_list.append(Line(point21, point22))
        if self.has_top_wall:
            line_list.append(Line(point11, point21))
        if self.has_bottom_wall:
            line_list.append(Line(point12, point22))
        for l in line_list:
            self._win.draw_line(l)
            

