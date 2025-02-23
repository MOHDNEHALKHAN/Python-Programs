# Write a program to add and delete key-value pairs in a dictionary. in different ways.

# function to display the current dictionary

def display(dict):
    print("The current dictionary is: ", dict)

#initial dictionary
dict = {'Name': 'John', 'Age': 25, 'city': 'New York'}
display(dict)

# Adding a key-value pair to the dictionary

dict['Occupation'] = 'Engineer'
display(dict)

# Adding a key-value pair to the dictionary using update() method

new_dict = {
    'Hobby': 'Reading', 
    'Salary': 50000
}
dict.update(new_dict)
display(dict)

# Deleting a key-value pair from the dictionary using del keyword

if 'Age' in dict:
    del dict['Age']