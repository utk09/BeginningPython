# Let us now look at String Methods.
# String methods are like additional actions that strings can be performed.

alpha = 'this is SOME smalls'
beta = 'THIS IS ALL CAPS'
gamma = '####$$$$%%%%****'

alpha_capitalized = alpha.capitalize()  # capitalizes the first letter
print("Old String:=", alpha)
print("New Capitalized String:=", alpha_capitalized)

beta_casefold = beta.casefold()  # makes all letters small
print("Old String:=", beta)
print("New casefold string:=", beta_casefold)

alpha_centered = alpha.center(24)  # The center() method returns a string which is padded with the specified character.
print("Old String:=", alpha)
print("New Centered String:=", alpha_centered)  # Here, before and after the string,
                                                # there are 24 characters in total, including spaces


