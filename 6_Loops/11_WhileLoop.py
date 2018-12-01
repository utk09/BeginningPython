index = 0
fruits = ["apple", "mango", "strawberry", "grapes", "pear", "kiwi", "orange", "banana"]
print(fruits)
print(len(fruits))

while index < len(fruits):  # while loop goes on executing until the condition inside it is satisfied
    fruit_new = fruits[index]
    print(index)
    print(fruit_new)
    index = index + 1

# while True:  # Uncomment this, it is an infinite loop
#   print("a")

'''
The "while" loop can execute a set of statements as long as a condition is true.
The "break" statement can stop the loop even if the while condition is true.
The "continue" statement can stop the current iteration, and continue with the next.
'''

###########------------------BONUS------------------###########

print("\n")  # adds new lines

print('''
We take a variable i = 6. Iterate it till it reaches 24.
But then we use "break" if i reaches 17.
You'll see that it comes out of the "while" loop, even though iterations are remaining.
''')
i = 6
while i < 24:
    print(i)
    if i == 17:
        break
    i += 1  # increments "i" till it reaches 17.

print("\n")  # adds new lines

print('''
We take a variable i = 6. Iterate it till it reaches 24.
But then we use "continue" if i reaches 17 and print that i = 17 here.
We then "continue" with remaining iterations.
''')

i = 6
while i < 24:
    i += 1
    if i == 17:
        print("i = 17 here")
        continue
    print(i)
