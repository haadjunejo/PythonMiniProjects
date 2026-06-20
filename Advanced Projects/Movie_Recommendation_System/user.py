class User:

    def __init__(self,user_id,user_name):
        self.user_id=user_id
        self.user_name=user_name
        self.watched_movies=[]
        self.ratings={}

    def watch_movie(self,movie_id):
        self.watched_movies.append(movie_id)

    def rate_movie(self,movie_id,rating):
        self.ratings[movie_id]=rating

    def get_watched_movies(self):
        return self.watched_movies

    def get_ratings(self):
        return self.ratings            

    def has_watched(self, movie_id):
        return movie_id in self.watched_movies