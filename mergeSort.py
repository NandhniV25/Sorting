# Time = O(N logN) and Space = O(N), Stabilty = Yes
def merge(clist, l, m, r):
    # calculate the length of two subarrays
    n1 = m-l+1
    n2 = r-m
    # create empty two subarrays
    L = [0]*n1
    R = [0]*n2
    # copy the elements from the list
    for i in range(n1):
        L[i] = clist[l+i]
    for j in range(n2):
        R[j] = clist[m+1+j]
    # initial the index of the merge arrays
    i, j, k = 0, 0, l
    # compare the equal elements in the two subarray
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            clist[k] = L[i]
            i += 1
        else:
            clist[k] = R[j]
            j += 1
        k += 1
    # copy the remaining subarray elements
    while i<n1:
        clist[k] = L[i]
        i += 1
        k += 1
    while j<n2:
        clist[k] = R[j]
        j += 1 
        k += 1

def mergeSort(clist, l, r):
    if l<r:
        m = (l+r)//2
        mergeSort(clist, l, m)
        mergeSort(clist, m+1, r)
        merge(clist, l, m, r)
    return clist
clist = [3,1,4,6,2]
print(mergeSort(clist,0,4))