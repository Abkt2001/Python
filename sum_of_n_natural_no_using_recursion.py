def recursion(n):
    if n<1:
        return 0
    else:
        sum = 0
        sum = n + recursion(n-1)
        return sum


n=10
print(f"Sum of {n} natural no. is " ,recursion(10))