import random

score = 0
player = []

while score < 4:
    try:
        user_choice = int(input('Type 0 for rock, 1 for paper, 2 for scissors\n'))
        computer_choice = random.randint(0, 2)
        print(f'Computer chose: {computer_choice}')

        if user_choice < 0 or user_choice > 2:
            print('You entered a wrong selection!')
            user_choice = int(input('Type 0 for rock, 1 for paper, 2 for scissors\n'))
        elif (user_choice == 0 and computer_choice == 2) or \
                (user_choice == 1 and computer_choice == 0) or \
                (user_choice == 2 and computer_choice == 1):
            print('You win!')
            score += 1
        elif user_choice == computer_choice:
            print("It's a tie!")
        else:
            print('Computer wins!')

        # Update the player's choices
        player.append((user_choice, computer_choice))

    except ValueError:
        print('Please enter a valid number!')
        continue
    except KeyboardInterrupt:
        print('\nGame interrupted. Thanks for playing!')
        break

    # Determine the winner
    user_wins = sum(1 for user, computer in player if (user == 0 and computer == 2) or \
                    (user == 1 and computer == 0) or (user == 2 and computer == 1))
    computer_wins = len(player) - user_wins

    # Declare the winner
    if user_wins > computer_wins:
        print('CONGRATULATIONS!! You are the winner!')
    elif user_wins < computer_wins:
        print('Computer is the winner!')
    else:
        print('It\'s a tie!')

    print(f'Total Rounds: {len(player)}')
    # Ask if the user wants to play again
    play_again = input('Do you want to play again? (YES/NO): ')

    if play_again.upper() in {'YES', 'Y'}:
        # Reset the score and player choices for a new game
        score = 0
        player = []
        user_choice = int(input('Type 0 for rock, 1 for paper, 2 for scissors\n'))
    elif play_again.upper() in {'NO', 'N'}:
        print('Thank you for playing!')
    else:
        break
