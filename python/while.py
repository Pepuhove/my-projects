trial = 0
name = input('Enter your name: ')

while name.strip() == "" or name.isdigit():
    print('You did not put your name!')
    name = input('Enter your name: ')
    trial += 1
    if trial == 3:
        import time
        for seconds in range(10, 0, -1):
            print(f'You have {seconds} seconds left.')
            time.sleep(1)
        trial = 0

if trial < 3:
    trial += 1
    print(f'Hello {name}, you made it in {trial} trial(s).')
    print('That\'s awesome!')
