# Time = O(N^2) and Space = O(1), Stabilty = No
def selectionSort(clist):
    length = len(clist)
    for i in range(length):
        minIndex = i
        for j in range(i+1, length):
            if clist[minIndex]>clist[j]:
                minIndex = j
        clist[i],clist[minIndex] = clist[minIndex],clist[i]
    return clist
clist = [3,1,4,6]
print(selectionSort(clist))