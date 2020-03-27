import unittest
from utls import random_call, random_hand, inner_sort, sort, announcements

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

class TestAnnouncements(unittest.TestCase):
    def test_with_only_with_one_belote_when_the_rank_is_clubs(self):
        sorted_cards = [ ['7c', '12c', '13c'], ['11d', '13d'], ['7h', '10h'], ['7s'] ]

        res = announcements(sorted_cards, 'Clubs')

        self.assertEqual(res, {'belote': [['12c', '13c']]})

    def test_with_more_belotes_when_the_rank_is_all_trumps_returns_only_one(self):
        sorted_cards = [ ['7c', '12c', '13c'], ['12d', '13d'], ['10h'], ['12s', '13s'] ]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'belote': [['12c', '13c']]})

    def test_with_only_with_one_tierce_when_the_rank_is_clubs(self):
        sorted_cards = [ ['7c', '10c', '11c', '12c'], ['11d', '13d'], ['7h', '10h'], [] ]

        res = announcements(sorted_cards, 'Clubs')

        self.assertEqual(res, {'tierce': [['10c', '11c', '12c']]})

    def test_with_more_tierces_and_one_belote_when_the_rank_is_all_trumps(self):
        sorted_cards = [ ['7c', '8c', '9c'], ['10d', '11d'], [], ['12s', '13s','14s'] ]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'belote': [['12s', '13s']], 'tierce': [['7c', '8c', '9c'],['12s', '13s','14s']]})

    def test_with_one_quatre_when_the_rank_is_clubs_returns_only_the_quatre_not_the_tierce(self):
        sorted_cards = [ ['7c', '8c', '9c', '10c','14c'], ['7d', '8d'], ['7h'], [] ]

        res = announcements(sorted_cards, 'Clubs')

        self.assertEqual(res, {'quatre': [['7c', '8c', '9c', '10c']]})

    def test_with_more_quatres_when_the_rank_is_all_trumps_returns_only_the_quatres_not_with_tierces(self):
        sorted_cards = [ ['7c', '8c', '9c', '10c'], ['8d', '9d', '10d', '11d'], [], [] ]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'quatre': [['7c', '8c', '9c', '10c'], ['8d', '9d', '10d', '11d']]})


if __name__ == '__main__':
    unittest.main()