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

card_deck_cp = deepcopy(card_deck)
def random_hand(card_deck_for_the_round):
    lst_hand = []

    for x in range(0,8):
        n = rand(0,len(card_deck_for_the_round)-1)
        lst_hand.append(card_deck_for_the_round[n])
        card_deck_for_the_round.remove(card_deck_for_the_round[n])

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
    lc=[]
    ld=[]
    lh=[]
    ls=[]
#four lists with each rank
    for x in lst:
        if len(x)==2:
            if x[1]=="c":
                lc.append(x)
            elif x[1]=="d":
                ld.append(x)
            elif x[1]=="h":
                lh.append(x)
            elif x[1]=="s":
                ls.append(x)
        if len(x)==3:
            if x[2]=="c":
                lc.append(x)
            elif x[2]=="d":
                ld.append(x)
            elif x[2]=="h":
                lh.append(x)
            elif x[2]=="s":
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
