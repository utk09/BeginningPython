# Lists are like Arrays. But they can store multiple datatype.
# A single list can  have integer, float, string, long, etc.

# Let us create a list of 'numbers'

numbers_list = [12, 34, 545, 6.89, -4.67, 1, 0, 668899]
alphabet_list = ["apple", "India", "pizza", "Pycharm", "Lion", "Mt. Everest"]
jumbled_list = [23, 3434, "mango", "chocolate", "fries", 8.5950598, 455, "Movies", "Sacred Games"]
print(numbers_list, "\n", alphabet_list, "\n", jumbled_list)
print(type(numbers_list))
# "\n" is called an escape character.
# It shifts cursor to the next line.

# Let us now learn about Indexing.
# Indexing means to find the value at a particular position.
# Note that Indexing starts counting from 0 instead of 1.
# So first element will be at 0th position instead of first position and so on.

print(numbers_list[3])  # It will give the element at position "3" from "numbers_list"
print(alphabet_list[1:4])  # It will give us the value in range of 1st position to 3rd position.
# Note that range always goes from mth position to (n-1)th position.

print(jumbled_list[::2])
# In this, since there's no start and end point, it goes from 0th position to end position.
# And '2' means that it'll print elements by jumping over one place.
# Run the program and you'll understand this.

print("Reversed Jumbled List: ", jumbled_list[::-1]) # will reverse the list

print(alphabet_list)
del alphabet_list[2]  # will delete the element at index 2.
print(alphabet_list)
# This also means that lists are mutable. Their values can be changed.
# Mutable Meaning:
# https://www.google.co.in/search?q=mutable+meaning&oq=mutable+m&aqs=chrome.1.69i57j0l5.6600j0j7&sourceid=chrome&ie=UTF-8


# This can also be applied to Strings
aRandomString = "Hey there!I'm a random string"
print(aRandomString[5])  # 5th index
print(aRandomString[2:5])  # 2nd to 4th index [(5-1)th position]
print(aRandomString[4:24:2])  # jumps of 2
# del (aRandomString[5])  # Uncomment this del function
# This will throw an error, meaning it's contents cannot be changed.
# Strings are immutable
print(aRandomString)

print(aRandomString[::-1]) # will reverse the string
