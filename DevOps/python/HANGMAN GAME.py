word_list=['ardvark','baboon','camel']
lives=6
import random

chosen_word=random.choice(word_list)

guess=input('Guess a letter: ').lower()
word_length=len(chosen_word)
display=[]
for _ in range(word_length):
    display+='_'
print(display)
guess=input('Guess a letter: ').lower()
for position in range(word_length):
    letter = chosen_word[position]
    if   letter==guess:
        display[position]=letter

print(display)
print(chosen_word)
end_of_game=False
while not end_of_game:
    guess=input('Guess a letter: ').lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter==guess:
            display[position]=letter
        print(display)

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print('you loss')


    if not '_' in display:
        end_of_game=True
    print('won')





