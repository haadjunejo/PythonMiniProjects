from recommendationengine import RecommendationEngine

RE = RecommendationEngine()
RE.load_data()
running =True

while running:

    print("-"*25,"Movie Recommendation System","-"*25)
    print("Welcome To MRS")
    print("1. Add Movie")
    print("2. Add User")
    print("3. User Watch & Rate Movie")
    print("4. Recommend by Genre")
    print("5. Recommend Similar")
    print("6. View Top Rated Movies")
    print("7. View User's Watched Movies")
    print("8. Exit (save data)")

    try:
        ans = int(input("Enter Any Number From Above : "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if(ans==1):
        print("-"*25,"Add Movie","-"*25)
        title = input("Enter Movie Title : ")
        genre = input("Enter Movie Genre : ")
        rating = float(input("Enter Movie Rating : "))
        description = input("Enter Movie Description : ")
        RE.add_movie(title,genre,rating,description)
        print("Added Movie Successfully!")

    elif(ans==2):
        print("-"*25,"Add User","-"*25)
        name = input("Enter User Name : ")
        RE.add_user(name)
        print("Added User Successfully!")

    elif(ans==3):
        print("-"*25,"User Watch & Rate Movie","-"*25)
        user_id = int(input("Enter User ID : "))
        movie_id = int(input("Enter Movie ID : "))
        rating = float(input("Enter Movie Rating : "))
        RE.user_watch_and_rate(user_id,movie_id,rating)
        print("Movie Watched And Rated!")

    elif(ans==4):
        print("-"*25,"Recommend by Genre","-"*25)
        user_id = int(input("Enter User ID : "))
        genre = input("Enter Movie Genre : ")
        recomended = RE.recommend_by_genre(user_id,genre)
        print("Recommendation List")
        i=1
        for m in recomended:
            print(f"{i}. {m.get_info()}") 
            i += 1

    
    elif(ans==5):
        print("-"*25,"Recommend Similar","-"*25)
        user_id = int(input("Enter User ID : "))
        movie_id = int(input("Enter Movie ID : "))
        recomended = RE.recommend_similar(user_id,movie_id)
        print("Recommendation List")
        i=1
        for m in recomended:
            print(f"{i}. {m.get_info()}") 
            i += 1

    elif(ans==6):
        print("-"*25,"View Top Rated Movies","-"*25)
        limit = int(input("Enter Number Top Movies To See (default 5)"))
        topmovies = RE.top_rated_movies(limit)
        print("Top Rated Movies List")
        i=1
        for m in topmovies:
            print(f"{i}. {m.get_info()}") 
            i += 1

    elif(ans==7):
        print("-"*25,"View User's Watched Movies","-"*25)
        user_id = int(input("Enter User ID : "))
        u = RE.find_user(user_id)
        if u:
            print(f"Movies watched by {u.user_name}:")
            if len(u.get_watched_movies()) == 0:
                print("  No movies watched yet!")
            else:
                for movie_id in u.get_watched_movies():
                    m = RE.find_movie(movie_id)
                    if m:
                        rating = u.ratings.get(movie_id, "Not rated")  # ← Use .get() instead
                        print(f"  - {m.title} (Rating: {rating})")
        else:
            print("User not found!") 
    elif(ans==8):             
        print("-"*25,"Saving and Exiting!","-"*25)
        RE.save_to_file()
        running = False

print("-"*25,"Thank You For Using MRS!","-"*25)