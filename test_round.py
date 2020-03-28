import unittest
from round import check_team_announcements

class TestCheckTeamAnnouncements(unittest.TestCase):
    def test_with_two_empty_announcements_returns_list_with_two_empty_dictionaries(self):
        res = check_team_announcements({}, {})

        self.assertEqual(res, [{}, {}])

    def test_with_one_empty_announcement_returns_list_with_empty_dictionarie_of_that_empty_team(self):
        res = check_team_announcements({'belote': [['12s', '13s']]}, {})
        res2 = check_team_announcements({},{'belote': [['12s', '13s']]})

        self.assertEqual(res, [{'belote': [['12s', '13s']]}, {}])
        self.assertEqual(res2,[{}, {'belote': [['12s', '13s']]}])

    def test_with_tierce_from_one_team_and_quinte_or_quatre_in_the_other_team(self):
        res = check_team_announcements({'tierce': [['7h', '8h', '9h']]}, {'quinte': [['7s', '8s','9s','10s', '11s']]})

        self.assertEqual(res, [{'tierce': []}, {'quinte': [['7s', '8s','9s','10s', '11s']]}] )

    def test_with_quatre_from_one_team_and_quinte_in_the_other_team(self):
        res = check_team_announcements({'quatre': [['7h', '8h', '9h','10h']]}, {'quinte': [['7s', '8s','9s','10s', '11s']]})

        self.assertEqual(res, [{'quatre': []}, {'quinte': [['7s', '8s','9s','10s', '11s']]}] )

    def test_with_tierces_from_one_team_and_tierce_in_the_other_team(self):
        res = check_team_announcements({'triece': [['7h', '8h', '9h']]}, {'tierce': [['9d', '10d', '11d'], ['7s', '8s','9s']]})

        self.assertEqual(res, [{'tierce': []}, {'tierce': [['9d', '10d', '11d'], ['7s', '8s','9s']]}] )



    # def test_with_announcements_which_dont_kill_the_other_returns_list_with_dictionaries(self):
    #     res = check_team_announcements({'belote': [['12s', '13s']]}, {'tierce': [['8h', '9h', '10h']]})

    #     self.assertEqual(res, [{'belote': [['12s', '13s']]}, {'tierce': [['8h', '9h', '10h']]}])


if __name__ == '__main__':
    unittest.main()