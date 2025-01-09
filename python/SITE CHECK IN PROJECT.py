print("WELCOME TO THE SITE.")
Mission = input("What's your mission? (CONTRACTOR, ARCHITECT, CLIENT): ")

if Mission not in ["CONTRACTOR", "ARCHITECT", "CLIENT"]:
    print("Please leave the buildings!!")
    quit()
else:
    name = input("What's your name? ")
    if len(name) < 1 or len(name) > 30:
        print("Please enter a valid name.")
        quit()  # Added quit() to exit the program if name is invalid.
    address = input("Enter your address: ")
    if len(address) < 1 or len(address) > 30:
        print("Enter a valid address.")
        quit()  # Added quit() to exit the program if address is invalid.

    if Mission == "CLIENT":
        print("Thank you for checking in!")
    else:
        project_name = input("Enter project name: ")
        if len(project_name) < 1 or len(project_name) > 30:
            print("Please enter a valid project name.")
            quit()  # Added quit() to exit the program if project_name is invalid.

        max_trials = 3
        for trial in range(1, max_trials + 1):
            try:
                project_number = int(input("Enter project number: "))
                print(f"Project number is {project_number}")
                break
            except ValueError:
                print("The value you entered is not a number.")
        else:
            print(f"You've exceeded the maximum number of trials ({max_trials}). Exiting program.")
            quit()
