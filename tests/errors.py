__author__ = 't35khan'


class ErrorList:

    def __init__(self):
        self.error_list = {'1': 'NaiveRover get_new_location() return incorrect',
                              '2': 'NaiveRover rotated LEFT incorrectly',
                              '3': 'NaiveRover rotated RIGHT incorrectly',
                              '4': 'RectangularPlateau returns wrong boolean - general case',
                              '5': 'RectangularPlateau returns wrong boolean - edge case',
                              '6': 'NaiveRover moved out of RectangularPlateau',
                              '7': 'NaiverRover set_location() incorrect value',
                              '8': 'Called with incorrect path',
                              '9': 'RectangularPlateau boundaries incorrect',
                             '10': 'Error in get_rover_commands in Controller'}
