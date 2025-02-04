def is_imdb_above_5_5(movie):
    return movie["imdb"] > 5.5

def filter_movies_above_5_5(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]

def compute_average_imdb(movies):
    total_imdb = sum(movie["imdb"] for movie in movies)
    return total_imdb / len(movies) if len(movies) > 0 else 0

def compute_average_imdb_by_category(movies, category):
    filtered_movies = get_movies_by_category(movies, category)
    return compute_average_imdb(filtered_movies)

print(is_imdb_above_5_5(movies[0]))  
# Output: True

print(filter_movies_above_5_5(movies))  
# Output: [{'name': 'Usual Suspects', 'imdb': 7.0, 'category': 'Thriller'}, 
#          {'name': 'Hitman', 'imdb': 6.3, 'category': 'Action'}, 
#          {'name': 'Dark Knight', 'imdb': 9.0, 'category': 'Adventure'}, 
#          {'name': 'The Help', 'imdb': 8.0, 'category': 'Drama'}, 
#          {'name': 'The Choice', 'imdb': 6.2, 'category': 'Romance'}, 
#          {'name': 'Colonia', 'imdb': 7.4, 'category': 'Romance'}, 
#          {'name': 'Love', 'imdb': 6.0, 'category': 'Romance'}, 
#          {'name': 'Joking muck', 'imdb': 7.2, 'category': 'Comedy'}, 
#          {'name': 'What is the name', 'imdb': 9.2, 'category': 'Suspense'}, 
#          {'name': 'Detective', 'imdb': 7.0, 'category': 'Suspense'}, 
#          {'name': 'We Two', 'imdb': 7.2, 'category': 'Romance'}]

print(get_movies_by_category(movies, "Romance"))  
# Output: [{'name': 'The Choice', 'imdb': 6.2, 'category': 'Romance'},
#          {'name': 'Colonia', 'imdb': 7.4, 'category': 'Romance'},
#          {'name': 'Love', 'imdb': 6.0, 'category': 'Romance'},
#          {'name': 'Bride Wars', 'imdb': 5.4, 'category': 'Romance'},
#          {'name': 'We Two', 'imdb': 7.2, 'category': 'Romance'}]

print(compute_average_imdb(movies))  
# Output: 6.6

print(compute_average_imdb_by_category(movies, "Romance"))  
# Output: 6.64
