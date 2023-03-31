def replaceChar(inputStr: str, replaceChar: str, newChar: str):
    """
    My version of replace.
    This function will replace all the specified characters with the new characters

    Parameters
    inputStr: The string you want to change
    replaceChar: The characters you want to change
    newChar: The character to replace with

    Limitations
    This function can only replace characters and nothing else I may eventually make it so you can replace words and phrases.
    """
    index = [0, 0]
    finalStr = ""
    for c in inputStr:
        if c == replaceChar:
            finalStr += newChar
            index[1] = index[0]
        else:
            finalStr += c
        index[0] += 1
        if index == len(inputStr) - 1:
            finalStr += inputStr[len(inputStr) - 1]
    return finalStr
