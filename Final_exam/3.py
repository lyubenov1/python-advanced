def movie_organizer(*args):
    result = {}

    for movie_name, genre in args:
        if genre not in result.keys():
            result[genre] = [movie_name]
        else:
            result[genre].append(movie_name)

    genre_sort = sorted(result.keys(), key=lambda x: (-len(result[x]), x))
    last = ''
    for genre in genre_sort:
        last += f'{genre} - {len(result[genre])}\n'
        for movie_name in sorted(result[genre]):
            last += f'* {movie_name}\n'

    return last

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

