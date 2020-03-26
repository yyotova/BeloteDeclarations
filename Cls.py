class Player:
	def __init__(self,name):
		self.name=name
		self.lst_hand=[]
		#get belot 50,100 etc
		self.announcements=[]
		#get points after round
		self.points=0

	def __str__(self):
		return "{0}->{1}".format(self.name,self.lst_hand)
	
	def __repr__(self):
		return "{0}->{1}".format(self.name,self.lst_hand)
	
	def get_hand(self, lst_hand):
		self.lst_hand = lst_hand

	def get_announcements(self,announcements_list):
		#check for belot 30 ,50, 100
		self.announcements=announcements_list

	def get_points(self,points):
		#get points of player 
		self.points=points

class Team:
	def __init__(self,name,lst_player):
		self.name=name
		self.lst_player=lst_player
		self.score=0

	def __str__(self):
		return str(self.name)
	def update_score(self,score):
		self.score+=score
	def get_players(self):
		return self.lst_player