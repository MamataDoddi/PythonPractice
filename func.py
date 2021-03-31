mylist=[1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2==0

even=filter(even_bool,mylist)
print(list(even))

evens=map(even_bool,mylist)
print(list(evens))

def strm(str1):
    result=""
    for i in range(len(str1)):
        if i%2==0:
            result=result+str1[i]
    return result
str1="ABCeddf"
le=strm(str1)
print(le)

def dubb(str1):
    dub=""
    for i in str1:
        dub=dub+i*2
    return dub
str1="ABCeddf"

mystr=dubb(str1)
print(mystr)

me=(lambda dub,i:dub+i+i,str1)
print(list(me))