import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        for i in range(100) :
           x = np.random.uniform(0,1)
           y = np.random.uniform(0,1) 
           self.assertTrue( ((x*x+y*y)<1)==incircle(x,y), "The program you wrote for determining whether or not points are within the circle is incorrect" )
