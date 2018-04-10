import unittest2 as unittest
from ipynb.fs.full.index import *

class TestPythonFunctionsWithArguments(unittest.TestCase):
    def test_restaurant_name_func(self):
        self.assertEqual(restaurant_name(fork_fig), 'Fork & Fig')
        self.assertEqual(restaurant_name(frontier_restaurant), 'Frontier Restaurant')

    def test_restaurant_rating_func(self):
        self.assertEqual(restaurant_rating(fork_fig), 4.5)
        self.assertEqual(restaurant_rating(frontier_restaurant), 4.0)

    def test_is_better_func(self):
        self.assertEqual(is_better(frontier_restaurant, fork_fig), False)
        self.assertEqual(is_better(fork_fig, frontier_restaurant), True)
        self.assertEqual(is_better(fork_fig, fork_fig), False)

    def test_is_cheaper_func(self):
        self.assertEqual(is_cheaper(frontier_restaurant, fork_fig), True)
        self.assertEqual(is_cheaper(fork_fig, frontier_restaurant), False)
        self.assertEqual(is_cheaper(fork_fig, fork_fig), False)

    def test_high_rating_func(self):
        self.assertEqual(high_rating(fork_fig, 4), True)
        self.assertEqual(high_rating(fork_fig, 5), False)
        self.assertEqual(high_rating(frontier_restaurant, 4), True)
