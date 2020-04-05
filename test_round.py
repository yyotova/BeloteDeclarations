import unittest
from round import compare_team_announcements, final_announcements


class TestcompareTeamAnnouncements(unittest.TestCase):
    def test_with_two_empty_announcements_returns_list_with_two_empty_dictionaries(self):
        res = compare_team_announcements({}, {})

        self.assertEqual(res, [{}, {}])

    def test_with_one_empty_announcement_returns_list_with_empty_dictionarie_of_that_empty_team(self):
        res = compare_team_announcements({'belote': [['12s', '13s']]}, {})
        res2 = compare_team_announcements({}, {'belote': [['12s', '13s']]})

        self.assertEqual(res, [{'belote': [['12s', '13s']]}, {}])
        self.assertEqual(res2, [{}, {'belote': [['12s', '13s']]}])

    def test_with_tierce_from_one_team_and_quinte_or_quatre_in_the_other_team(self):
        res = compare_team_announcements({'tierce': [['7h', '8h', '9h']]}, {'quinte': [['7s', '8s', '9s', '10s', '11s']]})

        self.assertEqual(res, [{'tierce': []}, {'quinte': [['7s', '8s','9s','10s', '11s']]}] )

    def test_with_tierces_from_one_team_and_quinte_or_quatre_in_the_other_team(self):
        res = compare_team_announcements({'tierce': [['7h', '8h', '9h'],['7h', '8h', '9h']]}, {'quinte': [['7s', '8s','9s','10s', '11s']]})

        self.assertEqual(res, [{'tierce': []}, {'quinte': [['7s', '8s','9s','10s', '11s']]}])

    def test_with_quatre_from_one_team_and_quinte_in_the_other_team(self):
        res = compare_team_announcements({'quatre': [['7h', '8h', '9h','10h']]}, {'quinte': [['7s', '8s','9s','10s', '11s']]})

        self.assertEqual(res, [{'quatre': []}, {'quinte': [['7s', '8s', '9s', '10s', '11s']]}])

    def test_with_tierces_from_one_team_and_tierce_in_the_other_team(self):
        res = compare_team_announcements({'tierce': [['7h', '8h', '9h']]}, {'tierce': [['9d', '10d', '11d'], ['7s', '8s','9s']]})
        res2 = compare_team_announcements({'tierce': [['9d', '10d', '11d'], ['7s', '8s','9s']]}, {'tierce': [['7h', '8h', '9h']]})

        self.assertEqual(res, [{'tierce': []}, {'tierce': [['9d', '10d', '11d'], ['7s', '8s', '9s']]}])
        self.assertEqual(res2, [{'tierce': [['9d', '10d', '11d'], ['7s', '8s', '9s']]}, {'tierce': []}])

    def test_with_tierces_from_one_team_and_tierces_in_the_other_team_which_are_equal(self):
        res = compare_team_announcements({'tierce': [['7h', '8h', '9h']]}, {'tierce': [['7s', '8s', '9s']]})
        res2 = compare_team_announcements({'tierce': [['9d', '10d', '11d'], ['7s', '8s','9s']]}, {'tierce': [['7h', '8h', '9h'],['9c', '10c', '11c']]})

        self.assertEqual(res, [{'tierce': []}, {'tierce': []}])
        self.assertEqual(res2, [{'tierce': []}, {'tierce': []}])

    def test_with_quatre_from_one_team_and_quatre_in_the_other_team_which_are_not_equal(self):
        res = compare_team_announcements({'quatre': [['7h', '8h', '9h', '10h']]}, {'quatre': [['8d','9d', '10d', '11d'], ['7s', '8s','9s','10s']]})
        res2 = compare_team_announcements({'quatre': [['8d', '9d', '10d', '11d'], ['7s', '8s','9s', '10s']]}, {'quatre': [['7h', '8h', '9h', '10h']]})

        self.assertEqual(res, [{'quatre': []}, {'quatre': [['8d','9d', '10d', '11d'], ['7s', '8s','9s','10s']]}] )
        self.assertEqual(res2, [{'quatre': [['8d', '9d', '10d', '11d'], ['7s', '8s', '9s', '10s']]}, {'quatre': []}])

    def test_with_quatres_from_one_team_and_quatres_in_the_other_team_which_are_equal(self):
        res = compare_team_announcements({'quatre': [['7h', '8h', '9h', '10h']]}, {'quatre': [['7s', '8s','9s', '10s']]})
        res2 = compare_team_announcements({'quatre': [['9d', '10d', '11d', '12d'], ['7s', '8s','9s','10s']]}, {'quatre': [['7h', '8h', '9h','10h'],['9c', '10c', '11c','12c']]})

        self.assertEqual(res, [{'quatre': []}, {'quatre': []}])
        self.assertEqual(res2, [{'quatre': []}, {'quatre': []}])

    def test_with_quinte_from_one_team_and_quinte_in_the_other_team_which_are_not_equal(self):
        res = compare_team_announcements({'quinte': [['7h', '8h', '9h', '10h','11h']]}, {'quinte': [['8d','9d', '10d', '11d','12d'], ['7s', '8s','9s','10s','11s']]})
        res2 = compare_team_announcements( {'quinte': [['8d','9d', '10d', '11d', '12d'], ['7s', '8s','9s', '10s','11s']]}, {'quinte': [['7h', '8h', '9h', '10h','11h']]})

        self.assertEqual(res, [{'quinte': []}, {'quinte': [['8d','9d', '10d', '11d','12d'], ['7s', '8s','9s','10s','11s']]}] )
        self.assertEqual(res2, [{'quinte': [['8d','9d', '10d', '11d', '12d'], ['7s', '8s','9s', '10s','11s']]}, {'quinte': []}])

    def test_with_quintes_from_one_team_and_quintes_in_the_other_team_which_are_equal(self):
        res = compare_team_announcements({'quinte': [['7h', '8h', '9h', '10h','11h']]}, {'quinte': [['7s', '8s','9s', '10s', '11s']]})
        res2 = compare_team_announcements({'quinte': [['8d','9d', '10d', '11d', '12d'], ['7s', '8s','9s','10s','11s']]}, {'quinte': [['7h', '8h', '9h','10h','11h'],['8c','9c', '10c', '11c','12c']]})

        self.assertEqual(res, [{'quinte': []}, {'quinte': []}])
        self.assertEqual(res2, [{'quinte': []}, {'quinte': []}])

    def test_with_announcements_which_dont_kill_the_each_other_returns_list_with_dictionaries(self):
        res = compare_team_announcements({'belote': [['12s', '13s']]}, {'tierce': [['8h', '9h', '10h']]})
        self.assertEqual(res, [{'belote': [['12s', '13s']]}, {'tierce': [['8h', '9h', '10h']]}])


