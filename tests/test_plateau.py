import unittest
from tests.errors import ErrorList
from lib.plateau import RectangularPlateau

__author__ = 't35khan'

# initialize a RectangularPlateau with given bounds
# test RectangularPlateau.is_inside()


class PlateauTestCase(unittest.TestCase):

    error_list = ErrorList().error_list

    def test_is_inside_true(self):
        co_ordinates = [2, 2]
        bounds = [0, 0, 5, 5]
        plateau = RectangularPlateau(bounds)
        self.assertTrue(plateau.is_inside(co_ordinates),
                        msg='{0}'.format(PlateauTestCase.error_list['4']))

    def test_is_inside_true_edge_case(self):
        co_ordinates = [5, 5]
        bounds = [0, 0, 5, 5]
        plateau = RectangularPlateau(bounds)
        self.assertTrue(plateau.is_inside(co_ordinates),
                        msg='{0}'.format(PlateauTestCase.error_list['5']))

    def test_is_inside_false(self):
        co_ordinates = [6, 5]
        bounds = [0, 0, 5, 5]
        plateau = RectangularPlateau(bounds)
        self.assertFalse(plateau.is_inside(co_ordinates),
                         msg='{0}'.format(PlateauTestCase.error_list['4']))

if __name__ == '__main__':
    unittest.main()
