# This program will take input from User and tell whether it's Prime or Not.

import numpy as np

print('''
Hey! Enter a number and I'll tell you if it's prime or not.
''')

num = int(input("Enter a number: "))
if num >= 2:
    divisors_list = []
    for divisor in range (2, num):
        # if num % divisor == 0:
        if np.remainder(num, divisor) == 0:
            divisors_list.append(divisor)

    if len(divisors_list) == 0:
        print("{:d} is prime".format(num))
    else:
        print("{:d} is not prime because {:s} divide {:d}".format(num, str(divisors_list), num))
else:
    print("{:d} is not prime. Please enter a number greater than 1".format(num))

