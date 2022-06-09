number=[1,2,3,4,5,6,7,8,9,10]
for ords in number:
    print(ords)
for ords in number:
    if ords==1:
        print(str(ords)+"st")
    elif ords==2:
        print(str(ords)+"nd")
    elif ords==3:
        print(str(ords)+"rd")
    else:
        print(str(ords)+"th")
