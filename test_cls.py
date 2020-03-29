import unittest
from Cls import Player,Team,Round,Game
import json

class test_player_class(unittest.TestCase):

	def test_player_class(self):
		player=Player("Gosho")
		self.assertEqual(str(player),"Gosho->[]")

	def test_player_class_get_dict_player(self):
		player=Player("Gosho")
		player_dict=player.get_dict_player()
		self.assertEqual(player_dict,{"Gosho":{"cards":[],"announcements":[],"points":0}})

class test_team_class(unittest.TestCase):

	def test_team_class(self):
		team=Team("Severozapada",[Player("Petar"),Player("Yoanna")])
		self.assertEqual(str(team),"Severozapada")

	def test_team_class_update_score(self):
		team=Team("Severozapada",[Player("Petar"),Player("Yoanna")])
		team.score+=50
		self.assertTrue(team.score==50)

	def test_team_class_get_dict_team(self):
		team=Team("Severozapada",[Player("Petar"),Player("Yoanna")])
		res=team.get_dict_team()
		expected={"Severozapada":[
		{"Petar":{"cards":[],"announcements":[],"points":0}},
		{"Yoanna":{"cards":[],"announcements":[],"points":0}}]}
		self.assertEqual(res, expected)

class test_round_class(unittest.TestCase):

	def test_round_class_get_dict_round(self):
		first_team=Team("Severozapada",[Player("Petar"),Player("Yoanna")])
		second_team=Team("Ne_moga_da_izmislq_dr_ime",[Player("Metar"),Player("Ivana")])
		round_1=Round([first_team,second_team],1)
		# round_1.add_hands_to_players()
		res=round_1.get_dict_round()
		expected={"round 1":[
		{"Severozapada":[
		{"Petar":{"cards":[],"announcements":[],"points":0}},
		{"Yoanna":{"cards":[],"announcements":[],"points":0}}]}
		,{"Ne_moga_da_izmislq_dr_ime":[
		{"Metar":{"cards":[],"announcements":[],"points":0}},
		{"Ivana":{"cards":[],"announcements":[],"points":0}}]}
		]}
		# print(json.dumps(res,indent=4))
		self.assertEqual(res, expected)

	def test_round_class_player_announcements(self):
		first_team=Team("Severozapada",[Player("Petar"),Player("Yoanna")])
		second_team=Team("Ne_moga_da_izmislq_dr_ime",[Player("Metar"),Player("Ivana")])
		round_1=Round([first_team,second_team],1)
		round_1.add_hands_to_players()
		round_1.add_announcements_to_players()
		res=round_1.get_dict_round()
		# print(json.dumps(res,indent=4))
	
	def test_round_class_player_points(self):
		first_team=Team("Severozapada",[Player("Petar"),Player("Yoanna")])
		second_team=Team("Ne_moga_da_izmislq_dr_ime",[Player("Metar"),Player("Ivana")])
		# round_1.add_hands_to_players()
		first_team.lst_players[0].cards=["7c","8c","9c","10c","Jd","Kd","Qd","As"]
		first_team.lst_players[1].cards=["7s","8d","9d","10s","Js","Kc","Qc","Ad"]
		second_team.lst_players[0].cards=["7d","8s","9s","10d","Jd","Kh","Qh","As"]
		second_team.lst_players[1].cards=["7h","8h","9h","10c","Js","Ks","Qs","Ah"]

		round_1=Round([first_team,second_team],1)

		round_1.add_announcements_to_players()
		round_1.add_points_to_player()
		round_1.add_team_score()
		res=round_1.get_dict_round()
		# print(json.dumps(res,indent=4))
		
	def test_round_class_team_score(self):
		first_team=Team("Severozapada",[Player("Petar"),Player("Yoanna")])
		second_team=Team("Ne_moga_da_izmislq_dr_ime",[Player("Metar"),Player("Ivana")])
		round_1=Round([first_team,second_team],1)
		round_1.add_hands_to_players()
		round_1.add_announcements_to_players()
		round_1.add_points_to_player()
		round_1.add_team_score()
		# round_1.add_team_score()
		# ls=[round_1.teams_lst[0].score,round_1.teams_lst[1].score]
		# print(ls)
		# print(type(round_1.teams_lst[0].score))




class test_game_class(unittest.TestCase):
	def test_game_class(self):
		first_team=Team("Severozapada",[Player("Petar"),Player("Yoanna")])
		second_team=Team("Ne_moga_da_izmislq_dr_ime",[Player("Metar"),Player("Ivana")])
		test_game=Game(1,[first_team,second_team])
		test_game.play_game()
		# print(test_game.round_lst)
		print(json.dumps(test_game.get_dict_game(),indent=4))
		


		
if __name__ == '__main__':
	unittest.main()