print('WELCOME TO THE ROCK, PAPER, SCISSORS GAME!!')

import random

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")

        try:
            user_choice = int(input("Enter your choice (1-3): "))
            if 1 < user_choice > 3:
                print("That's a wrong selection!")
                user_choice = input("Enter your choice (1-3): ")

            choices = ["rock", "paper", "scissors"]
            user_choice = choices[int(user_choice) - 1]
            computer_choice = random.choice(choices)

            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")

            result = get_winner(user_choice, computer_choice)
            print(result)

            if "win" in result:
                user_score += 1
            elif "lose" in result:
                computer_score += 1

            print(f"Score - You: {user_score}, Computer: {computer_score}")

            if user_score == 4:
                print("Congratulations! You've won 4 times. You are the overall winner!")
                break

        except ValueError:
            print('Invalid input. Please enter a number between 1 and 3.')

        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.upper() != 'Y':
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    play_game()
