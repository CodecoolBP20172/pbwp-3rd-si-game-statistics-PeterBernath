from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title
from reports import sort_abc
from reports import get_genres
from reports import when_was_top_sold_fps


def print_games_count(file_name='game_stat.txt'):
    print("There are %s games in the file \n" % count_games(file_name))


def print_decide(year, file_name='game_stat.txt'):
    if decide(file_name, year) is True:
        print("Yes, there is a game from year %s\n" % year)
    else:
        print("No, there isn't a game from that year")


def print_latest(file_name='game_stat.txt'):
    print("The latest game from the list is %s\n" % get_latest(file_name))


def print_genre_count(genre, file_name='game_stat.txt'):
    print("There are %s games of that genre in the list\n" % count_by_genre(file_name, genre))


def print_game_line(title, file_name='game_stat.txt'):
    print("The line number of the given game is %s\n\n" % get_line_number_by_title(file_name, title))


def print_ordered_list(file_name='game_stat.txt'):
    sorted_list = sort_abc(file_name)
    print("The alphabetical ordered list of the titles is: \n")
    for i in range(len(sorted_list)):
        print(sorted_list[i])
    print("\n")


def print_genres(file_name='game_stat.txt'):
    genres = get_genres('game_stat.txt')
    print("The genres in the list are: \n")
    for i in range(len(genres)):
        print(genres[i])
    print("\n")


def print_top_sold_fps_release(file_name='game_stat.txt'):
    print("The top sold First-person shooter game was released in year %s. \n" % when_was_top_sold_fps(file_name))


def main():
    print_games_count()
    print_decide(2000)
    print_latest()
    print_genre_count('First-person shooter')
    print_game_line('EverQuest')
    print_ordered_list()
    print_genres()
    print_top_sold_fps_release()


main()
