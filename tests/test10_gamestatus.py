class gamestatus(unittest.TestCase):

  def test_initialization(self):
        testobj = character()
 #       expected_name_value is notnull
        
        self.assertNotEqual(testobj.name,'')