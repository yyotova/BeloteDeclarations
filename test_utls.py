import unittest
from utls2 import random_call, random_hand, inner_sort, sort

class TestInnerSort(unittest.TestCase):
    def test_inner_sort_with_empty_list_returns_empty_list(self):
        list_cards = []

        res = inner_sort(list_cards)

        self.assertEqual(res, [])

    def test_inner_sort_with_list_with_cards_returns_sorted_list_by_suites(self):
        list_cards = ['7s', '10s', 'Ks', 'Js']

        res = inner_sort(list_cards)

        self.assertEqual(res, ['7s', '10s', '11s', '13s'])

class TestSort(unittest.TestCase):
    def test_sort_with_no_ranks_returns_four_empty_lists(self):
        list_cards = [[], [], [], []]

        res = sort(list_cards)

        self.assertEqual(res, list_cards) 
    def test_sort_with_random_cards_returns_sorted_by_rank(self):
        list_cards = ['7s', '10s', '11s', '10h',  '7h', '13d', '11d']

        res = sort(list_cards)

        expected = [ [], ['11d', '13d'], ['7h', '10h'], ['7s', '10s', '11s'] ]

        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()