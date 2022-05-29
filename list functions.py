
list=[]
n=int(input("enter the number of elements in list"))
i=1
for i in range(n):
   l=float(input("Enter a element of list:"))
   list.append(l)
   i+=1
print(max(list))
print(min(list))
print(sum(list))
