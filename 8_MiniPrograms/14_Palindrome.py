'''
Let us write a program to check if a given string is Palindrome or Not.
A palindrome is a string that reads the same forward or reversed.
Eg: 'abba' is Palindrome, '12321' is palindrome, 'abda' is not a palindrome.
'''


def palindrome(pal):
    for i in range(len(pal) // 2):  # to find the central value and iterate till there
        if pal[i] != pal[len(pal) - i - 1]:  # checks if last element is equal to first, 2nd last equal to 2nd and so on
            return ("'{:s}' is not a Palindrome".format(pal))

    return ("'{:s}' is Palindrome".format(pal))


pal = str(input("Enter a string: "))
print(palindrome(pal))
