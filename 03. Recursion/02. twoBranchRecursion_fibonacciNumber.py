def fibonacciNumber(n):
    if (n <= 1):
        return n
    else:
        return fibonacciNumber(n-1) + fibonacciNumber(n-2)
    
print(fibonacciNumber(5))