def main():
	first_team = input("Team 1 name: ")
	second_team = input("Team 2 name: ")

	firts_team_players = input(f'{first_team} players: ').split(",")
	second_team_players = input(f'{second_team} players: ').split(",")

	player1_first_team = firts_team_players[0]
	player2_first_team =firts_team_players[1]

	player1_second_team = second_team_players[0]
	player2_second_team = second_team_players[1]


if __name__ == '__main__':
	main()