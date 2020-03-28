from Cls import Player,Team
from utls import random_hand, sort, create_deck_copy, random_call, announcements
'''
from belote import get_players
'''
def round():
    call = random_call()
    card_deck=create_deck_copy()
    announcements_of_the_first_team =[]
    announcements_of_the_second_team =[]

    first_team=Team("Nie",[Player("Gosho"),Player("Pesho")])
    second_team=Team("Vie",[Player("Kiro"),Player("Miro")])
    
    print('rank: ', call)
    #Player1(first team)
    first_team.lst_players[0].cards =random_hand(card_deck) 
    print('Cards Player1: ', first_team.lst_players[0].cards)

    print('announcements:', announcements(sort(first_team.lst_players[0].cards), call))
    announcements_first_player = announcements(sort(first_team.lst_players[0].cards), call)
    announcements_of_the_first_team.append(announcements_first_player)
    first_team.lst_players[0].announcements = list(announcements_first_player.keys())
    print(first_team.lst_players[0].announcements)

    #Player2(second team)
    second_team.lst_players[0].cards =random_hand(card_deck)
    print('Cards Player2: ', second_team.lst_players[0].cards)

    print('announcements:', announcements(sort(second_team.lst_players[0].cards), call))
    announcements_second_player = announcements(sort(second_team.lst_players[0].cards), call)
    announcements_of_the_second_team.append(announcements_second_player)
    second_team.lst_players[0].announcements = list(announcements_second_player.keys())
    print(second_team.lst_players[0].announcements)

    #Player3(first team)
    first_team.lst_players[1].cards =random_hand(card_deck) 
    print('Cards Player1: ', first_team.lst_players[1].cards)

    print('announcements:', announcements(sort(first_team.lst_players[1].cards), call))
    announcements_third_player = announcements(sort(first_team.lst_players[1].cards), call)
    announcements_of_the_first_team.append(announcements_third_player)
    first_team.lst_players[1].announcements = list(announcements_third_player.keys())
    print(first_team.lst_players[1].announcements)

    #Player4(second team)
    second_team.lst_players[1].cards =random_hand(card_deck)
    print('Cards Player2: ', second_team.lst_players[1].cards)

    print('announcements:', announcements(sort(second_team.lst_players[1].cards), call))
    announcements_fourth_player = announcements(sort(second_team.lst_players[1].cards), call)
    second_team.lst_players[1].announcements = list(announcements_fourth_player.keys())
    print(second_team.lst_players[1].announcements)

def main():
    round()

if __name__ == '__main__':
    main()