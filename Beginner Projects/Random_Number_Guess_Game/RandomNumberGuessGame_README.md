# 🎮 Random Number Guessing Game

An interactive Python game where players try to guess a randomly generated number between 1 and 100. Get hints after each guess and test your luck and logic!

## 📋 Features

- **Random Number Generation** - Computer picks a number between 1-100
- **Interactive Gameplay** - Real-time feedback on guesses
- **Smart Hints** - Tells if your guess is higher or lower than target
- **Quit Option** - Exit game anytime with 'Q'
- **Win Condition** - Celebrate when you guess correctly
- **Play Again** - Restart for another round

---

## 🎯 How to Play

### Rules
1. Computer randomly picks a number between **1 and 100**
2. You have **unlimited attempts** to guess the number
3. After each guess, you get a hint:
   - ✅ "Congratulation you guess correct!" → You won!
   - ⬆️ "Your guess is greater than actual number" → Guess lower
   - ⬇️ "Your guess is lesser than actual number" → Guess higher
4. Type **'Q'** anytime to quit the game

### Objective
Find the secret number in as few guesses as possible!

---

## 🚀 Installation & Setup

### Requirements
- Python 3.x
- No external dependencies (uses built-in modules only)

### Clone Repository
```bash
git clone https://github.com/yourusername/PythonMiniProjects.git
cd PythonMiniProjects/Beginner_Projects/RandomNumberGuessGame
```

### Run the Game
```bash
python RandomNumberGuessGame.py
```

---

## 📖 How to Use

### Starting the Game
```bash
$ python RandomNumberGuessGame.py
Enter your guess or Quit(Q) : 50
your guess is greater than actual number
Enter your guess or Quit(Q) : 25
your guess is lesser than actual number
Enter your guess or Quit(Q) : 37
your guess is greater than actual number
Enter your guess or Quit(Q) : 31
congratulation you guess correct!
Actual Number was :  31
-------GAMEOVER--------
```

### Example Game Sessions

**Game 1: Lucky Winner**
```
Enter your guess or Quit(Q) : 50
your guess is lesser than actual number
Enter your guess or Quit(Q) : 75
your guess is greater than actual number
Enter your guess or Quit(Q) : 62
congratulation you guess correct!
Actual Number was :  62
-------GAMEOVER--------
```

**Game 2: Quit Early**
```
Enter your guess or Quit(Q) : 50
your guess is greater than actual number
Enter your guess or Quit(Q) : 25
your guess is lesser than actual number
Enter your guess or Quit(Q) : Q
you decided to quit!
-------GAMEOVER--------
```

**Game 3: Unlucky Guess**
```
Enter your guess or Quit(Q) : 1
your guess is lesser than actual number
Enter your guess or Quit(Q) : 100
your guess is greater than actual number
Enter your guess or Quit(Q) : 50
your guess is greater than actual number
Enter your guess or Quit(Q) : 25
your guess is lesser than actual number
Enter your guess or Quit(Q) : 37
your guess is lesser than actual number
Enter your guess or Quit(Q) : 43
congratulation you guess correct!
Actual Number was :  43
-------GAMEOVER--------
```

---

## 💻 Code Explanation

### **Import Statement**
```python
import random
```
Imports Python's built-in random module for number generation.

---

### **Generate Target Number**
```python
target = random.randint(1, 100)
```

- `random.randint(1, 100)` generates random integer from 1 to 100 (inclusive)
- Computer "thinks" of a secret number stored in `target` variable
- Number changes each time you run the game

---

### **Initialize User Guess**
```python
userguess = ()
```

Sets `userguess` to empty tuple initially (this is just to start the while loop).

---

### **Main Game Loop**
```python
while userguess != target:
```

Continues looping until user's guess matches the target number.

---

### **Get User Input**
```python
userguess = input("Enter your guess or Quit(Q) : ")
```

Asks player to enter their guess (returns a string).

---

### **Check for Quit**
```python
if(userguess.upper() == "Q"):
    print("you decided to quit!")
    break
```

- `.upper()` converts input to uppercase
- Allows 'q' or 'Q' to quit
- `break` exits the while loop immediately

