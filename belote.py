from Cls import Game, Team, Player
from file import create_file_result, write_end_of_file
import json


def main():
    first_team_name = input("Team 1 name: ")
    second_team_name = input("Team 2 name: ")

    firts_team_players = input(f'"{first_team_name}" players: ').split(",")
    second_team_players = input(f'"{second_team_name}" players: ').split(",")

    player1_first_team = firts_team_players[0]
    player2_first_team = firts_team_players[1]

    player1_second_team = second_team_players[0]
    player2_second_team = second_team_players[1]

    player_one = Player(player1_first_team)
    player_two = Player(player2_first_team)
    player_three = Player(player1_second_team)
    player_four = Player(player2_second_team)

    first_team = Team(first_team_name, [player_one, player_two])
    second_team = Team(second_team_name, [player_three, player_four])

    score = [0, 0]
    count_games = 1

    json_file = open("data.json", "w")
    json_file.close()
    json_file = open("data.json", "a")
    file = create_file_result([first_team, second_team])

    while score[0] < 2 and score[1] < 2:
        game = Game(count_games, [first_team, second_team], score)
        game.play_game(file.name)
        json.dump(game.get_dict_game(), json_file, indent=4)
        score = game.update_score()
        write_end_of_file(score, file.name)
        count_games += 1

    json_file.close()
    file.close()


if __name__ == '__main__':
    main()
