from random import randint as rand
from copy import deepcopy
'''
тествам си качването
'''
card_deck = ["7s", "8s", "9s", "10s", "Js", "Qs","Ks","As",
"7d", "8d", "9d", "10d", "Jd", "Qd", "Kd", "Ad",
"7c", "8c", "9c", "10c", "Jc", "Qc", "Kc", "Ac",
"7h", "8h", "9h", "10h", "Jh", "Qh", "Kh", "Ah"
]

lst_calls = ["Clubs", "Diamonds", "Hearts", "Spades", "No trumps", "All trumps"]

def random_call():
    n = rand(0,len(lst_calls)-1)

    return lst_calls[n]

def create_deck_copy():
    return deepcopy(card_deck)

def random_hand(card_deck_cp):
    lst_hand = []

    for x in range(0,8):
        n = rand(0,len(card_deck_cp)-1)
        lst_hand.append(card_deck_cp[n])
        card_deck_cp.remove(card_deck_cp[n])

    return lst_hand

#sorting by the suits(7 8 9 10 J->11 Q->12 K->13 A->14)
def inner_sort(lst):
    if lst == []:
        return lst
    else:
        l = []
        l2 = []

        #getting the rank 
        rank = lst[0][-1:]

        for x in lst:
            #take only the suite
            x = x[:-1]

            if x == "J":
                x = "11"
            elif x == "Q":
                x = "12"
            elif x == "K":
                x = "13"
            elif x == "A":
                x = "14"

            l.append(int(x))
        l.sort()

    return [str(card)+rank for card in l]

def sort(lst):
    list_with_clubs=[]
    list_with_dimonds=[]
    list_with_hearts=[]
    list_with_spades=[]
#four lists with each rank

    for card in lst:
        if len(card) == 2:
            if card[1] == "c":
                list_with_clubs.append(card)

            elif card[1] == "d":
                list_with_dimonds.append(card)

            elif card[1] == "h":
                list_with_hearts.append(card)

            elif card[1] == "s":
                list_with_spades.append(card)

        if len(card) == 3:
            if card[2] == "c":
                list_with_clubs.append(card)

            elif card[2] == "d":
                list_with_dimonds.append(card)

            elif card[2] == "h":
                list_with_hearts.append(card)

            elif card[2] == "s":
                list_with_spades.append(card)

    list_with_clubs = inner_sort(list_with_clubs)
    list_with_dimonds = inner_sort(list_with_dimonds)
    list_with_hearts = inner_sort(list_with_hearts)
    list_with_spades = inner_sort(list_with_spades)

    final_list_with_sorted_cards = []

    final_list_with_sorted_cards.append(list_with_clubs)
    final_list_with_sorted_cards.append(list_with_dimonds)
    final_list_with_sorted_cards.append(list_with_hearts)
    final_list_with_sorted_cards.append(list_with_spades)

    return final_list_with_sorted_cards

def has_belote(cards):
    if len(cards) == 0:
        return []

    else:
        result =[]
        count =  0
        for card in cards:
            if card[:-1] == '12':
                count += 1
                result.append(card)

            elif card[:-1] == '13':
                count += 1
                result.append(card)

        if count == 2:
            return result
        else: 
            return []

def has_tierce(cards):
    if len(cards) < 3:
        return []
    else:
        count = 1
        result = []
        for i in range(len(cards)):
            if i != len(cards) - 1 and int(cards[i+1][:-1]) == int(cards[i][:-1]) + 1:
                count += 1
                result.append(cards[i])
            #include the last card from the seqence
            elif count == 3 and int(cards[i][:-1]) == int(cards[i - 1][:-1]) + 1:
                result.append(cards[i])
                
                return result
            #the sequence is breaked
            else:
                count = 1
                result.clear()

        return []

def has_quatre(cards):
    if len(cards) < 4:
        return []
    else:
        count = 1
        result = []
        for i in range(len(cards)):
            if i != len(cards) - 1 and int(cards[i+1][:-1]) == int(cards[i][:-1]) + 1:
                count += 1
                result.append(cards[i])
            #include the last card from the seqence
            elif count == 4 and int(cards[i][:-1]) == int(cards[i - 1][:-1]) + 1:
                result.append(cards[i])
                
                return result
            #the sequence is breaked
            else:
                count = 1
                result.clear()

        return []

def has_quinte(cards):
    if len(cards) < 5:
        return []
    else:
        count = 1
        result = []
        for i in range(len(cards)):
            if i != len(cards) - 1 and int(cards[i+1][:-1]) == int(cards[i][:-1]) + 1:
                count += 1
                result.append(cards[i])

            #include the last card from the seqence
            elif count >= 5 and int(cards[i][:-1]) == int(cards[i - 1][:-1]) + 1:
                result.append(cards[i])
                
                return result
            #the sequence is breaked
            else:
                count = 1
                result.clear()

        return []

def check_for_announcements(sorted_cards):
    announcements = {'belote': [],
    'tierce': [],
    'quatre': [],
    'quinte': [],
    'carre of 9s': [],
    'carre of Js': [],
    'carre': []
    }
    announcement = {}

    result = {}


    if len(has_belote(sorted_cards)) > 0:
        announcements['belote'] =  has_belote(sorted_cards)

    if len(has_tierce(sorted_cards)) > 0:
        announcements['tierce'] = has_tierce(sorted_cards)

    if len(has_quatre(sorted_cards)) > 0:
        announcements['quatre'] = has_quatre(sorted_cards)

    if len(has_quinte(sorted_cards)) > 0:
        announcements['quinte'] = has_quinte(sorted_cards)

    for key, value in announcements.items():
        if len(value) != 0:
            result[key] = value

    return result

#for one player at the round 
def announcements(sorted_cards, round_call):
    announcements = {'belote': [],
    'tierce': [],
    'quatre': [],
    'quinte': [],
    'carre of 9s': [],
    'carre of Js': [],
    'carre': []
    }
    result = {}

    if round_call == 'Clubs':
        return check_for_announcements(sorted_cards[0])

    elif round_call == 'Diamonds':
        return check_for_announcements(sorted_cards[1])

    elif round_call == 'Hearts':
        return check_for_announcements(sorted_cards[2])

    elif round_call == 'Spades':
        return check_for_announcements(sorted_cards[3])

    elif round_call == 'All trumps':
        dic1 = check_for_announcements(sorted_cards[0])
        dic2 = check_for_announcements(sorted_cards[1])
        dic3 = check_for_announcements(sorted_cards[2])
        dic4 = check_for_announcements(sorted_cards[3])

        for key, value in dic1.items():
            announcements[key].append(value)

        for key, value in dic2.items():
            announcements[key].append(value)

        for key, value in dic3.items():
            announcements[key].append(value)

        for key, value in dic4.items():
            announcements[key].append(value)

        #cannot have more than one belote in one round
        if len(announcements['belote']) > 1:
            announcements['belote'] = announcements['belote'][0]

        for key, value in announcements.items():
            if len(value) != 0:
                result[key] = value

        return result
    else:
        return {}

def points(announcements):
    if announcements == []:
        return 0

    else:
        list_with_points = []

        for announce in announcements:
            if announce == 'belote':
                list_with_points.append(20)

            elif announce == 'tierce':
                list_with_points.append(20)

            elif announce == 'quarte':
                list_with_points.append(50)

            elif announce == 'quinte':
                list_with_points.append(100)

            elif announce == 'carre of 9s':
                list_with_points.append(150)

            elif announce == 'carre of Js':
                list_with_points.append(200)

        return list_with_points

