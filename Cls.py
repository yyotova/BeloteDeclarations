from utls import announcements
from utls import create_deck_copy,random_hand
from utls import sort, random_call, announcements,points

class Player:
    def __init__(self,name):
        self.name=name
        self.cards=[]
        #get belot 50,100 etc
        self.announcements=[]
        #get points after round
        self.points = 0

    def __str__(self):
        return "{0}->{1}".format(self.name,self.cards)
    
    def __repr__(self):
        return "{0}->{1}".format(self.name,self.cards)
    
    def get_dict_player(self):
        return {self.name:{"cards":self.cards,"announcements":self.announcements,"points":self.points}}

class Team:
    def __init__(self,name,lst_players):
        self.name = name
        self.lst_players = lst_players
        self.score = 0

    def __str__(self):
        return str(self.name)
    
    def get_dict_team(self):
        return {self.name:[self.lst_players[0].get_dict_player(),self.lst_players[1].get_dict_player()]}

    def __add__(self,other):
        return self.score+other.score

class Round:
    def __init__(self,teams_lst ,round_number):
        self.teams_lst=teams_lst
        self.round_number=round_number
    
    def __str__(self):
        return "round {0}".format(self.round_number)

    def __repr__(self):
        return str(self)
        
    def get_dict_round(self):
        round_number="round "+str(self.round_number)
        return {round_number:[self.teams_lst[0].get_dict_team(),self.teams_lst[1].get_dict_team()]}

    def add_hands_to_players(self):
        card_deck=create_deck_copy()
        for teams in self.teams_lst:
                for player in teams.lst_players:
                        player.cards=random_hand(card_deck)    

    def add_announcements_to_players(self,call="All trumps"):
        for teams in self.teams_lst:
                for player in teams.lst_players:
                        player.announcements=announcements(sort(player.cards),call)

    def add_points_to_player(self):
        for teams in self.teams_lst:
                for player in teams.lst_players:
                        player.points=points(player.announcements)

    def add_team_score(self):
        self.teams_lst[0].score+=sum(self.teams_lst[0].lst_players[0].points)+sum(self.teams_lst[0].lst_players[1].points)
        self.teams_lst[1].score+=sum(self.teams_lst[1].lst_players[0].points)+sum(self.teams_lst[1].lst_players[1].points)

class Game:

    def __init__(self,game_number,teams_lst,game_score=None):
        self.game_number=game_number
        self.teams_lst=teams_lst
        self.round_lst=[]
        if game_score==None:
            self.game_score=[]
        else:
            self.game_score=game_score

    def play_game(self):
        round_counter=0
        while self.teams_lst[0].score<=150 and self.teams_lst[1].score<=150:
            game_round=Round(self.teams_lst,round_counter)
            game_round.add_hands_to_players()
            game_round.add_announcements_to_players()
            game_round.add_points_to_player()
            game_round.add_team_score()
            self.round_lst.append(game_round)
            round_counter+=1

    def get_dict_game(self):
        game_number_str="game {0}".format(self.game_number)
        pass

    def save_score(file):
        pass