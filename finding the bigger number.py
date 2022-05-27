n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))
n3=float(input("Enter the third number:"))
if(n1>n2 and n1>n3):
    print("First number: ",n1," is bigger")
elif(n2>n1 and n2>n3):
    print("Second number :",n2," is bigger")
else:
    print("Third number :",n3," is bigger")
