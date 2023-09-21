import unittest
from src.levelup.gamestatus import gamestatus
class gamestatus(unittest.TestCase):

  def test_initialization(self):
        testobj = character()
 #       expected_name_value is notnull
        
        self.assertNotEqual(testobj.name,'')


