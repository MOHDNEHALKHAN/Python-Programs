# Write a program to implement exception handling for zero division & value error

try :
    num = int(input("Enter a number: "))
    result = 10/num
    print("Result: ", result)
except ZeroDivisionError:
        print("Division by zero is not allowed")

except ValueError:
            print("Invalid input")