# Let us make a name ag which displays output in following format:
# First Name, then first letter of middle name, followed by a dot and then Last name.
# Eg: Utkarsh A.Tiwari

first_name = input("Enter First Name: ")  # asking user input
middle_name = input("Enter Middle name: ")
last_name = input("Enter Last Name: ")

first_name = first_name.capitalize()  # to capitalize the first alphabet, if user hasn't done it
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

output_formatted = "{first} {middle:.1s}. {last}"  # string formatting. The curly braces act as placeholders.
print("Hello,", output_formatted.format(first=first_name, middle=middle_name, last=last_name))

'''
Here, the first from output_formatted variable, is assigned the value of first_name variable.
Similarly for middle and last.
In {middle:.1s}, 's' represents string and '.1' means just the first character of the string.
The 'dot' after '{middle:.1s}' is because we wanted it in our output format. 
'''

# Typecasting.
# By default, 'input' function takes value as string.
# It means, even if you enter a number, it'll be made a string.
# So now, we'll learn to change str to int or float or any other data-type.
# Continuing the above example...

enter_response = str(input("So, how are you? "))  # Here, we're making the input string
print("Ohkay!")
# Now, let's typecast to integer
age_value = int(input("Enter your age: "))  # if user tries to enter anything other than an integer, it'll throw error.
output_formatted_1 = "Ahha! So you're {age} years old. Nice."
print(output_formatted_1.format(age=age_value))
