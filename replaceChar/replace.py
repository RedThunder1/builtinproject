def replaceChar(inputStr: str, rChar: str, newChar: str):
    """
    My version of replaceChar.
    This function will replaceChar all the specified characters with the new characters

    Parameters
    inputStr: The string you want to change
    replaceChar: The characters you want to change
    newChar: The character to replaceChar with

    Limitations This function can only replaceChar characters and nothing else I may eventually make it so you can
     replaceChar words and phrases.
    """
    index = [0, 0]
    finalStr = ""
    for c in inputStr:
        if c == rChar:
            finalStr += newChar
            index[1] = index[0]
        else:
            finalStr += c
        index[0] += 1
        if index == len(inputStr) - 1:
            finalStr += inputStr[len(inputStr) - 1]
    return finalStr
