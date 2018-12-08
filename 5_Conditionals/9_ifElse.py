# Conditionals are True-False statements.
# "If" the given condition is true, it'll be executed, "else", something otherwise will happen.

your_name = str(input("Enter your name: "))
if your_name == 'Utkarsh':  # a condition to match the input with name "Utkarsh"
    print("Hey Utkarsh! Long time, no see.")
else:  # if input does not match, this "else" will be executed
    print("Whoa! You're new here.")

'''
The spacing that you see, is called Indentation. 
It works as curly braces, like in C, C++, Java.
It shouldn't be removed, otherwise it'll give error.
1 Indent = 1 Tab Key OR 4 Space-bar Key
'''

your_age = int(input("Enter your age: "))
if your_age >= 13:
    gmail_id = str(input("Do you have email ID? Yes or No? "))
    if gmail_id == "Yes" or gmail_id == "yes" or gmail_id == "yupp":
        print("You're eligible to join Facebook.")
    elif gmail_id == "No" or gmail_id == "no" or gmail_id == "nope":  # elif is like an else-if combination
        print("Make a email ID and then you can join Facebook.")
        print("Or, you can even join using Mobile number.")
    else:
        exit()
else:
    print("Sorry kiddo! You're not allowed.")

# or is a keyword. it means between this or this or this, at least one should be True.
# If any of them matches, statement will be true.
# Some other keywords are "and", "not".

city_name = str(input("Enter the name of your city: "))
pincode = int(input("Enter your Pincode: "))

if city_name == "Mumbai" and pincode == 400045:
    # here, when both conditions are true, then it'll execute the statement under "if"
    print("Hallelujah! We live so close!")
elif city_name == "Mumbai":
    print("Hmm... Let's catch-up sometime later.")
else:
    print("See ya!")

'''
2 ">" 3 means 2 "greater than" 3
5 "<" 9 means 5 "less than" 9
"=" is assignment operator. It assigns a value
"==" is checking if LHS and RHS are equal
Other operators are ">=", "<="
'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num2 is not 0:
    print("num1 divided by num2 is: ", num1 / num2)
else:
    print("Make sure second number is not zero.")
