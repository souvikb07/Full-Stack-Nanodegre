import media
import fresh_tomatoes
# Contains the details of movie objects
toy_story = media.Movie('Toy Story', 'A story of a boy and his toys come into life',
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar',
                     'A marine on an Alien Planet',
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
avengers_end_game = media.Movie('Avengers Endgame',
                       'This is a Story about the Avengers who saves the earth from Thanos',
                       "https://in.bmscdn.com/iedb/movies/images/website/poster/large/avengers-end-game-et00090482-07-12-2018-06-50-21.jpg",
                       "https://www.youtube.com/watch?v=TcMBFSGVi1c")

# saving the movies in a list
movies = [toy_story, avatar, avengers_end_game]
#calling the fresh_tomatoes function to generate web pages
fresh_tomatoes.open_movies_page(movies)