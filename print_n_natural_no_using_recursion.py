def natural(n):
    if n<=0:
        return 

    print(n)
    return(natural(n-1))
    
def reversenatural(n):
    if n<=0:
        return
    
    reversenatural(n-1)
    print(n)
    


natural(5)
print("\n")
reversenatural(5)