---

### **Convert to Integer**
```python
guessNumber = int(userguess)
```

Converts the string input to an integer for comparison with target number.

---

### **Check Guess**
```python
if(guessNumber == target):
    print("congratulation you guess correct!")        
    print("Actual Number was : ", target)
    break
```

If guess matches target:
- Print congratulations message
- Reveal the actual number
- Break out of loop (game ends)

---

### **Provide Hints**
```python
elif(guessNumber > target):
    print("your guess is greater than actual number")
elif(guessNumber < target):    
    print("your guess is lesser than actual number")
```

If guess doesn't match:
- Tell if guess is too high or too low
- Loop repeats for next attempt

---

### **Game Over**
```python
print("-------GAMEOVER--------")
```

Displays after loop ends (either won or quit).

---

## 🎲 Game Statistics

### **Number Range**
```
Range: 1 to 100
Total Possibilities: 100
```

### **Optimal Strategy: Binary Search**
Using binary search (always guess middle), you need at most **7 guesses**:

```
Guesses needed:
1st guess: 50  (eliminates 50 numbers)
2nd guess: 25  (eliminates 25 numbers)
3rd guess: 38  (eliminates 13 numbers)
4th guess: 57  (eliminates 6 numbers)
5th guess: 69  (eliminates 3 numbers)
6th guess: 81  (eliminates 1 number)
7th guess: guaranteed win!
```

### **Probability Analysis**
- **Probability of guessing correctly on 1st try:** 1/100 = 1%
- **Probability of guessing within 5 tries:** ~5%
- **Expected attempts (random guessing):** ~33.5 guesses
- **Expected attempts (optimal strategy):** 3-4 guesses

---

## 🎯 Key Learning Concepts

This project teaches:

✅ **Loops**
- While loops for continuous execution
- Loop control with `break`
- Loop conditions

✅ **Conditionals**
- If-elif-else statements
- Multiple condition checking
- Nested conditions

✅ **User Input**
- `input()` function
- String input handling
- Type conversion with `int()`

✅ **String Methods**
- `.upper()` for case-insensitive comparison
- String operations

✅ **Random Module**
- `random.randint()` function
- Random number generation
- Seeding randomness

✅ **Program Flow**
- Loop iterations
- Break statements
- Variable management

---

## 🧠 Strategies to Win

### **Strategy 1: Binary Search (BEST)**
Always guess the middle number:
```
1. Guess 50
   → If target > 50, guess 75 next
   → If target < 50, guess 25 next
   → If target = 50, you win!
```

**Advantage:** Guaranteed win in maximum 7 guesses

### **Strategy 2: Systematic Linear**
Guess numbers sequentially:
```
1. Guess 1, 2, 3, 4, 5...
→ Will eventually find the number
→ But takes longer (up to 100 guesses)
```

### **Strategy 3: Random Guessing**
Pick random numbers:
```
1. Guess any random number
→ Get feedback
→ Use feedback to guess next
→ Takes 30-50 attempts on average
```

### **Strategy 4: Intuition**
Use gut feeling based on hints:
```
1. Start with 50
2. Pay attention to hints
3. Use pattern recognition
→ Takes 5-15 attempts for experienced players
```

---

## 📁 File Structure

```
RandomNumberGuessGame/
├── RandomNumberGuessGame.py   # Main game script
└── README.md                  # This file
```

---

## 🚀 Enhancements & Ideas

### Short Term
- [ ] Add attempt counter
- [ ] Add difficulty levels (range: 1-50, 1-100, 1-1000)
- [ ] Add score/rating system
- [ ] Add play again feature
- [ ] Add statistics tracking

### Medium Term
- [ ] Add time limit
- [ ] Add hint system (reveal if number is even/odd)
- [ ] Add multiplayer mode
- [ ] Display warm/cold feedback
- [ ] Add leaderboard
- [ ] Create GUI with tkinter

### Advanced
- [ ] Web version with Flask
- [ ] AI opponent mode
- [ ] Different game modes
- [ ] Save game statistics
- [ ] Add achievements/badges
- [ ] Mobile app version

---

