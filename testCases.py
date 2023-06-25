import unittest
from apiproject import *

class TestIsPokemon(unittest.TestCase):
    def test_valid_pokemon(self):
        self.assertTrue(is_pokemon("pikachu"))

    def test_invalid_pokemon(self):
        self.assertFalse(is_pokemon("notapokemon"))



if __name__ == "__main__":
    unittest.main()