import unittest
from graphics import Window 
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_rows
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols
        )
        win.close()

    def test_maze_break_entrance_and_exit(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
                m1._cells[0][0].has_left_wall,
                False
        )
        self.assertEqual(
                m1._cells[m1.num_rows-1][m1.num_cols-1].has_right_wall,
                False
        )
        win.close()


if __name__ == "__main__":
    unittest.main()
