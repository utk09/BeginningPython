'''
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
In Python a function is defined using the "def" keyword.
To call a function, use the function name followed by parenthesis.
'''

# Let us write a function to calculate area_of_circle.

pi = 3.14159  # we assign a value to variable "pi"


def area_of_circle(r):  # create a function named area_of_circle and parameter "r"
    return pi * r * r  # the formula to calculate area_of_ circle


print(area_of_circle(5))  # prints area of circle with radius 5. Change '5' to '6' and run.

x = int(input("Enter radius(r): "))  # we can even ask for user input and calculate area
print("Area of circle from user input: ", area_of_circle(x))


# Calculate volume of cone from user inputs
# we will use pi which has been declared above

def volume_of_cone(r, h):
    return (1 / 3) * pi * (r * r) * (h)  # return means to give back the value obtained


r = int(input("Enter radius(r): "))
h = int(input("Enter height(h): "))
print("Volume of cone from user input is: ", volume_of_cone(r, h))
