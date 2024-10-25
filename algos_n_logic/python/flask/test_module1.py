'''Import the 'unittest' module to create unit tests for your code.
Import the 'square' and 'double' functions from the 'mymodule' module.'''
import unittest
from module1 import square, double, add

class TestSquare(unittest.TestCase):
    '''Define a test case class for testing the 'square' function.
    A test case is a single unit of testing. It checks a specific aspect of the code's behavior.'''

    def test1(self):
        '''Define the first test method for the 'square' function.
        Test methods should start with the word 'test' '''

        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.

class TestDouble(unittest.TestCase):
    '''Define a test case class for testing the 'double' function.'''

    def test1(self):
        '''Define the first test method for the 'double' function.'''
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

class TestAdd(unittest.TestCase):
    '''Define a test case class for testing the 'add' function.'''

    def test1(self):
        '''Define the first test method for the 'add' function.'''
        self.assertEqual(add(2, 3), 5) # tests add.
        self.assertEqual(round(add(-3.1, -6.2), 1), round(-9.3, 1)) # tests add.
        self.assertEqual(add(0, 0), 0) # tests add.

unittest.main()
