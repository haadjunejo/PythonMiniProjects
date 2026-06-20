# 🎬 Movie Recommendation System

A Python-based movie recommendation engine with object-oriented design that suggests movies based on genres and user preferences.

## 📋 Features

- **Add Movies** - Store movies with title, genre, rating, and description
- **Add Users** - Create user profiles to track viewing history
- **Watch & Rate** - Users can watch movies and provide ratings
- **Genre-Based Recommendations** - Get movie suggestions based on preferred genre
- **Similar Recommendations** - Find movies similar to ones you've already watched
- **Top Rated Movies** - View the highest-rated movies in the system
- **Data Persistence** - Save and load user/movie data using JSON files
- **Error Handling** - Robust input validation and exception handling

---

## 🏗️ Project Architecture

### Classes

#### **Movie**
Represents a single movie in the system.

**Attributes:**
- `movie_id` - Unique identifier
- `title` - Movie name
- `genre` - Movie category (Sci-Fi, Action, Drama, etc.)
- `rating` - Average rating (1-10)
- `description` - Brief movie description

**Methods:**
- `get_info()` - Returns formatted movie details
- `update_rating(new_rating)` - Updates the movie rating

```python
movie = Movie(1, "Inception", "Sci-Fi", 9, "Mind-bending thriller")
```

---

#### **User**
Represents a user profile with viewing history and ratings.

**Attributes:**
- `user_id` - Unique identifier
- `user_name` - User's name
- `watched_movies` - List of movie IDs watched
- `ratings` - Dictionary of movie ratings (movie_id → rating)

**Methods:**
- `watch_movie(movie_id)` - Add movie to watched list
- `rate_movie(movie_id, rating)` - Rate a movie
- `get_watched_movies()` - Get list of watched movie IDs
- `get_ratings()` - Get all ratings
- `has_watched(movie_id)` - Check if user watched a movie

```python
user = User(1, "Ali")
user.watch_movie(1)
user.rate_movie(1, 9)
```

---

#### **RecommendationEngine**
Core engine that manages movies, users, and recommendations.

**Attributes:**
- `movies` - List of Movie objects
- `users` - List of User objects
- `movie_id` - Counter for movie IDs
- `user_id` - Counter for user IDs

**Key Methods:**

| Method | Purpose |
|--------|---------|
| `add_movie()` | Add new movie to system |
| `add_user()` | Add new user to system |
| `find_movie(movie_id)` | Retrieve movie by ID |
| `find_user(user_id)` | Retrieve user by ID |
| `user_watch_and_rate()` | User watches and rates a movie |
| `recommend_by_genre()` | Get recommendations by genre |
| `recommend_similar()` | Get recommendations similar to a movie |
| `top_rated_movies()` | Get top-rated movies |
| `save_to_file()` | Save data to JSON files |
| `load_data()` | Load data from JSON files |

---

## 🚀 Installation & Setup

### Requirements
- Python 3.7+
- No external dependencies (uses built-in libraries)

### Clone Repository
```bash
git clone https://github.com/yourusername/PythonMiniProjects.git
cd PythonMiniProjects/Movie_Recommendation_System
```

### Run the Application
```bash
python main.py
```

---

## 📖 How to Use

### Main Menu Options

```
======================== Movie Recommendation System ========================
Welcome To MRS
1. Add Movie
2. Add User
3. User Watch & Rate Movie
4. Recommend by Genre
5. Recommend Similar
6. View Top Rated Movies
7. View User's Watched Movies
8. Exit (save data)
```

### Example Usage Flow

#### Step 1: Add Movies
```
Option: 1
Enter Movie Title: Inception
Enter Movie Genre: Sci-Fi
Enter Movie Rating: 9
Enter Movie Description: Mind-bending thriller about dreams
✓ Added Movie Successfully!
```

#### Step 2: Add Users
```
Option: 2
Enter User Name: Ali
✓ Added User Successfully!
```

#### Step 3: User Watches & Rates
```
Option: 3
Enter User ID: 1
Enter Movie ID: 1
Enter Movie Rating: 9
✓ Movie Watched And Rated!
```

