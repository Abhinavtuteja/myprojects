import json

#
# def handle():
#     filepath = "/Users/naehas/PycharmProjects/Movie_Imdb/Movie_Imdb/imdb.json"
#     with open(filepath, 'r') as f:
#         raw_data = f.read()
#         data = json.loads(raw_data)
#         k = {}
#         for movie_item in data:
#             print(movie_item)
#             k['name'] = movie_item.get('name')
#             k['popularity'] = movie_item.get('99popularity')
#             k['director'] = movie_item.get('director')
#             k['imdb_score'] = movie_item.get('imdb_score')
#         movie, created = Movie.objects.get_or_create(**k)
#         genre_list = movie_item.get('genre')
#         # create genre for each genre in list and attach to current movie
#         for name in genre_list:
#             name = name.strip()
#             genre, created = Genre.objects.get_or_create(name=name)
#             movie.genre.add(genre)
#         movie.save()
#         print(movie)
