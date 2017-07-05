def create_list(file_name):
    results = []
    with open(file_name) as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
        return results


def count_games(file_name):
    results = create_list(file_name)
    return len(results)


def decide(file_name, year):
    results = create_list(file_name)
    results = list(map(lambda x: [x[0], x[1], int(x[2]), x[3], x[4]], results))
    for i in range(len(results)):
        if results[i][2] == year:
            return True


def get_latest(file_name):
    results = create_list(file_name)
    latest = max(results, key=lambda x: x[2])
    latest_name = latest[0]
    return latest_name


def count_by_genre(file_name, genre):
    results = create_list(file_name)
    genre_count = sum(x.count(genre) for x in results)
    return genre_count


def get_line_number_by_title(file_name, title):
    try:
        results = create_list(file_name)
        for i in range(len(results)):
            if results[i][0] == title:
                return i + 1
    except ValueError:
        print("That game is not in the list. Please give another title!")


def sort_abc(file_name):
    results = create_list(file_name)
    results = sorted(list(map(lambda x: x[0], results)))
    return results


def get_genres(file_name):
    results = create_list(file_name)
    results = list(map(lambda x: x[3], results))
    results = set(results)
    results = sorted(list(results))
    return results


def when_was_top_sold_fps(file_name):
    results = create_list(file_name)
    results = list(map(lambda x: [x[0], float(x[1]), int(x[2]), x[3], x[4]], results))
    most_games_sold = sorted(results, key=lambda x: x[1], reverse=True)
    for i in range(len(most_games_sold)):
        if most_games_sold[i][3] == 'First-person shooter':
            return most_games_sold[i][2]


def main():
    create_list('game_stat.txt')
    count_games('game_stat.txt')
    decide('game_stat.txt', 2000)
    get_latest('game_stat.txt')
    count_by_genre('game_stat.txt', 'First-person shooter')
    get_line_number_by_title('game_stat.txt', 'EverQuest')
    sort_abc('game_stat.txt')
    get_genres('game_stat.txt')
    when_was_top_sold_fps('game_stat.txt')


main()
