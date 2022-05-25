num1=float(input("Enter the 1st number:"))
num2=float(input("Enter the 2nd number:"))
choice=input("Enter any operator (+,-,*,/,%,**,//) :")

if choice in ('+','-','*','/','%','**','//'):
    

    if choice=='+':
        print(num1+num2)
    if choice=='-':
        print(num1-num2)
    if choice=='*':
        print(num1*num2)
    if choice=='/':
        print(num1/num2)
    if choice=='%':
        print (num1%num2)
    if choice=='**':
        print(num1**num2)
    if choice=='//':
        print(num1//num2)

else:
        print("invalid input")
