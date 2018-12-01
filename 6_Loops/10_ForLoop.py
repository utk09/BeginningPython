'''
In a list of numbers from 1 to 100, make a list of numbers which are divisible by,
the number which user inputs.
'''

list1 = []
list2 = []
for number in range(1, 101):
    '''
    To loop through a set of code a specified number of times, we can use the range() function,
    The range() function returns a sequence of numbers, starting from 0 by default, 
    and increments by 1 (by default), and ends at a specified number.
    '''
    list1.append(number)
print(list1)

divisor = int(input("Enter the number you want to divide by:"))

count = 0  # initial count is zero

for divNum in list1:
    if (divNum % divisor == 0 and divNum != divisor):
        count += 1
        list2.append(divNum)
print("Output List: ", list2)

print("Count is: ", count)

'''
A "for" loop is used for iterating over a sequence 
that is either a list, a tuple, a dictionary, a set, or a string.
'''
