decimals: str
wholeNum: int
rndPlace: int
checked = False


def rounder(inputNum: float, roundPlace: int = 0):
    """
    Parameters:
    inputNum: The number you want to be rounded
    roundPlace: To what decimal place you want to round the number.  If 0 or None it will round to a whole number.

    For now, it rounds to a whole number, but I may make it so you can make it round to a certain place.
    It is also limited to 16 decimal places.
    """
    global decimals, wholeNum, rndPlace
    strNum = str(inputNum)
    wholeNum = int(strNum[:strNum.find('.')])
    decimals = strNum[strNum.find('.'):]
    # Simple Rounding
    if roundPlace == 0:
        if float(decimals[1]) >= 5:
            return wholeNum + 1
        elif float(decimals[1]) == 4:
            return _simpleRound()
        elif float(decimals[1]) < 4:
            return wholeNum
    else:
        # Complex Rounding
        rndPlace = roundPlace
        return _complexRounder()


def _simpleRound():
    """
    Function used for simple rounding
    Will round to a whole number

    THis function is a mess and will be cleaned up later because im lazy
    """
    global decimals, wholeNum, checked
    i = 2
    while not checked:
        if len(decimals) == 2 and float(decimals[1]) < 5:
            checked = True
            return wholeNum
        if len(decimals) == 2 and float(decimals[1]) > 4:
            checked = True
            return wholeNum + 1
        if float(decimals[i]) > 4:
            if i == 1:
                checked = True
                return wholeNum + 1
            else:
                decimals = decimals[:i - 1] + str(int(decimals[i - 1]) + 1)
                i = 2
        elif len(decimals) == i + 1:
            return wholeNum
        else:
            i += 1


def _complexRounder():
    """
    Function used for complex rounding
    Will round to specified rounding place
    """
    global decimals, wholeNum, checked, rndPlace
    i = 1 + rndPlace
    while not checked:
        if len(decimals) == rndPlace + 1:
            return float(wholeNum) + float(decimals)
        else:
            if float(decimals[i]) > 4:
                decimals = decimals[:i - 1] + str(int(decimals[i - 1]) + 1)
                i = 2
            elif float(decimals[i]) < 5:
                if len(decimals) == i + 1:
                    return float(wholeNum) + float(decimals)
                else:
                    i += 1
