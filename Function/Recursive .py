def fibonacci(n):
    # Base Case

    if n == 0 :
        return 0;
    elif n == 1:
        return 1;

    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
# Example usage
print(fibonacci(10))