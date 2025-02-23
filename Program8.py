# Write a program to add new data item into list using append() method.

#function to display the current list
def display_list(my_list):
    print("Current list:", my_list)

#Initial list of data
data_list = [10, 20, 30, 40, 50]
display_list(data_list)

# Using append() method to add a new data item at the end of the list
new_data = 60
data_list.append(new_data)
display_list(data_list)

# Using insert() method to add a new data item at specific index

new_item = 70
position = 2
data_list.insert(position, new_item)
display_list(data_list)