from Cls import Player,Team
from utls import random_hand,sort,create_deck_copy
'''
from belote import get_players
'''
def round():
	card_deck=create_deck_copy()
	#players_lst=get_players()
	'''
	make static for now get from main func later
	for testing
	'''
	t1=Team("Nie",[Player("Gosho"),Player("Pesho")])
	t2=Team("Vie",[Player("Kiro"),Player("Miro")])

	for  x  in t1.get_players():
		x.get_hand(random_hand(card_deck))
	for  x  in t2.get_players():
		x.get_hand(random_hand(card_deck))
	for x in t1.get_players():
		print(x)
	for x in t2.get_players():
		print(x)
	for x in t1.get_players():
		print((sort(x.lst_hand)))
	for x in t2.get_players():
		print((sort(x.lst_hand)))
def main():
	round()
	round()
if __name__ == '__main__':
	main()