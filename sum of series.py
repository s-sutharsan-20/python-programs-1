num=int(input("Enter the value of n:"))
s=0.0
for i in range(1,num+1):
    a=float(i**i)/i
    s=s+a
print("The sum of the series is ",s)
