# This program will take input from User and tell whether it's Prime or Not.

import numpy as np # numpy is a mathematical library which does fast computation

print('''
Hey! Enter a number and I'll tell you if it's prime or not.
''')

num = int(input("Enter a number: "))

if num >= 2:
    divisors_list = []
    for divisor in range (2, num):
        # if num % divisor == 0:  # you can even use this commented 'if' statement.
        if np.remainder(num, divisor) == 0: # this makes calculation faster
            divisors_list.append(divisor)

    if len(divisors_list) == 0:
        print("{:d} is prime".format(num))
    else:
        print("{:d} is not prime because {:s} divide {:d}".format(num, str(divisors_list), num))
else:
    print("{:d} is not prime. Please enter a number greater than 1".format(num))

'''
The logic behind this is that --
First we take the user input 'num'.
We then iterate it over the range (2, num) because 2 is smallest prime number and 'num' can divide itself.
Then we find remainder of num divided by divisor.
If remainder of num divided by divisor is 0, it gets appended to the list.
If the list is empty, number is prime.
If the list has elements, the number is not prime.
If user inputs any number less than 2, it says please enter a number greater than 1.
'''