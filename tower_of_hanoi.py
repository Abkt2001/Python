def tower(n, A, B, C):
    if n == 1:
        print("Move 1 from", A, "to", C)
    else:
        tower(n-1, A, C, B)
        print("Move", n, "from", A, "to", C)
        tower(n-1, B, A, C)


tower(3, 'A', 'B', 'C')
