# Time = O(N^2) and Space = O(1), Stabilty = Yes
def bubbleSort(clist):
    length = len(clist)
    for i in range(length-1):
        for j in range(length-1-i):
            if clist[j]>clist[j+1]:
                clist[j],clist[j+1] = clist[j+1], clist[j]
    return clist
clist = [3,1,4,6]
print(bubbleSort(clist))