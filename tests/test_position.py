from unittest import TestCase
from src.levelup.position import Position

class TestPositionInit(TestCase):
    def test_init(self):
        xCoordinates = 1
        yCoordinates = ''
        testobj = Position(xCoordinates, yCoordinates)
        self.assertNotEqual(testobj.xCoordinates,"")
        self.assertNotEqual(testobj.yCoordinates,"")  

