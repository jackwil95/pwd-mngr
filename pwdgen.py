import random
import string

# Randomising functions


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Password generation


def passwordGen():
    uppercaseLetter1 = chr(random.randint(65, 90))
    uppercaseLetter2 = chr(random.randint(65, 90))
    uppercaseLetter3 = chr(random.randint(65, 90))
    lowercaseLetter1 = chr(random.randint(97, 122))
    lowercaseLetter2 = chr(random.randint(97, 122))
    lowercaseLetter3 = chr(random.randint(97, 122))
    digit1 = chr(random.randint(48, 57))
    digit2 = chr(random.randint(48, 57))
    digit3 = chr(random.randint(48, 57))
    punctuationSign1 = random.choice(string.punctuation)
    punctuationSign2 = random.choice(string.punctuation)
    punctuationSign3 = random.choice(string.punctuation)
    # Combine and shuffle
    password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + lowercaseLetter1 + lowercaseLetter2 + \
        lowercaseLetter3 + digit1 + digit2 + digit3 + punctuationSign1 + punctuationSign2 + punctuationSign3
    password = shuffle(password)
    # print(password)

#
# passwordGen()
