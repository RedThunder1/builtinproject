def rounder(inputNum: float, roundPlace: int = 0):
    """
    Parameters:
    inputNum: The number you want to be rounded
    roundPlace: To what decimal place you want to round the number.  If 0 it rounds to a whole number.

    For now, it rounds to a whole number, but I may make it so you can make it round to a certain place.
    It is also limited to 16 decimal places.
    """
    strNum = str(inputNum)
    wholeNum = int(strNum[:strNum.find('.')])
    decimals = strNum[strNum.find('.'):]
    # Simple Rounding
    if roundPlace == 0:
        if float(decimals[1]) >= 5:
            return wholeNum + 1
        elif float(decimals[1]) == 4:
            num = _rounder(inputNum, 1)
            strNum = str(num)
            if float(strNum[2]) > 4:
                return wholeNum + 1
            else:
                return wholeNum
        elif float(decimals[1]) < 4:
            return wholeNum
    else:
        # Complex Rounding
        return _rounder(inputNum, roundPlace)


def _rounder(inputNum, roundPlace):
    """
    Function used for rounding
    Will round to specified rounding place
    """
    strNum = str(inputNum)
    decimals = strNum[strNum.find('.'):]
    wholeNum = int(strNum[:strNum.find('.')])
    i = 1 + roundPlace
    while True:
        if len(decimals) == roundPlace + 1:
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
