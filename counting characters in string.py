def count(s):
    count={}
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print(count)
string=input("Enter any string :")
print(count(string))
