print("WELCOME TO THE SITE.")
Mission = input("What's your mission? (CONTRACTOR, ARCHITECT, CLIENT): ")

if Mission not in ["CONTRACTOR", "ARCHITECT", "CLIENT"]:
    print("Please leave the buildings!!")
    quit()
else:
    name = input("What's your name? ")
    if len(name)< 1 or len(name) >30:
        print(input("Please enter a valid name: "))
    address = input("Enter your address: ")
    if len(address)< 1 or len(address) >30:
        print(input("Enter valid address: "))
if Mission =="CLIENT":
    print("Thank you for checking in!")
else:
    project_name=input("Enter project name: ")
    if len(project_name)< 1 or len(project_name) >30:
        print("Please enter a valid name: ")
    while True:
        max_trials=3
        for trial in range(1,max_trials+1):
            try:
                project_number=int(input("Enter project number: "))
            except ValueError:
                    print("The value you entered is not a number")
            else:
                print(f"project_number is {project_number}")
                break
        print(f"You've exceeded the maximum number of trials ({max_trials}). Exiting program.")
        quit()

    
