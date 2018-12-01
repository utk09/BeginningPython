index = 0
fruits = ["apple", "mango", "strawberry", "grapes", "pear", "kiwi", "orange", "banana"]
print(fruits)
print(len(fruits))

while index < len(fruits): # while loop goes on executing until the condition inside it is satisfied
    fruit_new = fruits[index]
    print(index)
    print(fruit_new)
    index = index + 1

# while True:  # Uncomment this, it is an infinite loop
#   print("a")

'''
The "while" loop can execute a set of statements as long as a condition is true.
The "break" statement can stop the loop even if the while condition is true.
The continue statement can stop the current iteration, and continue with the next.
'''
