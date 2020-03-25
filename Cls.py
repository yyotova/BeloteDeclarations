from random import randint as rand
from copy import deepcopy
card_deck=["7s", "8s", "9s", "10c", "Jd", "Qd","Kd","As",
"7c", "8d", "9c", "10s", "Jh", "Qc", "Kc", "Ad",
"7c", "8d", "9c", "10s", "Jh", "Qc", "Kc", "Ad",
"7h", "8h", "9h", "10h", "Jc", "Qh", "Ks", "Ah"
]
card_deck_cp=deepcopy(card_deck)

def create_hand():
	lst_hand=[]
	for x in range(1,8):
		n=rand(0,len(card_deck_cp)-1)
		lst_hand.append(card_deck_cp[n])
		card_deck_cp.remove(card_deck_cp[n])
	return lst_hand

class Player:
	def __init__(self,name):
		self.name=name
		self.lst_hand=[]
	def __str__(self):
		return "{0}->{1}".format(self.name,self.lst_hand)
	
	def __repr__(self):
		return "{0}->{1}".format(self.name,self.lst_hand)
	
	def get_hand(self,lst_hand):
		self.lst_hand=lst_hand

class Team:
	def __init__(self,name,lst_player):
		self.name=name
		self.lst_player=lst_player
		self.score=0
	def __str__(self):
		return str(self.name)

