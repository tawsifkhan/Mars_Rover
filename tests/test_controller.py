import unittest
import mock
from lib.controller import Controller
from tests.errors import ErrorList
__author__ = 't35khan'

# test controller functions


class ControllerTestCase(unittest.TestCase):

    plateau_bounds = (0, 0, 5, 5)
    error_list = ErrorList().error_list
    path = '../test_input.txt'

    def test_controller_init(self):
        controller = Controller(ControllerTestCase.path)
        self.assertEqual(ControllerTestCase.plateau_bounds, (controller.x_plateau_lower,
                                                             controller.y_plateau_lower,
                                                             controller.x_plateau_upper,
                                                             controller.y_plateau_upper),
                         msg='{0}'.format(ControllerTestCase.error_list['9']))

    def test_get_plateau_bounds(self):
        controller = Controller(ControllerTestCase.path)
        self.assertEqual(ControllerTestCase.plateau_bounds, controller.get_plateau_bounds(),
                         msg= '{0}'.format(ControllerTestCase.error_list['9']))

    def test_get_rover_commands(self):
        controller = Controller(ControllerTestCase.path)
        rover_commands = controller.get_rover_commands()
        expected_commands = [['1', '2', 'N'], ['LMLMLMLMM'], ['3', '3', 'E'], ['MMRMMRMRRM']]
        for i, j in enumerate(rover_commands):
            self.assertEqual(rover_commands[i], expected_commands[i],
                             msg='{0}'.format(ControllerTestCase.error_list['10']))

    @mock.patch('lib.controller.Controller.__init__')
    def test_controller_file_input(self,mock___init__):
        Controller.__init__("path")
        mock___init__.assert_called_with("path")


if __name__ == '__main__':
    unittest.main()