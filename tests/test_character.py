from unittest import TestCase
from src.levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)
    
    def test_notnull(self):
        ISNULL = ''
        testobj = Character(ISNULL)
        self.assertNotEqual(testobj.name, '')
