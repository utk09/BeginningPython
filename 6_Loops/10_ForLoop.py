'''
In a list of numbers from 1 to 100, make a list of numbers which are divisible by the number user inputs.
'''

list1 = []
list2 = []
for number in range(1, 101):
    list1.append(number)
print(list1)

divisor = int(input("Enter the number you want to divide by:"))

count = 0

for divNum in list1:
    if (divNum % divisor == 0 and divNum != divisor):
        count += 1
        list2.append(divNum)
print(list2)

print(count)
