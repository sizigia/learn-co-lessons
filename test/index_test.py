import unittest2 as unittest
import pdb
from ipynb.fs.full.index import *

class TestPythonFunctions(unittest.TestCase):
    def test_number_of_destinations_func(self):
        self.assertEqual(number_of_destinations(), len(travel_destinations))

    def test_next_up_func(self):
        self.assertEqual(next_up(), 'argentina')

    def test_favorite_destination_func_return(self):
        self.assertEqual(favorite_destination(), 'madagascar')

    def test_capitalize_countries_func(self):
        self.assertItemsEqual(capitalize_countries(), ['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia', 'Japan'])
