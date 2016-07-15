import unittest
from tests.errors import ErrorList
from lib.rover import NaiveRover

__author__ = 't35khan'

# unittests for NaiverRover.get_new_location() for rotations


class RoverRotateCase(unittest.TestCase):

    error_list = ErrorList().error_list

    def test_rotate_left(self):
        test_cases = [[0, 0, 'N'], [0, 0, 'S'], [0, 0, 'E'], [0, 0, 'W']]
        expected_cases = [[0, 0, 'W'], [0, 0, 'E'], [0, 0, 'N'], [0, 0, 'S']]
        for i, j in enumerate(test_cases):
            rover = NaiveRover(test_cases[i])
            expected_case = expected_cases[i]
            obtained_case = list(rover.get_new_location('L'))
            self.assertEqual(obtained_case,expected_case, msg='{0}'.format(RoverRotateCase.error_list['2']))

    def test_rotate_right(self):
        test_cases = [[0, 0, 'N'], [0, 0, 'S'], [0, 0, 'E'], [0, 0, 'W']]
        expected_cases = [[0, 0, 'E'], [0, 0, 'W'], [0, 0, 'S'], [0, 0, 'N']]
        for i, j in enumerate(test_cases):
            rover = NaiveRover(test_cases[i])
            expected_case = expected_cases[i]
            obtained_case = list(rover.get_new_location('R'))
            self.assertEqual(obtained_case,expected_case, msg='{0}'.format(RoverRotateCase.error_list['3']))


if __name__ == '__main__':
    unittest.main()



