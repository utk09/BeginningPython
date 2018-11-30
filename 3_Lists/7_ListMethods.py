# Let us check some list methods now.

numbers_list = [12, 34, 545, 6.89, -4.67, 1, 0, 668899, 7432]
word_list = ["apple", "India", "pizza", "Pycharm", "Lion", "Mt. Everest"]
jumbled_list = [23, 3434, "mango", "chocolate", "fries", 8.5950598, 455, "Movies", "Sacred Games"]
print(numbers_list, "\n", word_list, "\n", jumbled_list)

numbers_list.append(781)  # It adds the value at the end of the list.
print(numbers_list)

numbers_list = numbers_list + [69, 9.81]  # another way to append
print(numbers_list)

word_list.pop(3)  # removes the value at "INDEX 3"
print(word_list)

print(jumbled_list)
anIndex = jumbled_list.index("chocolate")  # Index checks the value of particular term given to it.
print("Index of chocolate: ", anIndex)
del jumbled_list[anIndex]  # delete the value at "anIndex" variable
print(jumbled_list)

# anotherIndex = jumbled_list.index("pizza") # uncomment, will return value error, if not present
# print(anotherIndex)

all_list = word_list + jumbled_list + numbers_list
print("Combined lists: ", all_list)  # addition of lists

print(numbers_list)
numbers_list.remove(668899)  # removes the given value from the list
print(numbers_list)

numbers_list.sort()
print("Sorted Number List: ", numbers_list)

word_list.sort()
print("Sorted Alphabet List: ", word_list)

# jumbled_list.sort() # Uncomment this and run, will throw an error because data types are dissimilar
# print(jumbled_list)

print(all_list)
all_list.insert(4, "maltova")  # inserts element at the specified index
print(all_list)

# Let us start fresh
new_list1 = [2, 3, 4, 9, 7, 0]
new_list2 = ['a', 'b', 'c', 'd', 'z', 'x']
new_string='ror:shach'

new_list1.sort() # sorts in ascending order
print(new_list1)

new_list1.reverse() # reverses the list
print(new_list1)

new_list2 = "".join(new_list2) # joins all the elements of the list
print(new_list2)

new_list2 = "*".join(new_list2) # joins all the elements with a specifier between them
print(new_list2)

print(new_string.split(':')) # splits at specified classifier

# More List Methods: https://docs.python.org/3/tutorial/datastructures.html,
# http://effbot.org/zone/python-list.htm
