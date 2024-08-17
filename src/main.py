from graphics import *

def main():
    win = Window(800, 600)
    point1 = Point(200, 200)
    point2 = Point(400, 400)
    line = Line(point1, point2)
    cell = Cell(
            200,
            400,
            200,
            400,
            win
    )
    cell.draw()
    win.draw_line(line, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
