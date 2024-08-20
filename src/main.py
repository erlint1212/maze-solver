from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)
    """
    point1 = Point(200, 200)
    point2 = Point(400, 400)
    line = Line(point1, point2)
    cell1 = Cell(
            200,
            400,
            200,
            400,
            win
    )
    cell2 = Cell(
            270,
            470,
            270,
            470,
            win
    )
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2)
    """
    #win.draw_line(line, "red")
    maze1 = Maze(
        0,
        0,
        20,
        20,
        30,
        30,
        win,
        1
    )
    maze1.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
