import json
from movie import Movie
from user import User

class RecommendationEngine:

    def __init__(self):
        self.movies=[]
        self.users=[]
        self.movie_id=1
        self.user_id=1


    def add_movie(self,title,genre,rating,description):
        movie = Movie(self.movie_id,title,genre,rating,description)
        self.movies.append(movie)
        self.movie_id+=1

    def add_user(self,name):
        user = User(self.user_id,name)
        self.users.append(user)
        self.user_id+=1

    def find_movie(self,movie_id):

        for m in self.movies:
            if(m.movie_id==movie_id):
                return m
        else:
            return None

    def find_user(self,user_id):

        for u in self.users:
            if(u.user_id==user_id):
                return u
        else:
            return None        

    def user_watch_and_rate(self,user_id, movie_id, rating):

        u = self.find_user(user_id)  
        m = self.find_movie(movie_id)  
        u.watch_movie(movie_id)
        u.rate_movie(movie_id, rating)
    
    def recommend_by_genre(self,user_id, genre):

        u = self.find_user(user_id) 
        recommended = [m for m in self.movies 
                   if m.genre == genre and m.movie_id not in u.watched_movies]
        recommended.sort(key=lambda m: m.rating, reverse=True)

        return recommended[:5]
    
    def recommend_similar(self,user_id, movie_id):

        u = self.find_user(user_id)  
        m = self.find_movie(movie_id)
        recommended = [movie for movie in self.movies 
                   if movie.genre == m.genre and movie.movie_id not in u.watched_movies]
        recommended.sort(key=lambda movie: movie.rating, reverse=True)
    
        return recommended[:5]

    def top_rated_movies(self,limit=5):
        sorted_movies = sorted(self.movies, key=lambda m: m.rating, reverse=True)
        return sorted_movies[:limit]

    def save_to_file(self):
        movie_dict = [m.__dict__ for m in self.movies]
        users_data =[]
        for u in self.users:
            user_dict = {
                'user_id': u.user_id,
                'user_name': u.user_name,
                'watched_movies': u.watched_movies,
                'ratings': u.ratings
            }
            users_data.append(user_dict)

        with open("movies.json","w") as f:
            json.dump(movie_dict,f,indent=4)

        with open("users.json","w") as f: 
            json.dump(users_data,f,indent=4)

    def load_data(self):

        try:
            with open("movies.json","r") as f:
                data = json.load(f)

                for m in data:
                    movie = Movie(m["movie_id"], m["title"], m["genre"], m["rating"], m["description"])
                    self.movies.append(movie)
                
            with open("users.json","r") as f:
                data = json.load(f)

                for u in data:
                    user = User(u["user_id"], u["user_name"])
                    user.watched_movies = u["watched_movies"]
                    user.ratings = u["ratings"]
                    self.users.append(user)

            if self.movies:
                self.movie_id = max(m.movie_id for m in self.movies) + 1
            if self.users:
                self.user_id = max(u.user_id for u in self.users) + 1      

        except (FileNotFoundError, json.JSONDecodeError):
            print("No previous data found. Starting fresh!")               


