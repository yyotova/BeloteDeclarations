import unittest
from Cls import Player,Team,create_hand
class test_list_hand(unittest.TestCase):
	# def test_hand_of_player(self):
	# 	l=create_hand()
	# 	l1=create_hand()
	# 	l2=create_hand()
	# 	l3=create_hand()
	# 	print(l)
	# 	print(l1)
	# 	print(l2)
	# 	print(l3)
	pass
class test_player_class(unittest.TestCase):
	def test_player_class_hand_add(self):
		player=Player("Gosho")
		player.get_hand(create_hand())
		print(player)

if __name__ == '__main__':
	unittest.main()