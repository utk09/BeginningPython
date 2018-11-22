# Let us now look at String Methods.
# String methods are like additional actions that strings can be performed.

alpha = 'this is SOME smalls'
beta = 'THIS IS ALL CAPS'
gamma = '####$$$$%%%%****'


# Capitalize
alpha_capitalized = alpha.capitalize()  # capitalizes the first letter
print("Old String:=", alpha)
print("New Capitalized String:=", alpha_capitalized)

# Casefold
beta_casefold = beta.casefold()  # makes all letters small
print("Old String:=", beta)
print("New casefold string:=", beta_casefold)

# Center the String
alpha_centered = alpha.center(24)  # The center() method returns a string which is padded with the specified character.
print("Old String:=", alpha)
print("New Centered String:=", alpha_centered)  # Here, before and after the string,
                                                # there are 24 characters in total, including spaces

# You can even add your own characters around the string
beta_centered = beta.center(24, '?')
print("Old String:=", beta)
print("New Centered String:=", beta_centered)

# String Count
# The string count() method returns the number of occurrences of a substring in the given string.
delta = "We are students of KJSIEIT. We are learning Python. We are enjoying it!"
substring = "ear"
count = delta.count(substring)
print("The count is:=", count)
# The answer is one because there is one 'ear' in 'learning'

another_substring = "a"





