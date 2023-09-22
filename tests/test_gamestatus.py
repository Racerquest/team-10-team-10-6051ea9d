import unittest
from src.levelup.gamestatus import GameStatus
class gamestatus(unittest.TestCase):

  def test_initialization(self):
        testObj = GameStatus(status="")
        assert testObj.status != None

  def currentPosition(self):
        testObj = GameStatus(Position)
        assert testObj.Position == None