#### Step 4: Get Recommendations by Genre
```
Option: 4
Enter User ID: 1
Enter Movie Genre: Sci-Fi
Recommendation List:
1. Interstellar (Rating: 8)
2. Avatar (Rating: 8)
```

#### Step 5: Exit & Save
```
Option: 8
✓ Data saved to movies.json and users.json
```

---

## 💾 Data Storage

The system uses two JSON files for data persistence:

### `movies.json`
Stores all movies in the system:
```json
[
    {
        "movie_id": 1,
        "title": "Inception",
        "genre": "Sci-Fi",
        "rating": 9,
        "description": "Mind-bending thriller about dreams within dreams"
    },
    {
        "movie_id": 2,
        "title": "The Dark Knight",
        "genre": "Action",
        "rating": 9,
        "description": "Batman faces the Joker in Gotham City"
    }
]
```

### `users.json`
Stores user profiles with viewing history:
```json
[
    {
        "user_id": 1,
        "user_name": "Ali",
        "watched_movies": [1, 2],
        "ratings": {
            "1": 9,
            "2": 8
        }
    }
]
```

---

## 🎯 Key Learning Concepts

This project demonstrates:

✅ **Object-Oriented Programming**
- Class design and encapsulation
- Methods and attributes
- Inheritance concepts

✅ **Data Structures**
- Lists and dictionaries
- List comprehensions
- Lambda functions for sorting

✅ **File I/O**
- JSON serialization/deserialization
- File reading and writing
- Error handling

✅ **Algorithm Basics**
- Filtering and searching
- Sorting by criteria
- Pattern matching (similar recommendations)

✅ **Error Handling**
- Try-except blocks
- Input validation
- Exception handling

---

## 📊 Sample Data

Add these 10 movies to test the system:

| ID | Title | Genre | Rating |
|----|-------|-------|--------|
| 1 | Inception | Sci-Fi | 9 |
| 2 | The Dark Knight | Action | 9 |
| 3 | Forrest Gump | Drama | 8 |
| 4 | The Shawshank Redemption | Drama | 9 |
| 5 | Interstellar | Sci-Fi | 8 |
| 6 | Pulp Fiction | Action | 8 |
| 7 | The Notebook | Romance | 7 |
| 8 | Joker | Drama | 8 |
| 9 | Avatar | Sci-Fi | 8 |
| 10 | The Avengers | Action | 8 |

---

## 🔄 Workflow

```
START
  ↓
Load existing data (movies.json, users.json)
  ↓
Main Menu Loop
  ├─ Add Movies
  ├─ Add Users
  ├─ User Watch & Rate
  ├─ Get Recommendations
  ├─ View Top Rated
  └─ Exit
  ↓
Save data to JSON files
  ↓
END
```

---

## 🐛 Error Handling

The system handles:
- ✓ Invalid menu input (non-integer)
- ✓ User not found errors
- ✓ Movie not found errors
- ✓ Missing JSON files (first run)
- ✓ Corrupted JSON data
- ✓ Empty recommendations list

---

## 📁 File Structure

```
Movie_Recommendation_System/
├── main.py                    # Main program with menu loop
├── movie.py                   # Movie class
├── user.py                    # User class
├── recommendationengine.py    # RecommendationEngine class
├── movies.json                # Saved movies data
├── users.json                 # Saved users data
└── README.md                  # This file
```

---

## 🚀 Future Enhancements

- [ ] Add review/comment system for movies
- [ ] Implement collaborative filtering for better recommendations
- [ ] Add movie search functionality
- [ ] Create a web GUI using Flask/Django
- [ ] Add user authentication
- [ ] Integration with real movie APIs (TMDB, OMDb)
- [ ] Add movie popularity tracking
- [ ] Implement rating history/timeline

---

## 📚 Learning Path

**After mastering this project, move to:**
1. **Weather App** - Learn API integration
2. **Data Analysis Project** - Learn pandas & data visualization
3. **Machine Learning** - Use these OOP skills with scikit-learn

---

## 💡 Key Takeaways

- Understanding OOP design patterns
- Building recommendation algorithms
- JSON data persistence
- User input validation
- List/dictionary operations
- Sorting and filtering algorithms

---

## 👨‍💻 Author

Muhammad Haad

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Feel free to fork and submit pull requests for improvements!

---

**Happy Coding! 🚀**
