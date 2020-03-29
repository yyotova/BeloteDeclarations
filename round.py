# from Cls import Player, Team
from utls import random_hand, sort, create_deck_copy, random_call, announcements
from copy import deepcopy
'''
from belote import get_players
'''

def team_announcements(first_player, second_player):
    first_player_cp = deepcopy(first_player)
    for key, value in second_player.items():
        if key in first_player_cp:
            for cards in value:
                first_player_cp[key].append(cards)
        else:
            first_player_cp[key] = value
    return first_player_cp

def compare_team_announcements(first_team, second_team):
    if len(first_team) == 0 and len(second_team) == 0:
        return [{},{}]

    elif len(first_team) == 0:
        return [{}, second_team]
    elif len(second_team) == 0:
        return[first_team, {}]
    else:

        if 'tierce' in first_team and ('quinte' in second_team or 'quatre' in second_team):
            first_team['tierce'] = []
        if 'tierce' in second_team and ('quinte' in first_team or 'quatre' in first_team):
            second_team['tierce'] = []
        if 'quatre' in first_team and 'quinte' in second_team:
            first_team['quatre'] = []
        if 'quatre' in second_team and 'quinte' in first_team:
            second_team['quatre'] = []

        if 'tierce' in first_team and 'tierce' in second_team:
            for tierce in first_team['tierce']:
                suite = int(tierce[2][:-1])
                for tierce2  in second_team['tierce']:
                    suite2 = int(tierce2[2][:-1])
                    if suite2 > suite:
                        first_team['tierce'].remove(tierce)
                        break
            for tierce in second_team['tierce']:
                suite = int(tierce[2][:-1])
                for tierce2  in first_team['tierce']:
                    suite2 = int(tierce2[2][:-1])
                    if suite2 > suite:
                        second_team['tierce'].remove(tierce)
                        break
            for tierce in first_team['tierce']:
                suite = int(tierce[2][:-1])
                for tierce2  in second_team['tierce']:
                    suite2 = int(tierce2[2][:-1])
                    if suite2 == suite:
                        first_team['tierce'].remove(tierce)
                        second_team['tierce'].remove(tierce2)

        if 'quatre' in first_team and 'quatre' in second_team:
            for quatre in first_team['quatre']:
                suite = int(quatre[2][:-1])
                for quatre2  in second_team['quatre']:
                    suite2 = int(quatre2[2][:-1])
                    if suite2 > suite:
                        first_team['quatre'].remove(quatre)
                        break
            for quatre in second_team['quatre']:
                suite = int(quatre[2][:-1])
                for quatre2  in first_team['quatre']:
                    suite2 = int(quatre2[2][:-1])
                    if suite2 > suite:
                        second_team['quatre'].remove(quatre)
                        break
            for quatre in first_team['quatre']:
                suite = int(quatre[2][:-1])
                for quatre2  in second_team['quatre']:
                    suite2 = int(quatre2[2][:-1])
                    if suite2 == suite:
                        first_team['quatre'].remove(quatre)
                        second_team['quatre'].remove(quatre2)

        if 'quinte' in first_team and 'quinte' in second_team:
            for quinte in first_team['quinte']:
                suite = int(quinte[-1][:-1])
                for quinte2  in second_team['quinte']:
                    suite2 = int(quinte2[-1][:-1])
                    if suite2 > suite:
                        first_team['quinte'].remove(quinte)
                        break
            for quinte in second_team['quinte']:
                suite = int(quinte[-1][:-1])
                for quinte2  in first_team['quinte']:
                    suite2 = int(quinte2[-1][:-1])
                    if suite2 > suite:
                        second_team['quinte'].remove(quinte)
                        break
            for quinte in first_team['quinte']:
                suite = int(quinte[2][:-1])
                for quinte2  in second_team['quinte']:
                    suite2 = int(quinte2[2][:-1])
                    if suite2 == suite:
                        first_team['quinte'].remove(quinte)
                        second_team['quinte'].remove(quinte2)


        return[first_team, second_team]

