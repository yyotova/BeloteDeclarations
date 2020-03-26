import unittest
from Cls import Player,Team
from utls import random_hand, random_call, sort

class test_call(unittest.TestCase):
	def test_call_of_player(self):
		s = random_call()
		# print(s)

class test_player_class(unittest.TestCase):
	def test_player_class_hand_add(self):
		player=Player("Gosho")
		player.get_hand(random_hand())
		# print(player)

class test_sort(unittest.TestCase):
	def test_sort(self):
		l = random_hand()

		print(l)
		print(sort(l))

if __name__ == '__main__':
	unittest.main()