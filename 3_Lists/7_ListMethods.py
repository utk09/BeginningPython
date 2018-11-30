# Let us check some list methods now.

numbers_list = [12, 34, 545, 6.89, -4.67, 1, 0, 668899, 7432]
alphabet_list = ["apple", "India", "pizza", "Pycharm", "Lion", "Mt. Everest"]
jumbled_list = [23, 3434, "mango", "chocolate", "fries", 8.5950598, 455, "Movies", "Sacred Games"]
print(numbers_list, "\n", alphabet_list, "\n", jumbled_list)

numbers_list.append(781)  # It adds the value at the end of the list.
print(numbers_list)

numbers_list = numbers_list + [69, 9.81]  # another way to append
print(numbers_list)

alphabet_list.pop(3)  # removes the value at "INDEX 3"
print(alphabet_list)

print(jumbled_list)
anIndex = jumbled_list.index("chocolate") # Index checks the value of particular term given to it.
print("Index of chocolate: ",anIndex)
del jumbled_list[anIndex] # delete the value at "anIndex" variable
print(jumbled_list)

# anotherIndex = jumbled_list.index("pizza") # uncomment, will return value error, if not present
# print(anotherIndex)

print(alphabet_list+jumbled_list+numbers_list) # addition of lists

print(numbers_list)
numbers_list.remove(668899) # removes the given value from the list
print(numbers_list)

# More List Methods: https://docs.python.org/3/tutorial/datastructures.html
