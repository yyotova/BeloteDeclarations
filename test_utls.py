import unittest
from utls import random_call, random_hand, inner_sort, sort

class TestInnerSort(unittest.TestCase):
    def test_inner_sort_with_empty_list_returns_empty_list(self):
        list_cards = []

        res = inner_sort(list_cards)

        self.assertEqual(res, [])

    def test_inner_sort_with_list_with_cards_returns_sorted_list_by_suites(self):
        list_cards = ['7s', '10s', 'Ks', 'Js']

        res = inner_sort(list_cards)

        self.assertEqual(res, ['7s', '10s', '11s', '13s'])

if __name__ == '__main__':
    unittest.main()