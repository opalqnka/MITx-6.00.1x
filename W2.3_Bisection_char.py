def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr
        
    midIndex = int(len(aStr)/2)
    
    #if the char is greater or equal to aStr(midIndex) => search 2nd half of string. Add equal because if int cast
    if aStr[int(len(aStr)/2)] <= char:
        return isIn(char, aStr[midIndex:])
    #if the char is smaller than aStr(midIndex) => search 1st half of string
    else:
        return isIn(char, aStr[:midIndex])
