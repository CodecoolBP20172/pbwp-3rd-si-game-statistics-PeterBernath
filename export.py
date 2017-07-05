from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title
from reports import sort_abc
from reports import get_genres
from reports import when_was_top_sold_fps


def export_answers(year, genre, title, file_name='game_stat.txt', exp_file_name='game_stat_export.txt'):
    with open(exp_file_name, 'w') as f:
        [f.write("There are %s games in the file \n\n" % count_games(file_name))]
        if decide(file_name, year) is True:
            [f.write("Yes, there is a game from year %s\n\n" % year)]
        else:
            [f.write("No, there isn't a game from that year\n\n")]
        [f.write("The latest game from the list is %s\n\n" % get_latest(file_name))]
        [f.write("There are %s games of that genre in the list\n\n" % count_by_genre(file_name, genre))]
        [f.write("The line number of the given game is %s\n\n" % get_line_number_by_title(file_name, title))]
        sorted_list = sort_abc(file_name)
        [f.write("The alphabetical ordered list of the titles is: \n")]
        for i in range(len(sorted_list)):
            [f.write(sorted_list[i])]
            [f.write(", ")]
        [f.write("\n\n")]
        genres = get_genres(file_name)
        [f.write("The genres in the list are: \n")]
        for i in range(len(genres)):
            [f.write(genres[i])]
            [f.write(", ")]
        [f.write("\n\n")]
        [f.write("The top sold First-person shooter game was released in %s. \n" % when_was_top_sold_fps(file_name))]


def main():
    export_answers(2000, 'First-person shooter', 'EverQuest')


main()
