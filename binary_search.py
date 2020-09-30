def binary_search(arr,low,high,x):
    if high >= low:
        mid =  (low+high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1

#Iterative method:

def binary_search_itr(arr,x):
    low = 0
    high = len(arr)-1
    mid = 0
    while(high >= low):
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1
