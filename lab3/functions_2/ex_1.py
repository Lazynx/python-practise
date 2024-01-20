def single_movie(one_movie):
    if one_movie.get("imdb") > 5.5:
        return True
    else:
        return False


def sublist(movie_list):
    new_list = []
    for i in movie_list:
        if i.get("imdb") > 5.5:
            new_list.append(i)
    return new_list


def one_category(category, movie_list):
    category_list = []
    for i in movie_list:
        if i.get("category") == category:
            category_list.append(i)
    return category_list


def avg_imdb(movie_list):
    summ = 0
    count = 0
    for i in movie_list:
        summ += i.get("imdb")
        count += 1
    return summ / count


def avg_imdb_for_category(category, movie_list):
    category_list = []
    for i in movie_list:
        if i.get("category") == category:
            category_list.append(i)

    summ = 0
    count = 0
    for i in category_list:
        summ += i.get("imdb")
        count += 1
    return summ / count


movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


print(single_movie(movies[0]))
print(sublist(movies))
print(one_category("Adventure", movies))
print(avg_imdb(movies))
print(avg_imdb_for_category("Romance", movies))
