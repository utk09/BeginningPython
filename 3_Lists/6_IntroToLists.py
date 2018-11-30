# Lists are like Arrays. But they can store multiple datatype.
# A single list can  have integer, float, string, long, etc.

# Let us create a list of 'numbers'

numbers_list = [12, 34, 545, 6.89, -4.67, 1, 0, 668899]
alphabet_list = ["apple", "India", "pizza", "Pycharm", "Lion", "Mt. Everest"]
jumbled_list = [23, 3434, "mango", "chocolate", "fries", 8.5950598, 455, "Movies", "Sacred Games"]
print(numbers_list, "\n", alphabet_list, "\n", jumbled_list)
# "\n" is called an escape character.
# It shifts cursor to the next line.

# Let us now learn about Indexing.
# Indexing means to find the value at a particular position.
# Note that Indexing starts counting from 0 instead of 1.
# So first element will be at 0th position instead of first position and so on.

print(numbers_list[3]) # It will give the element at position "3" from "numbers_list"
print(alphabet_list[1:4]) # It will give us the value in range of 1st position to 3rd position.
# Note that range always goes from mth position to (n-1)th position.


