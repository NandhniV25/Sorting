# Time = O(N logN) and Space = O(N), Stabilty = No
def pivot(clist, pivotIndex, endIndex):
    swapIndex = pivotIndex
    for i in range(pivotIndex+1, endIndex+1):
        if clist[i]<clist[pivotIndex]:
            swapIndex += 1
            clist[i], clist[swapIndex] = clist[swapIndex], clist[i]
    clist[pivotIndex], clist[swapIndex] = clist[swapIndex], clist[pivotIndex]
    return swapIndex

def quickSort(clist, l, r):
    if l<r:
        pivotIndex = pivot(clist, l, r)
        quickSort(clist, l, pivotIndex-1)
        quickSort(clist, pivotIndex+1, r)
    return clist

clist = [3,5,0,6,2,1,4]
print(quickSort(clist,0,6))

