def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    x = max(a, b)
    y = min(a, b)
    gcd = y
    
    while gcd >= 1:
        if x % gcd != 0:
            gcd = gcd - 1            
        elif y % gcd != 0:
            gcd = gcd - 1            
        else:
            return gcd
