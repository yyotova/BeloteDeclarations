import unittest
from Cls import Player, Team, Round


class test_player_class(unittest.TestCase):

    def test_player_class(self):
        player = Player("Gosho")
        self.assertEqual(str(player), "Gosho->[]")

    def test_player_class_get_dict_player(self):
        player = Player("Gosho")
        player_dict = player.get_dict_player()
        self.assertEqual(player_dict, {"Gosho": {"cards": [], "announcements": [], "points": 0}})


class test_team_class(unittest.TestCase):

    def test_team_class(self):
        team = Team("Severozapada", [Player("Petar"), Player("Yoanna")])
        self.assertEqual(str(team), "Severozapada")

    def test_team_class_update_score(self):
        team = Team("Severozapada", [Player("Petar"), Player("Yoanna")])
        team.score += 50
        self.assertTrue(team.score == 50)

    def test_team_class_get_dict_team(self):
        team = Team("Severozapada", [Player("Petar"), Player("Yoanna")])
        res = team.get_dict_team()
        expected = {"Severozapada": [
        {"Petar": {"cards": [], "announcements": [], "points": 0}},
        {"Yoanna": {"cards": [], "announcements": [], "points":0}}]}
        self.assertEqual(res, expected)


class test_round_class(unittest.TestCase):

    def test_round_class_get_dict_round(self):
        first_team = Team("Severozapada", [Player("Petar"), Player("Yoanna")])
        second_team = Team("Ne_moga_da_izmislq_dr_ime", [Player("Metar"), Player("Ivana")])
        round_1 = Round([first_team, second_team], 1)
        res = round_1.get_dict_round()
        expected = {"round 1": [
        {"Severozapada": [
        {"Petar": {"cards": [], "announcements": [], "points": 0}},
        {"Yoanna": {"cards": [],"announcements": [], "points": 0}}]}
        ,{"Ne_moga_da_izmislq_dr_ime": [
        {"Metar": {"cards": [], "announcements": [], "points": 0}},
        {"Ivana": {"cards": [], "announcements": [], "points": 0}}]}
        ]}
        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
