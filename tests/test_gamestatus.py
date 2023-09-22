import unittest
from src.levelup.gamestatus import gamestatus
class gamestatus(unittest.TestCase):

  def test_initialization(self):
        testObj = gamestatus()
        assert testObj.status != None
        self.assertNotEqual(testobj.name,'')
