def repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        for j in range(i+1, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
  
mylist = [10, 20, 30, 20, 20, 30, 40, 
         50, -20, 60, 60, -20, -20, 20, 70]
myslist=["a","A","a","b","c","c","c","c"]
print(repeat(mylist))
print(repeat(myslist))
