import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story', 'A story of a boy and his toys come into life',
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')
#print(toy_story.storyline)
avatar = media.Movie('Avatar',
                     'A marine on an Alien Planet',
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)