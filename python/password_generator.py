# Welcome message
print("WELCOME TO PASSWORD GENERATOR!!")

# Importing random
import random

while True:
    try:
        # Get the number of letters, numbers, and symbols for the password
        num_letters = int(input('How many letters do you want?\n'))
        nums = int(input('How many numbers do you want?\n'))
        num_symbols = int(input('How many symbols do you want?\n'))

        # Define character sets for letters, numbers, and symbols
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        symbols = ['+', '*', '&', '#', '@', '^', '%','!','?']

        # Initialize an empty list to store the password
        password = []

        # Generate the required number of letters, numbers, and symbols
        for _ in range(num_letters):
            password.append(random.choice(letters))

        for _ in range(nums):
            password.append(random.choice(numbers))

        for _ in range(num_symbols):
            password.append(random.choice(symbols))

        # Shuffle the password to add randomness
        random.shuffle(password)

        # Join the characters to form the final password
        generated_password = ''.join(password)

        # Display the generated password
        print('Your password is {}'.format(generated_password))
        break  # Exit the loop if the password is generated successfully

    # Handle the case where the user enters non-numeric values
    except ValueError:
        print('Please enter valid numeric values for the password length.')

    # Handle unexpected errors
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
