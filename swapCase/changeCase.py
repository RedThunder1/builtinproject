upperChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'Y', 'Z']
lowerChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'y', 'z']


def swapCase(inputStr: str):
    newStr = ""
    for char in inputStr:
        if char.isalpha():
            if char in upperChars:
                index = 0
                for letter in upperChars:
                    if char is letter:
                        break
                    index += 1
                newStr += lowerChars[index]
            else:
                index = 0
                for letter in lowerChars:
                    if char is letter:
                        break
                    index += 1
                newStr += upperChars[index]
        else:
            newStr += char
    return newStr


def toUpper(inputStr: str):
    newStr = ""
    for char in inputStr:
        if char.isalpha():
            if char in lowerChars:
                index = 0
                for letter in lowerChars:
                    if char is letter:
                        break
                    index += 1
                newStr += upperChars[index]
            else:
                newStr += char
        else:
            newStr += char
    return newStr


def toLower(inputStr: str):
    newStr = ""
    for char in inputStr:
        if char.isalpha():
            if char in upperChars:
                index = 0
                for letter in upperChars:
                    if char is letter:
                        break
                    index += 1
                newStr += lowerChars[index]
            else:
                newStr += char
        else:
            newStr += char
    return newStr
