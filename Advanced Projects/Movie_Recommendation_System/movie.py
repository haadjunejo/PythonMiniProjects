class Movie:

    def __init__(self,movie_id,title,genre,rating,description):
        self.movie_id=movie_id
        self.title=title
        self.genre=genre
        self.rating=rating
        self.description=description

    def get_info(self):
        return f"ID: {self.movie_id} | Title: {self.title} | Genre: {self.genre} | Rating: {self.rating} | Description: {self.description}"

    def update_rating(self,newRating):
        self.rating=newRating    