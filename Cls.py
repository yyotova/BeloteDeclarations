card_deck=["7s", "8s", "9s", "10c", "Jd", "Qd","Kd","As",
"7c", "8d", "9c", "10s", "Jh", "Qc", "Kc", "Ad",
"7c", "8d", "9c", "10s", "Jh", "Qc", "Kc", "Ad",
"7h", "8h", "9h", "10h", "Jc", "Qh", "Ks", "Ah"
]


class Player:
	def __init__(self,name):
		self.name=name
		self.lst_hand
	def __str__(self):
		return str(self.name)
	def __repr__(self):
		return "{0}->{1}".format(self.name,self.hand)
	def get_hand(self,lst_hand):
		self.lst_hand=lst_hand
class Team:
	def __init__(self,name,lst_player):
		self.name=name
		self.lst_player=lst_player
		self.score=0
	def __str__(self):
		return str(self.name)
