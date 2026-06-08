# 🎯 Number Guessing Game (Simple CLI)

A fun command-line **Number Guessing Game** built with Python. The computer randomly chooses a number between **1 and 100** and you have to guess it. The game gives hints like **too high** or **too low** and tracks the number of attempts.

---

## ✨ Features
- Random secret number between **1 and 100**
- Feedback after every guess: **Too High / Too Low**
- Handles invalid input (non-integer guesses)
- Keeps playing until you decide to stop

---

## 🧰 Requirements
- Python 3.6+ (uses only the standard library)

---

## ▶️ How to Run
From the project folder:

```bash
python "projects/Number_Guessing_Game.py"
```

---

## 🕹️ How to Play
1. Start the program
2. Type your guess (an integer)
3. Read the hint:
   - 📉 Too high — guess lower
   - 📈 Too low — guess higher
4. Keep guessing until you find the secret number
5. Enter `y` to play again or `n` to exit

---

## 📌 Example Gameplay
```
🎯 Welcome to the Number Guessing Game! 🎯
I am thinking of a number between 1 and 100.

Enter your guess: 50
📉 Too high! Try a lower number.

Enter your guess: 25
📈 Too low! Try a higher number.

Enter your guess: 30
🎉 CONGRATULATIONS! You won!
🏆 You guessed the secret number 30 in 3 attempts.
```

---


