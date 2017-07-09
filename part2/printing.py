from reports import create_list
from reports import get_copies_sold_list
from reports import get_most_played
from reports import sum_sold
from reports import get_selling_avg
from reports import count_longest_title
from reports import get_date_avg
from reports import get_game
from reports import count_grouped_by_genre
from reports import get_date_ordered


def print_most_played(file_name='game_stat.txt'):
    print('The title of the most played game is %s \n' % get_most_played(file_name))


def print_sum_sold(file_name='game_stat.txt'):
    print('%s million copies have been sold in total \n' % sum_sold(file_name))


def print_selling_avg(file_name='game_stat.txt'):
    print('The average selling was %s million \n' % round(get_selling_avg(file_name), 2))


def print_longest_title(file_name='game_stat.txt'):
    print('The longest title is %s characters long \n' % count_longest_title(file_name))


def print_avg_date(file_name='game_stat.txt'):
    print('The average of the release dates is %s \n' % get_date_avg(file_name))


def print_get_game(title, file_name='game_stat.txt'):
    results = get_game(file_name, title)
    print('The chosen game has these properties: \n')
    print('Title: %s' % results[0])
    print('Total copies sold (million): %s' % results[1])
    print('Release date: %s' % results[2])
    print('Genre: %s' % results[3])
    print('Publisher: %s \n' % results[4])


def print_grouped_by_genre(file_name='game_stat.txt'):
    results = count_grouped_by_genre(file_name)
    print('Number of games in genres: \n')
    for kv in results.items():
        print(kv[0], ' : ', kv[1])
    print('\n')


def print_date_ordered(file_name='game_stat.txt'):
    results = get_date_ordered(file_name)
    print('Date ordered list of the games: \n')
    for i in range(len(results)):
        print(results[i])
    print('\n')


def main():
    print_most_played()
    print_sum_sold()
    print_selling_avg()
    print_longest_title()
    print_avg_date()
    print_get_game('Minecraft')
    print_grouped_by_genre()
    print_date_ordered()


main()
