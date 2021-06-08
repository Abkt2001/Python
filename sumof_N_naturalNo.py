a = input("Enter a natural no :- ")

def sum(a):
    s = 0
    for x in range (1,a+1):
        s = s + x
    return s

print("Sum of n Natural Number is ",sum(a))

