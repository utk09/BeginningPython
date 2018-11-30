index = 0
fruits = ["apple", "mango", "strawberry", "grapes", "pear", "kiwi", "orange", "banana"]
print(fruits)
print(len(fruits))

while index < len(fruits): # while loop goes on executing until the condition inside it is satisfied
    fruit_new = fruits[index]
    print(index)
    print(fruit_new)
    index = index + 1

# while True:  # this is an infinite loop
#   print("a")
