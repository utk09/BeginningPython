# Install pip from here: https://pip.pypa.io/en/stable/installing/
# pip is a package manager. if you want to install library in Python, just run pip install <name-of-library>
# and you need to go to your cmd or terminal to run this pip install <name-of-library>

# Eg: You want to install Numpy library.
# Go to cmd (Windows) or Terminal(Mac, Ubuntu)
# Type:   "python" or "python3" without the double quotes.
# Then press Enter.
# If you get something like this -- Python 3.7.0 (v3.....)
# Then it means your Python is on Path and now you're ready to run pip.

# Type: "pip install numpy"
# It'll start downloading and then install automatically.

# Install numpy from here: https://pypi.org/project/numpy/

# This program will take input from User and tell whether it's Prime or Not.


import numpy as np  # numpy is a mathematical library which does fast computation

# "as" is used to give a short name to library.
# you can write numpy as p, or numpy as num also. But accepted convention is np

print('''
Hey! Enter a number and I'll tell you if it's prime or not.
''')

num = int(input("Enter a number: "))

if num >= 2:
    divisors_list = []
    for divisor in range(2, num):
        # if num % divisor == 0:  # you can even use this commented 'if' statement.
        if np.remainder(num, divisor) == 0:  # this makes calculation faster
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
