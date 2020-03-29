from Cls import Player,Team
from utls import random_hand, sort, create_deck_copy, random_call, announcements
'''
from belote import get_players
'''

def team_announcements(first_player, second_player):
    for key, value in second_player.items():
        if key in first_player:
            for cards in value:
                first_player[key].append(cards)
        else:
            first_player[key] = value
    return first_player

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

def round():
    # call = random_call()
    call = 'All trumps'
    card_deck=create_deck_copy()
    announcements_of_the_first_team ={}
    announcements_of_the_second_team ={}

    first_team=Team("Nie",[Player("Gosho"),Player("Pesho")])
    second_team=Team("Vie",[Player("Kiro"),Player("Miro")])
    
    print('rank: ', call)
    #Player1(first team)
    first_team.lst_players[0].cards =random_hand(card_deck) 
    print('Cards Player1: ', first_team.lst_players[0].cards)

    print('announcements:', announcements(sort(first_team.lst_players[0].cards), call))
    announcements_first_player = announcements(sort(first_team.lst_players[0].cards), call)
   
    first_team.lst_players[0].announcements = list(announcements_first_player.keys())
    print(first_team.lst_players[0].announcements)

    #Player2(second team)
    second_team.lst_players[0].cards =random_hand(card_deck)
    print('Cards Player2: ', second_team.lst_players[0].cards)

    print('announcements:', announcements(sort(second_team.lst_players[0].cards), call))
    announcements_second_player = announcements(sort(second_team.lst_players[0].cards), call)
   
    second_team.lst_players[0].announcements = list(announcements_second_player.keys())
    print(second_team.lst_players[0].announcements)

    #Player3(first team)
    first_team.lst_players[1].cards =random_hand(card_deck) 
    print('Cards Player3: ', first_team.lst_players[1].cards)

    print('announcements:', announcements(sort(first_team.lst_players[1].cards), call))
    announcements_third_player = announcements(sort(first_team.lst_players[1].cards), call)
    
    first_team.lst_players[1].announcements = list(announcements_third_player.keys())
    print(first_team.lst_players[1].announcements)

    #Player4(second team)
    second_team.lst_players[1].cards =random_hand(card_deck)
    print('Cards Player4: ', second_team.lst_players[1].cards)

    print('announcements:', announcements(sort(second_team.lst_players[1].cards), call))
    announcements_fourth_player = announcements(sort(second_team.lst_players[1].cards), call)

    second_team.lst_players[1].announcements = list(announcements_fourth_player.keys())
    print(second_team.lst_players[1].announcements)

    announcements_of_the_first_team = team_announcements(announcements_first_player, announcements_third_player)
    announcements_of_the_second_team = team_announcements(announcements_second_player, announcements_fourth_player)

    print('announcements of the first team: ', announcements_of_the_first_team)
    print('announcements of the second team: ', announcements_of_the_second_team)

    print(compare_team_announcements(announcements_of_the_first_team, announcements_of_the_second_team))


def main():
    round()

if __name__ == '__main__':
    main()