from unittest import TestCase
from src.levelup.position import Position

class TestPositionInit(TestCase):
    def test_init(self):
        xycoordinates = (1,1)
        #xCoordinates = 1
        #yCoordinates = ''
        testobj = Position(xycoordinates)
        self.assertNotEqual(testobj.xyCoordinates[0],"")
        self.assertNotEqual(testobj.xyCoordinates[1],"") 
    def test_xylen(self):
        xycoordinates = (1,5)
        #xCoordinates = 1
        #yCoordinates = ''
        testobj = Position(xycoordinates)
        self.assertEqual(len(testobj.xyCoordinates),2) 

