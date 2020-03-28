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

        self.assertEqual(res, {'belote': ['12c', '13c']})

    def test_with_more_belotes_when_the_rank_is_all_trumps_returns_only_one(self):
        sorted_cards = [ ['7c', '12c', '13c'], ['12d', '13d'], ['10h'], ['12s', '13s'] ]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'belote': ['12c', '13c']})

    def test_with_only_with_one_tierce_in_different_ranks(self):
        sorted_cards1 = [ ['7c', '10c', '11c', '12c'], ['11d', '13d'], ['7h', '10h'], [] ]
        sorted_cards2 = [ ['7c', '10c', '11c', '12c'], ['7d', '10d', '11d', '12d'], [], [] ]
        
        res1 = announcements(sorted_cards1, 'Clubs')
        res2 = announcements(sorted_cards2, 'Diamonds')

        self.assertEqual(res2, {'tierce': ['10d', '11d', '12d']})
        self.assertEqual(res1, {'tierce': ['10c', '11c', '12c']})

    def test_with_no_announcements_when_the_rank_is_all_trumps(self):
        sorted_cards = [['14c'], ['9d'], ['8h', '10h'], ['8s', '9s', '11s', '12s']]
    
        res = announcements(sorted_cards, 'All trumps')
        
        self.assertEqual(res, {})

    def test_with_one_tierce_at_the_begining_when_the_rank_is_all_trumps(self):
        sorted_cards = [['14c'], ['9d'], ['8h'], ['7s','8s', '9s', '11s', '12s']]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'tierce': [['7s','8s', '9s']]})

    def test_with_one_tierce_at_the_end_when_the_rank_is_all_trumps(self):
        sorted_cards = [['14c'], ['9d'], ['8h'], ['7s','8s', '10s', '11s', '12s']]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'tierce': [['10s','11s', '12s']]})

    def test_with_more_tierces_and_one_belote_when_the_rank_is_all_trumps(self):
        sorted_cards = [ ['7c', '8c', '9c'], ['10d', '11d'], [], ['12s', '13s','14s'] ]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'belote': [['12s', '13s']], 'tierce': [['7c', '8c', '9c'],['12s', '13s','14s']]})

    def test_with_one_quinte_when_the_rank_is_all_trumps(self):
        sorted_cards = [ [], ['10d'], [], ['7s', '8s','9s','10s', '11s','13s', '14s'] ]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'quinte': [['7s', '8s','9s','10s', '11s']]})

    def test_with_one_quatre_when_the_rank_is_clubs_returns_only_the_quatre_not_the_tierce(self):
        sorted_cards = [ ['7c', '8c', '9c', '10c','14c'], ['7d', '8d'], ['7h'], [] ]

        res = announcements(sorted_cards, 'Clubs')

        self.assertEqual(res, {'quatre': ['7c', '8c', '9c', '10c']})

    def test_with_more_quatres_when_the_rank_is_all_trumps_returns_only_the_quatres_not_with_tierces(self):
        sorted_cards = [ ['7c', '8c', '9c', '10c'], ['8d', '9d', '10d', '11d'], [], [] ]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'quatre': [['7c', '8c', '9c', '10c'], ['8d', '9d', '10d', '11d']]})

    def test_with_only_with_one_quinte_with_five_cards__when_the_rank_is_clubs(self):
        sorted_cards = [ ['9c', '10c', '11c', '12c', '13c'], ['11d', '13d'], ['7h'], [] ]

        res = announcements(sorted_cards, 'Clubs')

        self.assertEqual(res, {'belote': ['12c', '13c'], 'quinte': ['9c','10c', '11c', '12c', '13c']})

    def test_with_rank_no_trumps_returns_empty_dictionary(self):
        sorted_cards = [ ['9c', '10c', '11c', '12c', '13c'], ['11d', '13d'], ['7h'], [] ]

        res = announcements(sorted_cards, 'No trumps')

        self.assertEqual(res, {})

    def test_with_carre_in_differnt_ranks(self):
        sorted_cards = [ ['9c', '10c', '13c'], ['9d', '13d'], ['9h'], ['7s', '9s'] ]

        res1 = announcements(sorted_cards, 'Clubs')
        res2 = announcements(sorted_cards, 'Diamonds')
        res3 = announcements(sorted_cards, 'Hearts')
        res4 = announcements(sorted_cards, 'Spades')

        self.assertEqual(res1, {'carre of 9s': ['9c', '9d', '9h', '9s']})
        self.assertEqual(res2, {'carre of 9s': ['9c', '9d', '9h', '9s']})
        self.assertEqual(res3, {'carre of 9s': ['9c', '9d', '9h', '9s']})
        self.assertEqual(res4, {'carre of 9s': ['9c', '9d', '9h', '9s']})

    def test_with_more_carres_when_the_rank_is_all_trumps(self):
        sorted_cards = [ ['9c', '10c'], ['9d', '10d'], ['9h', '10h'], ['9s', '10s'] ]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'carre of 9s': [['9c', '9d', '9h', '9s']], 'carre of 10s': [['10c', '10d', '10h', '10s']]})

    def test_with_carre_and_tierce_returns_only_carre(self):
        sorted_cards = [ ['9c', '10c'], ['7d', '8d', '9d'], ['9h', '10h'], ['9s']]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'carre of 9s': [['9c', '9d', '9h', '9s']]})

    def test_with_carre_and_quatre_returns_only_carre(self):
        sorted_cards = [ ['9c'], ['7d', '8d', '9d', '10d'], ['9h', '10h'], ['9s']]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'carre of 9s': [['9c', '9d', '9h', '9s']]})

    def test_with_carre_and_quinte_returns_only_carre(self):
        sorted_cards = [ ['9c'], ['7d', '8d', '9d', '10d', '11d'], ['9h'], ['9s']]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'carre of 9s': [['9c', '9d', '9h', '9s']]})

    def test_with_carre_and_belote_returns_both(self):
        sorted_cards = [ ['12c'], ['7d', '12d', '13d'], ['9h', '12h'], ['12s', '13s']]

        res = announcements(sorted_cards, 'All trumps')

        self.assertEqual(res, {'belote': ['12d', '13d'], 'carre of Qs': [['12c', '12d', '12h', '12s']]})


if __name__ == '__main__':
    unittest.main()