#Fibonacci
def fib(n):
    """
    n >= 0, an integer
    """
    if n == 0 or n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
