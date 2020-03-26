from Cls import Player,Team
from Cls import create_hand,sort
'''
from belote import get_players
'''
def round():

	#players_lst=get_players()
	'''
	make static for now get from main func later
	for testing
	'''
	t1=Team("Nie",[Player("Gosho"),Player("Pesho")])
	t2=Team("Vie",[Player("Kiro"),Player("Miro")])

	for  x  in t1.get_players():
		x.set_hand(create_hand())
	for  x  in t2.get_players():
		x.set_hand(create_hand())
	for x in t1.get_players():
		print(x)
	for x in t2.get_players():
		print(x)
	for x in t1.get_players():
		print((sort(x.lst_hand)))
	for x in t2.get_players():
		print((sort(x.lst_hand)))
