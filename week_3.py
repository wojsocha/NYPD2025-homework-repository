#Wojciech Socha 439057
#week 3

def set_sum(lst1, lst2):
    sum = lst1
    for i in lst2:
        was_before = 0
        for j in lst1:
            if i == j:
                was_before = 1
        if not was_before:
            sum.append(i)
    return sum
    
#print(set_sum([], []))
#print(set_sum([1, 2, 3], [1, 2, 3]))
#print(set_sum([], [1, 2, 3]))
#print(set_sum([1, 2, 3], []))
#print(set_sum([1, 3, -2], [-2, -3, 0, 1, 34]))

def sorted_set_sum(lst1, lst2):
    i=0
    j=0
    sum = []
    while (i < len(lst1) and j < len(lst2)):
        if lst1[i] > lst2[j]:
            sum.append(lst2[j])
            j +=1
        elif lst1[i] < lst2[j]:
            sum.append(lst1[i])
            i +=1
        else:
            j += 1
        #print(sum, i ,j)
        
    if (len(lst1) == i):
        while(j < len(lst2)):
            sum.append(lst2[j])
            j +=1
    else:
        while(i < len(lst1)):
            sum.append(lst1[i])
            i +=1
    return sum

#print(sorted_set_sum([], []))
#print(sorted_set_sum([1, 2, 3], [1, 2, 3]))
#print(sorted_set_sum([], [1, 2, 3]))
#print(sorted_set_sum([1, 2, 3], []))
#print(sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]))