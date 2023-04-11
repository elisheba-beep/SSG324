def factorial(x):
    if x == 0 or x == 1:
        return (1)
    return x * factorial(x-1)
    
print(factorial(4))

def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x - 1) + fib(x - 2)
    
    
print(fib(6))