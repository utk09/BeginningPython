import sys

# import is used to add a library to our programs.
# The libraries are pre-written functions which can be directly used.
# sys is a library for "system"

print("Enter a mathematical expression. Make sure you've spaces in between numbers and operators. Eg: 5 * 6")
many_inputs = input()  # Type in format 5 + 4 and it'll give you answer. You can also do 5 - 3, 6 * 5 and so on.
splitting = many_inputs.split()

if splitting != 3:
    print("Formatting is wrong.")
    sys.exit()

left_val = int(splitting[0]) # we're doing indexing to take out left value, operator used and right value
operator = splitting[1]
right_val = int(splitting[2])

# answer = 0

if operator == '+':
    print("Addition:", left_val + right_val)
elif operator == '-':
    print("Subtraction:", left_val - right_val)
elif operator == '*':
    print("Multiplication:", left_val*right_val)
elif operator == '**' or operator == '^':
    print("Power:", left_val**right_val)
elif operator == "/":
    if right_val is not 0:
        print("Division:", left_val/right_val)
    else:
        print("Division by 0 not possible")
        sys.exit()
else:
    print("Unknown Operator detected. We don't know about {opr}".format(opr = operator))



