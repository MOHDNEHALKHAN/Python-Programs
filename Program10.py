# Write a python program for creating user defined exception & raise it when input no. is negative.

class NegativeNumberError(Exception):
    def __init__(self, message="Input no. cannot be negative"):
        self.message = message
        super().__init__(self.message)

def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError()
    else:
        print(f"The number {number} is positive")

def main():
    try:
        userinput = int(input("Enter a number: "))
        check_positive_number(userinput)
    except NegativeNumberError as ne:
        print("Error: ", ne)
    except ValueError:
        print("Please enter a valid number")
    else:
        print("No exception raised")

if __name__ == "__main__":
    main()