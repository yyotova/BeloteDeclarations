from random import randint as rand
from copy import deepcopy
card_deck=["7s", "8s", "9s", "10s", "Js", "Qs","Ks","As",
"7d", "8d", "9d", "10d", "Jd", "Qd", "Kd", "Ad",
"7c", "8c", "9c", "10c", "Jc", "Qc", "Kc", "Ac",
"7h", "8h", "9h", "10h", "Jh", "Qh", "Kh", "Ah"
]

lst_calls=["Clubs", "Diamonds", "Hearts", "Spades","No trumps","All trumps"]


def player_call():
	n=rand(0,len(lst_calls)-1)
	return lst_calls[n]

card_deck_cp=deepcopy(card_deck)

def create_hand():
	lst_hand=[]
	for x in range(0,8):
		n=rand(0,len(card_deck_cp)-1)
		lst_hand.append(card_deck_cp[n])
		card_deck_cp.remove(card_deck_cp[n])
	return lst_hand
#test a funcito. maybe use idk/ sort by color
#maybe dont return list but work with lists of color
def inner_sort(lst):
# 7 8 9 10 J Q K A
	l=[]
	l2=[]
	color=lst[0][-1:]
	for x in lst:
		x=x[:-1]
		if x =="J":
			x="11"
		if x =="Q":
			x="12"
		if x =="K":
			x="13"
		if x =="A":
			x="14"
		l.append(int(x))
	l.sort()
	for x in l:
		x=str(x)
		if x =="11":
			x="J"
		if x =="12":
			x="Q"
		if x =="13":
			x="K"
		if x =="14":
			x="A"
		x+=color
		l2.append(x)
	return l2

def sort(lst):
	lc=[]
	ld=[]
	lh=[]
	ls=[]
	for x in lst:
		if len(x)==2:
			if x[1]=="c":
				lc.append(x)
			if x[1]=="d":
				ld.append(x)
			if x[1]=="h":
				lh.append(x)
			if x[1]=="s":
				ls.append(x)
		if len(x)==3:
			if x[2]=="c":
				lc.append(x)
			if x[2]=="d":
				ld.append(x)
			if x[2]=="h":
				lh.append(x)
			if x[2]=="s":
				ls.append(x)
	lc=inner_sort(lc)
	ld=inner_sort(ld)
	lh=inner_sort(lh)
	ls=inner_sort(ls)
	l_end=[]
	l_end.append(ls)
	l_end.append(lh)
	l_end.append(ld)
	l_end.append(lc)
	return l_end

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
	
	def get_hand(self,lst_hand):
		self.lst_hand=lst_hand
	def get_announcements(self):
		#check for belot 30 ,50, 100
		pass
	def get_points(self):
		#get points of player 
		pass
class Team:
	def __init__(self,name,lst_player):
		self.name=name
		self.lst_player=lst_player
		self.score=0
	def __str__(self):
		return str(self.name)
'''
game.py
while gameover==False:
round()
->score
'''
