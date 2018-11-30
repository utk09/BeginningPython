# Let us check some list methods now.

numbers_list = [12, 34, 545, 6.89, -4.67, 1, 0, 668899]
alphabet_list = ["apple", "India", "pizza", "Pycharm", "Lion", "Mt. Everest"]
jumbled_list = [23, 3434, "mango", "chocolate", "fries", 8.5950598, 455, "Movies", "Sacred Games"]
print(numbers_list, "\n", alphabet_list, "\n", jumbled_list)

numbers_list.append(781)  # It adds the value at the end of the list.
print(numbers_list)

numbers_list = numbers_list + [69]  # another way to append
print(numbers_list)

alphabet_list.pop(3)  # removes the value at "INDEX 3"
print(alphabet_list)