def final_announcements(announce_player, team_announcements):
    if len(announce_player) == 0 and len(team_announcements) == 0:
        return []
    else:
        for announce, value in team_announcements.items():
            if announce in announce_player:
                for a in announce_player[announce]:
                    if a not in value:
                        announce_player[announce].remove(a)
        return list(key for key in announce_player.keys() if len(announce_player[key]) > 0)

def round():
    # call = random_call()
    # call = 'All trumps'
    # card_deck=create_deck_copy()
    # announcements_of_the_first_team ={}
    # announcements_of_the_second_team ={}

    # first_team=Team("Nie",[Player("Gosho"),Player("Pesho")])
    # second_team=Team("Vie",[Player("Kiro"),Player("Miro")])
    
    # print('rank: ', call)
    # #Player1(first team)
    # # first_team.lst_players[0].cards =random_hand(card_deck) 
    # first_team.lst_players[0].cards = ['Ad', 'Qd', 'Kc', 'Jc', '7h', '9c', 'Kh', '8d']
    # print('Cards Player1: ', first_team.lst_players[0].cards)

    # print('announcements:', announcements(sort(first_team.lst_players[0].cards), call))
    # announcements_first_player = announcements(sort(first_team.lst_players[0].cards), call)
   
    # #Player2(second team)
    # # second_team.lst_players[0].cards =random_hand(card_deck)
    # second_team.lst_players[0].cards = ['9d', 'Ac', 'Jd', '10c', 'Kd', 'Qc', 'Ah', '10d'] 
    # print('Cards Player2: ', second_team.lst_players[0].cards)

    # print('announcements:', announcements(sort(second_team.lst_players[0].cards), call))
    # announcements_second_player = announcements(sort(second_team.lst_players[0].cards), call)
   
    # #Player3(first team)
    # # first_team.lst_players[1].cards =random_hand(card_deck) 
    # first_team.lst_players[1].cards = ['10h', '7c', '8s', '10s', 'Qh', 'As', '8c', 'Jh']
    # print('Cards Player3: ', first_team.lst_players[1].cards)

    # print('announcements:', announcements(sort(first_team.lst_players[1].cards), call))
    # announcements_third_player = announcements(sort(first_team.lst_players[1].cards), call)
    
    # #Player4(second team)
    # # second_team.lst_players[1].cards =random_hand(card_deck)
    # second_team.lst_players[1].cards = ['Qs', '7s', '7d', '8h', 'Js', 'Ks', '9s', '9h']
    # print('Cards Player4: ', second_team.lst_players[1].cards)

    # print('announcements:', announcements(sort(second_team.lst_players[1].cards), call))
    # announcements_fourth_player = announcements(sort(second_team.lst_players[1].cards), call)

    # announcements_of_the_first_team = team_announcements(announcements_first_player, announcements_third_player)
    # announcements_of_the_second_team = team_announcements(announcements_second_player, announcements_fourth_player)

    # new_announcements_first_team = compare_team_announcements(announcements_of_the_first_team, announcements_of_the_second_team)[0]
    # new_announcements_second_team = compare_team_announcements(announcements_of_the_first_team, announcements_of_the_second_team)[1]

    # print('final announcementsTeam1: ', new_announcements_first_team)
    # print('final announcementsTeam2: ', new_announcements_second_team)

    # first_team.lst_players[0].announcements = final_announcements(announcements_first_player, new_announcements_first_team)
    # first_team.lst_players[1].announcements = final_announcements(announcements_third_player, new_announcements_first_team)

    # second_team.lst_players[0].announcements = final_announcements(announcements_second_player, new_announcements_second_team)
    # second_team.lst_players[1].announcements = final_announcements(announcements_fourth_player, new_announcements_second_team)

    # print('final announcementsPlayer1: ', first_team.lst_players[0].announcements)
    # print('final announcementsPlayer2: ', second_team.lst_players[0].announcements)
    # print('final announcementsPlayer3: ', first_team.lst_players[1].announcements)
    # print('final announcementsPlayer4: ', second_team.lst_players[1].announcements)

    pass





def main():
    round()

if __name__ == '__main__':
    main()