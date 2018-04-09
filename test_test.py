import unittest2 as unittest
from ipynb.fs.full.index import *

class TestPythonFunctionss(unittest.TestCase):
    def test_number_of_destinations_func(self):
        travel_destinations = ['argentina', 'mexico', 'italy']
        self.assertEqual(number_of_destinations(), 3)

    def test_next_up_func(self):
        travel_destinations = ['argentina', 'mexico', 'italy']
        self.assertEqual(next_up(), 'argentina')

    def test_favorite_destination_func_return(self):
        self.assertEqual(favorite_destination(), 'madagascar')

    def test_favorite_destination_func_mutates_arr(self):
        travel_destinations = ['argentina', 'mexico', 'italy']
        self.assertEqual(favorite_destination(), 'madagascar')
        favorite_destination()
        self.assertEqual(travel_destinations[-1], ['argentina', 'mexico', 'italy','madagascar'])

    def test_capitalize_countries_func(self):
        travel_destinations = ['argentina', 'mexico', 'italy']
        self.assertItemsEqual(capitalize_countries(), ['Argentina', 'Mexico', 'Italy'])
        travel_destinations.append('japan')
        self.assertItemsEqual(capitalize_countries(), ['Argentina', 'Mexico', 'Italy', 'Japan'])
        
