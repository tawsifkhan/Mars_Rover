import unittest
from tests.errors import ErrorList
from lib.rover import NaiveRover
from lib.plateau import RectangularPlateau
__author__ = 't35khan'

# tests a complete move for a rover on the plateau edges facing outward


class RoverTestCaseCompleteMove(unittest.TestCase):

    error_list = ErrorList().error_list

    def test_rover_move(self):
        test_cases = [[5, 5, 'N'], [0, 0, 'S'], [5, 0, 'E'], [0, 0, 'W']]
        expected_cases_get_loc = [[5, 6, 'N'], [0, -1, 'S'], [6, 0, 'E'], [-1, 0, 'W']]
        plateau = RectangularPlateau([0, 0, 5, 5])

        for i, j in enumerate(test_cases):
            rover = NaiveRover(test_cases[i])
            x, y, orientation = rover.get_new_location('M')
            self.assertEqual(expected_cases_get_loc[i], [x, y, orientation],
                             msg='{0}'.format(RoverTestCaseCompleteMove.error_list['1']))
            if plateau.is_inside([x, y]):
                rover.set_location(x, y, orientation)
            self.assertEqual(test_cases[i], [rover.x, rover.y, rover.orientation],
                             msg='{0}'.format(RoverTestCaseCompleteMove.error_list['7']))


if __name__ == '__main__':
    unittest.main()