import math
from collections import Counter


def create_list(file_name):
    results = []
    with open(file_name) as inputfile:
        for line in inputfile:
            results.append(line.strip().split("\t"))
        results = list(map(lambda x: [x[0], float(x[1]), int(x[2]), x[3], x[4]], results))
        return results


def get_copies_sold_list(file_name):
    results = create_list(file_name)
    copies_sold_list = list(map(lambda x: x[1], results))
    return copies_sold_list


def get_most_played(file_name):
    results = create_list(file_name)
    most_played = max(results, key=lambda x: x[1])
    most_played_title = most_played[0]
    return most_played_title


def sum_sold(file_name):
    copies_sold_list = get_copies_sold_list(file_name)
    total_sold = sum(copies_sold_list)
    return total_sold


def get_selling_avg(file_name):
    copies_sold_list = get_copies_sold_list(file_name)
    avg_sold = sum(copies_sold_list) / len(copies_sold_list)
    return avg_sold


def count_longest_title(file_name):
    results = create_list(file_name)
    length_list = []
    title_list = list(map(lambda x: x[0], results))
    for i in range(len(title_list)):
        length_list.append(len(title_list[i]))
    longest_title = max(length_list)
    return longest_title


def get_date_avg(file_name):
    results = create_list(file_name)
    list_of_years = list(map(lambda x: x[2], results))
    avg_year = math.ceil(sum(list_of_years) / len(list_of_years))
    return avg_year


def get_game(file_name, title):
    results = create_list(file_name)
    for i in range(len(results)):
        if results[i][0] == title:
            return results[i]


def count_grouped_by_genre(file_name):
    results = create_list(file_name)
    list_of_genres = list(map(lambda x: x[3], results))
    genre_counter = dict(Counter(list_of_genres))
    return genre_counter


def get_date_ordered(file_name):
    results = create_list(file_name)
    results.sort(key=lambda x: x[0])
    results.sort(key=lambda x: x[2], reverse=True)
    list_of_titles = list(map(lambda x: x[0], results))
    return list_of_titles
