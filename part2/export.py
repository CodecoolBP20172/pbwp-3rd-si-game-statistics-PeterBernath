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


def export_answers(title, file_name='game_stat.txt', exp_file_name='game_stat_export.txt'):
    with open(exp_file_name, 'w') as f:
        [f.write('The title of the most played game is %s \n\n' % get_most_played(file_name))]
        [f.write('%s million copies have been sold in total \n\n' % sum_sold(file_name))]
        [f.write('The average selling was %s million \n\n' % round(get_selling_avg(file_name), 2))]
        [f.write('The longest title is %s characters long \n\n' % count_longest_title(file_name))]
        [f.write('The average of the release dates is %s \n\n' % get_date_avg(file_name))]
        results = get_game(file_name, title)
        [f.write('The chosen game has these properties: \n\n')]
        [f.write('Title: %s\n' % results[0])]
        [f.write('Total copies sold (million): %s\n' % results[1])]
        [f.write('Release date: %s\n' % results[2])]
        [f.write('Genre: %s\n' % results[3])]
        [f.write('Publisher: %s \n\n' % results[4])]
        results = count_grouped_by_genre(file_name)
        [f.write('Number of games in genres: \n\n')]
        [f.write('{0} : {1}\n'.format(key, value)) for key, value in results.items()]
        [f.write('\n')]
        results = get_date_ordered(file_name)
        [f.write('Date ordered list of the games: \n\n')]
        for i in range(len(results)):
            [f.write(results[i])]
            [f.write('\n')]


def main():
    export_answers('Minecraft')


main()
