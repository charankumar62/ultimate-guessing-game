import random
import time

def welcome_message():
    print("\n🎯 Hey there! Welcome to the Ultimate Number Guessing Game!")
    time.sleep(1)
    print("🤖 I’ve just thought of a secret number between 1 and 100.")
    time.sleep(1)
    print("🧠 Let’s see if you can guess it in as few tries as possible. Good luck!\n")

def get_user_guess():
    while True:
        try:
            guess = int(input("👉 Go ahead, enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("⚠️ Whoops! Remember, it’s gotta be between 1 and 100.\n")
        except ValueError:
            print("😅 Hmm, that doesn’t look like a number. Try again!\n")

def give_feedback(guess, target):
    if guess < target:
        print("📉 Nope, too low! Try a bigger number.\n")
    elif guess > target:
        print("📈 Nope, too high! Try a smaller number.\n")

def play_game():
    welcome_message()
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess == secret_number:
            score = max(0, 100 - attempts * 10)
            print(f"\n🎉 Wow! You nailed it! The number was {secret_number}.")
            print(f"🔥 It took you {attempts} tries — your score: {score} points!\n")
            break
        else:
            give_feedback(guess, secret_number)

    print("🙏 Thanks for playing! Hope you had fun!")
    again = input("🔄 Wanna give it another shot? (y/n): ").strip().lower()
    if again == 'y':
        print("\n👍 Alright, here we go again!")
        play_game()
    else:
        print("\n👋 Catch you later! Stay awesome!")

if __name__ == "__main__":
    play_game()
