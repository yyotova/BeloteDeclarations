from random import randint as rand
from copy import deepcopy

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