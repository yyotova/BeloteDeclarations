from utls import random_hand, sort, create_deck_copy, random_call, announcements
from copy import deepcopy

def team_announcements(first_player, second_player):
    result = {'belote': [],
    'tierce': [],
    'quatre': [],
    'quinte': [],
    'carre of 9s': [],
    'carre of 10s': [],
    'carre of Js': [],
    'carre of Qs': [],
    'carre of Ks': [],
    'carre of As': []
    }
    for key, value in first_player.items():
        if type(value[0]) == list:
            for v in value:
                result[key].append(v)
        else:
            result[key].append(value)

    for key, value in second_player.items():
        if type(value[0]) == list:
            for v in value:
                result[key].append(v)
        else:
            result[key].append(value)

    announcements = {}

    for key, value in result.items():
        if len(value) != 0:
            announcements[key] = value

    return announcements

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
