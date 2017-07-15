class Movie():
    def __init__(self, title, movie_story, poster_image_url, trailer_youtube_url):
        """ Initialize the movie instance.
            Arguments:
            title: title of the movie
            movie_story: a short description of the movie.
            poster_image_url:the movie's image url.
            trailer_youtube_url:trailer's youtube video link.
            Returns: None. """
        self.title = title
        self.storyline = movie_story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
