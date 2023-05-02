def findTheWinner(n,k):
    list = []
    start = 0
    for i in range(n):
        list.append(i+1)
    print(list)
    print(len(list))
    
    while len(list) != 1:
        if (k > len(list) and len(list)!=1):
            list.pop()
            
        if list[k-1] == list[len(list)-1]:
            list.pop(list[len(list)-2])
            
        else:
            list.pop(list[k-1])
    return list[0]
        
# wrong

print(findTheWinner(5,2))
        