class TestFinalAnnouncements(unittest.TestCase):
    def test_with_no_announcements_return_empty_list(self):
        res = final_announcements({}, {})

        self.assertEqual(res, [])

    def test_with_announcements_which_are_not_killed_return_list_with_announcements(self):
        res = final_announcements({'belote': [['12h', '13h']]}, {'belote': [['12h', '13h'], ['12d', '13d']]})
        res2 = final_announcements({'belote': [['12d', '13d']]}, {'belote': [['12h', '13h'], ['12d', '13d']]})

        self.assertEqual(res, ['belote'])
        self.assertEqual(res2, ['belote'])

    def test_with_announcements_which_are_killed_return_list_with_announcements(self):
        res = final_announcements({'tierce': [['7h', '8h', '9h']]}, {'tierce': []})
        res2 = final_announcements({'belote': [['12d', '13d']], 'tierce': [['7h', '8h', '9h']]}, {'belote': [['12d', '13d']], 'tierce': []})

        self.assertEqual(res, [])
        self.assertEqual(res2, ['belote'])

    def test_with_no_announcements_of_the_one_player_empty_list_with_announcements(self):
        res = final_announcements({}, {'tierce': [['7d', '8d', '9d']]})

        self.assertEqual(res, [])

    def test_with_one_announcements_of_the_one_player_and_one_of_the_other_return_announcements_of_the_player(self):
        res = final_announcements({'tierce': [['9d', '10d', '11d']]}, {'tierce': [['9d', '10d', '11d'], ['11s', '12s', '13s']], 'belote': [['12s', '13s']]})

        self.assertEqual(res, ['tierce'])


if __name__ == '__main__':
    unittest.main()
