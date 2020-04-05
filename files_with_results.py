def create_file_result(team_list):
    file = open("result.txt", "w")

    first_line = "\t{0}\t|\t{1}\t\n".format(team_list[0], team_list[1])
    file.write(first_line)
    file.write("======================")

    file.close()
    return file


def write_to_file(team_list_score, file):
    file = open(file, "a")

    score_line = "\n{0}\t|{1}\t".format(team_list_score[0], team_list_score[1])
    file.write(score_line)

    file.close()


def write_end_of_file(team_list_game_score, file):
    file = open(file, "a")

    score_line = "\n\t{0}\t|\t{1}\t".format(team_list_game_score[0], team_list_game_score[1])
    file.write(score_line)
    file.write("\n======================")

    file.close()


def create_json_file():
    file = open("data.json", "a")
    file.close()
    return file
