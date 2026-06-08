import random # Importing the random module to generate a random number for the guessing game

def play_guessing_game():
    while True:  # Outer loop: Handles restarting the entire game
        secret_number = random.randint(1, 100)
        attempts = 0
        
        print("=" * 40)
        print("🎯 Welcome to the Number Guessing Game! 🎯")
        print("I am thinking of a number between 1 and 100.")
        print("=" * 40)

        # Inner loop: Handles individual guesses
        while True:
            try:
                guess = int(input("\nEnter your guess: "))
                attempts += 1

                if guess > secret_number:
                    print("📉 Too high! Try a lower number.")
                elif guess < secret_number:
                    print("📈 Too low! Try a higher number.")
                else:
                    print("\n🎉 CONGRATULATIONS! You won!")
                    print(f"🏆 You guessed the secret number {secret_number} in {attempts} attempts.")
                    print("=" * 40)
                    break  # Breaks the inner loop because they guessed correctly
                    
            except ValueError:
                print("❌ Invalid input. Please enter a valid integer.")

        # Ask to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        
        if play_again != 'y' and play_again != 'yes':
            print("\n👋 Thanks for playing! Goodbye.")
            break  # Breaks the outer loop to exit the program entirely

if __name__ == "__main__":
    play_guessing_game()
