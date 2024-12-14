"""
This script demonstrates basic Python functionality, including:
- Greeting a user with a personalized message.
- Calculating the sum of two numbers provided by the user.
- Finding the maximum value from a list of numbers provided by the user.

The script guides the user through input prompts and provides appropriate feedback and error handling.
"""
"import packages
import random

"great the user
def greet_user(name):
    """Greet the user with a personalized message."""
    greetings = ["Hello", "Hi", "Hey", "Welcome", "Greetings"]
    greeting = random.choice(greetings)
    return f"{greeting}, {name}!"

def calculate_sum(a, b):
    """Return the sum of two numbers."""
    return a + b

def find_max(numbers):
    """Return the maximum number from a list of numbers."""
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    return max(numbers)

def main():
    """Main function to demonstrate the functionality of the script."""
    user_name = input("What's your name? ")
    print(greet_user(user_name))
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {calculate_sum(num1, num2)}.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    try:
        numbers = [float(num) for num in numbers]
        print(f"The maximum number in the list is {find_max(numbers)}.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
