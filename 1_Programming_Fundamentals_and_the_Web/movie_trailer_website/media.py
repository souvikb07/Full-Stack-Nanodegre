class Movie():
    """
    A class used to represent a Movie

    ...

    Attributes
    ----------
    title : str
        a formatted string which says the name of the movie
    storyline : str
        a formatted string which says the storyline of the movie
     : str
        the sound that the animal makes
    poster_image_url : str
        a formatted string contains the link of the movie poster
    trailer_youtube_url: str
        a formatted string contains the link of the movie trailer

    """
    def __init__(self, movie_title, movie_story_line, poster_image, trailer_youtube_link):
        """
        Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    movie_title : str
        The Name of the Movie
    movie_story_line : str
        The story line of the movie
    poster_image : str
        Link of the movie's poster image

    trailer_youtube_link: str
        Link of the trailer from youtube

    Returns
    -------
    Movie Page
        Gives Name of the movie
        Gives story line of the movie
        Show the Poster of the movie
        Show the trailer of the movie
        """
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_link