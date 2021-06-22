def rec(n):
    if n < 10:
        return n
    return (rec(n//10) + n%10)


digi = 502
print("Sum of all the digits is ",rec(digi))