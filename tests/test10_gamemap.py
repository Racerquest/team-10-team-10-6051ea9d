import unittest

class gamemap(unittest.TestCase):

  def test_initialization(self):
        testobj = character()
 #       expected_name_value is notnull
        
        self.assertNotEqual(testobj.name,'')

if __name__ == '__main__':
    unittest.main()
