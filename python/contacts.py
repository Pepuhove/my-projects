contacts = {}

while True:
    try:
        name = input('Enter a name (or type "exit" to stop): ')
        if name.lower() == 'exit':
            break

        number = int(input('Enter a number: '))
        contacts[name] = number
        print('Contact added:', {name: number})

    except ValueError:
        print('Please enter a valid number')

print('All contacts:', contacts)
