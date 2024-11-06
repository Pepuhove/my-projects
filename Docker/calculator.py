def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print("SIMPLE CALCULATOR")

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        while True:
            print("Choose operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            operation_choice = input("Enter the operation number (1-4): ")

            if operation_choice in ['1', '2', '3', '4']:
                break
            else:
                print("Invalid operation choice. Please enter a number from 1 to 4.")

        if operation_choice == '1':
            result = add(num1, num2)
        elif operation_choice == '2':
            result = subtract(num1, num2)
        elif operation_choice == '3':
            result = multiply(num1, num2)
        elif operation_choice == '4':
            result = divide(num1, num2)

        print(f"Result: {result}")
        #break  # Exit the outer loop if the calculation is successful

        answer=print('Do you wanna calculate again? N or Y')
        if answer=='Y':
             num1 = float(input("Enter the first number: "))
             num2 = float(input("Enter the second number: "))
        else:
            break


    except ValueError:
        print("Please enter valid numeric values for the numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError as e:
        print(f"An unexpected error occurred: {e}")
