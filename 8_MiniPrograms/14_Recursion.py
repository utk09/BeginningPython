# We will find the sequence of Fibonacci Numbers using recursion.
# Recursive function is a function that calls itself, sort of like loop.
# Recursion works like loop but sometimes it makes more sense to use recursion than loop.
# You can convert any loop to recursion. ... Recursive function is called by some external code.
# If the base condition is met then the program do something meaningful and exits.


# Let us use recursion to find fibonacci numbers.
# Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, 21....
def fibonacci(n):
    if n == 0 or n == 1:  # this is the base condition -- it is the index value of the above sequence.
        return n  # so, if user wants fibonacci number at index 0, it'll return 0 and if at index 1, it'll return 1
    return fibonacci(n - 2) + fibonacci(n - 1)  # but if user wants fibonacci number at index 4, it'll add
    # the fibonacci number at index (n-2) i.e. (4-2) and index (n-1) i.e. (4-1)
# so, it'll return 2nd position element i.e. 1 and 3rd position element i.e. 2 and then it's sum i.e. 3


n = int(input("Enter the number of Fibonacci numbers you want: "))

for i in range(n): # we print all the numbers in range that user inputs
    print(fibonacci(i))
