# Mars Rover Technical Challenge

# Table of Contents
1. [Design Decisions](#design-decisions)

2. [Assumptions](#assumptions)

3. [Class Descriptions](#class-descriptions)

     a. [NaiveRover](#a.-naiverover)
     
     b. [RectangularPlateau](#b.-rectangularplateau)
     
     c. [Controller](#c.-controller)
     
     d. [Explore](#d.-explore)
 
4. [Tests](#tests)

5. [Output](#output)

## 1. Design Decisions

A model view controller design pattern was implemented. The rover and plateau classes together serve as the "model", the
class Explore is a "viewer". Controller pre-processes the data for later requirements. It fetches the bounds of the plateau 
and separates the rover data. It was assumed that input file will not be very large, so everything is loaded onto the 
memory.

For execution and to obtain the expected output run **explore.py**.

## 2. Assumptions
It was assumed that the input file will be reasonably formatted before being used. Invalid move commands can be present, but
the rovers will not respond. For example, consider the input - 'LRMMQRR'. If an invalid move is followed by a valid move, 
the rover will respond to that. Empty lines will be handled, but completely out of order non-empty line will cause
problems. It was also assumed that the Rover and Plateau have the same reference point - i.e a Rover's (x, y) implies
plateau's (x, y). Also, the rover can reach the edges of the plateau but cannot go beyond these. 

## 3. Class Descriptions
### a. NaiveRover
The NaiveRover class is contained in the module rover. NaiveRover is implemented as a rover which moves strictly in a
rectangular fashion and has only two degrees of freedom. Any object is constructed with the following attributes:

       * x : initial x-coordinate of the rover
       * y : initial y-coordinate of the rover
       * orientation : one of the four cardinal compass components the rover is facing

The rover can be initialized by any int type x,y co-ordinates irrespective of the plateau boundaries. The class
RectangularPlateau contains a method that returns whether a rover is inside or outside the boundaries. The Explore
class will make sure a rover is not initialized that is outside the boundary.


**get_new_location(step)**

    Returns the new possible location and the orientation of the rover given a valid input command. This is a probable 
    location since the new location should be checked whether it is inside the plateau boundary.
    
The new location uses the following dictionary which maps an orientation to a correct movement. Three
dictionaries for three different possible commands **L, R, M**.

    
    move_dict = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
    left_rotate_dict = {'N': 'W', 'S': 'E', 'E': 'N', 'W': 'S'}
    right_rotate_dict = {'N': 'E', 'S': 'W', 'E': 'S', 'W': 'N'}
    
    Example: if step = 'M' and orientation = 'N' then x += move_dict['N'][0]
             if step = 'L', then orientation ='S' then new orientation = left_rotate_dict['S']
    
**set_location(x, y, orientation)**

    Sets the new location of rover to x, y and orientation.

**Note: An object rover of the class NaiveRover can only move by one step instead of taking a series of steps. Since**
**each of the rovers move exclusively, the latter might have been a faster way. But, it was done as such because**
**whether a rover's new probable location is inside the plateau or not should be returned by a method of class RectangularPlateau.**

### b. RectangularPlateau
The RectangularPlateau class is contained in the module plateau. It is rectangular in shape and is characterized by four
parameters: x, y co-ordinates of the **lower left corner** and **upper right corner**.
 
**is_inside(x,y)**

    Returns a True if (x,y) is inside the plateau boundary, and False otherwise.
    
### c. Controller
The class Controller was created to handle future variations in the input file. It will prepare the input commands by 
reading from the input file. The plateau bounds are set to some default values.
 
     * input_commands = lines from the input file
     * self.x_plateau_lower, self.y_plateau_lower = 0, 0
     * self.x_plateau_upper, self.y_plateau_upper = 5, 5

**get_plateau_bounds()**

    Uses the first line of input_commands to get the plateau bounds. If a valid input does not exist, the bounds will 
    remain as the default values.
    
**get_rover_commands()**

    Returns a list of rover initial locations and move commands.
    
### d. Explore
Explore is the main class file which can be executed as a stand alone script. It will initialize the NaiveRovers that 
are inside the plateau and execute move commands on them. It will return the final locations of each of the rovers in
the input file. 


## 4. Tests
A unittest framework was used for testing. Specific case of rover moves, rotation, plateau boundaries and etc. were
tested. 

    RoverMoveTestCase - Unit test for NaiveRover.get_new_location() from an 'M' command
    RoverRotateCase - Contains two tests for rover rotating left and right
    PlateauTestCase - Contains three tests to check RectangularPlateau.is_inside()
    RoverTestCaseCompleteMove - Tests the following sequence
                                  1. Give a rover located on an edge facing outward an 'M' command
                                  2. NaiveRover.get_new_location returns a correct location outside plateau
                                  3. RectangularPlateau.is_inside() returns FALSE
                                  4. NaiveRover location does not change      
## 5. Output
           
####Test Input
     5 5
     1 2 N
     LMLMLMLMM
     3 3 E
     MMRMMRMRRM    
####Obtained output
     1 3 N
     5 1 E      