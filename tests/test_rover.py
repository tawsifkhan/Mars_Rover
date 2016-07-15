import unittest
from lib.rover import NaiveRover
from tests.errors import ErrorList

__author__ = 't35khan'

# test NaiveRover.get_new_location()


class RoverMoveTestCase(unittest.TestCase):

    error_list = ErrorList().error_list

    def test_general_move(self):
        with open('../tests/edge_cases.txt', 'r') as test_input:
            for line in test_input:
                line = line.strip().split(" ")
                init_case = [int(line[0]), int(line[1]), line[2]]
                expected_case = [int(line[3]), int(line[4]), line[5]]
                rover = NaiveRover([init_case[0], init_case[1], init_case[2]])
                obtained_case = list(rover.get_new_location('M'))
                self.assertEqual(obtained_case, expected_case,
                                 msg='{0}'.format(self.error_list['1']))

if __name__ == '__main__':
    unittest.main()
