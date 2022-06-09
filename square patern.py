n=6
for row in range(n):
    for column in range(n):
        if row==n-1 or column==n-1 or row==0 or column==0:
            print(" x",end="  ")
        else:
            print("x ",end="  ")
    print("  ")