## 📝 Enhanced Version Example

Here's how you could improve the script:

```python
import random

def play_game(min_num=1, max_num=100):
    """Play the number guessing game"""
    target = random.randint(min_num, max_num)
    attempts = 0
    
    print(f"I'm thinking of a number between {min_num} and {max_num}")
    
    while True:
        try:
            user_input = input(f"Enter your guess (or 'Q' to quit): ").strip()
            
            if user_input.upper() == 'Q':
                print(f"You quit! The number was {target}")
                break
            
            guess = int(user_input)
            attempts += 1
            
            if guess == target:
                print(f"🎉 You got it right in {attempts} attempts!")
                print(f"The number was: {target}")
                break
            elif guess > target:
                print("❌ Your guess is too high")
            else:
                print("❌ Your guess is too low")
                
        except ValueError:
            print("⚠️ Please enter a valid number")

# Main game loop
if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nPlay again? (Y/N): ").upper()
        if play_again != 'Y':
            print("Thanks for playing!")
            break
```

**Improvements:**
- Attempts counter
- Exception handling
- Play again feature
- Better formatting with emojis
- Function-based design
- Input validation

---

## 🎮 Game Difficulty Customization

### **Easy Mode (1-10)**
```python
target = random.randint(1, 10)
```
- Only 10 possibilities
- Maximum 4 guesses with binary search
- Great for beginners

### **Medium Mode (1-100)**
```python
target = random.randint(1, 100)  # Current
```
- 100 possibilities
- Maximum 7 guesses with binary search
- Standard difficulty

### **Hard Mode (1-1000)**
```python
target = random.randint(1, 1000)
```
- 1000 possibilities
- Maximum 10 guesses with binary search
- Challenging

### **Extreme Mode (1-10000)**
```python
target = random.randint(1, 10000)
```
- 10000 possibilities
- Maximum 14 guesses with binary search
- Very difficult

---

## 🏆 Scoring System Idea

```python
def calculate_score(attempts, target_num=100):
    """Calculate player score"""
    optimal = 7  # Binary search max
    if attempts == 1:
        return 1000  # Perfect!
    elif attempts <= optimal:
        return int(1000 / attempts)
    else:
        return int(500 / attempts)
```

---

## 🐛 Potential Issues & Fixes

### **Issue 1: Invalid Input (non-number)**
**Current:** Crashes with ValueError
**Fix:** Add try-except
```python
try:
    guessNumber = int(userguess)
except ValueError:
    print("Invalid input! Please enter a number.")
    continue
```

### **Issue 2: Numbers Outside Range**
**Current:** Accepts any number
**Fix:** Add validation
```python
if guessNumber < 1 or guessNumber > 100:
    print("Please guess between 1 and 100")
    continue
```

### **Issue 3: No Play Again**
**Current:** Must restart manually
**Fix:** Add outer loop
```python
while True:
    # Game code here
    if play_again != 'Y':
        break
```

---

## 📚 Learning Path

This game teaches:
1. **Beginner** - Loops, conditionals, input/output
2. **Intermediate** - Game logic, user interaction
3. **Advanced** - Algorithms, optimization, refactoring

**Progression:**
```
Random Number Game (Loops, Conditionals)
          ↓
Student Management System (File I/O, CRUD)
          ↓
Task Manager (OOP, Classes)
          ↓
Movie Recommendation (Advanced OOP + Algorithms)
```

---

## 🎓 Related Concepts

This project introduces:
- **Game Theory** - Win conditions, strategies
- **Algorithms** - Binary search strategy
- **User Interface** - Console interaction
- **Logic** - Conditional thinking
- **Math** - Probability, ranges

---

## 💡 Fun Extensions

### **Challenge Ideas**
- [ ] Fastest time to win?
- [ ] Fewest guesses?
- [ ] Guess in exactly 5 attempts?
- [ ] Guess without using hints?

### **Variations**
- [ ] Computer vs Player (both guess each other's number)
- [ ] Multiplayer (pass and play)
- [ ] Reverse game (computer guesses your number)
- [ ] Multiple numbers to guess

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

**Happy Guessing! 🎮**
