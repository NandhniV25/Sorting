# Time = O(N^2) and Space = O(1), Stabilty = Yes
def insertionSort(clist):
    length = len(clist)
    for i in range(1,length):
        key = clist[i]
        j=i-1
        while j>=0 and key<clist[j]:
            clist[j+1]=clist[j]
            j-=1
        clist[j+1]=key
    return clist
clist = [3,1,4,6,2]
print(insertionSort(clist))