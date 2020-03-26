from Cls import Player,Team
from utls import random_hand, sort, create_deck_copy, random_call
'''
from belote import get_players
'''
def round():
	call = random_call()
	card_deck=create_deck_copy()
	#players_lst=get_players()
	'''
	make static for now get from main func later
	for testing
	'''
	'''
	   Редът на играчите е друг!  
	'''
	announcements_of_the_first_team =[]
	announcements_of_the_second_team =[]

	first_team=Team("Nie",[Player("Gosho"),Player("Pesho")])
	second_team=Team("Vie",[Player("Kiro"),Player("Miro")])

	for  player  in first_team.lst_players:
		player.set_hand(random_hand(card_deck))

	for  player  in second_team.lst_players:
		player.set_hand(random_hand(card_deck))

	for player in first_team.lst_players:
		print(player)

	for player in second_team.lst_players:
		print(player)

	for player in first_team.lst_players:
		print((sort(player.lst_hand)))

	for player in second_team.lst_players:
		print((sort(player.lst_hand)))

def main():
	round()
	round()

if __name__ == '__main__':
	main()