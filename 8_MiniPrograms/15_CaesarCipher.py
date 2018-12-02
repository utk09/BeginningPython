'''
Let us now write a code for Caesar Cipher.
Read more about Ceaser Cipher here:
http://practicalcryptography.com/ciphers/caesar-cipher/
It is basically a substitution cipher, which each letter gets substituted by
another letter as specified by the key.
Eg: 'ABC' is my message, and key = 1
Then it'll become 'BCD' as
'A' will be substituted by 'B'
'B' will be substituted by 'C'
'C' will be substituted by 'D'
'''

MAX_KEY_SIZE = 26  # referes to maximum 26 letters in English Alphabets


def getMode():
    while True:
        print("Do you wish to Encrypt(e) or Decrypt(d) the message? ")
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print("Enter either 'encrypt' or 'e' or 'decrypt' or 'd' ")


def getMessage():
    print("Enter the message: ")
    return str(input())


def getKey():
    key = 0
    while True:
        print("Enter Key by which you want to Encrypt or Decrypt (1 - %s): " % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def translatedText(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if (num > ord('Z')):
                    num -= 26
                elif (num < ord('A')):
                    num += 26
            elif symbol.islower():
                if (num > ord('z')):
                    num -= 26
                elif (num < ord('a')):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


mode = getMode()
message = getMessage()
key = getKey()

if mode == 'encrypt' or mode == 'e':
    print("Your Encrypted message by key {:d} is: ".format(key))
    print(translatedText(mode, message, key))
else:
    print("Your Decrypted message by key {:d} is: ".format(key))
    print(translatedText(mode, message, key))