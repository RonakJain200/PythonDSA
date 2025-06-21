


'''while low<=high:
    mid=low+(low-high)/2
    if (ar[mid]== value):
        print(mid)
    elif(ar[mid]<value):
        low=mid+1
        high=mid-1'''

'''def binarySearch(ar,low,high,value) :
    mid = low+(high-low)//2
    if ar[mid]==value:
        return mid
    elif ar[mid]<value:
        return binarySearch((ar,mid+1,high,value))
    else:
        return binarySearch((ar,low,mid-1,value))

ar = [1,2,4,6,7,8,9]


#without Recursion
low = 0
high = len(ar)-1
value=8



answer= binarySearch(ar,low,high,value)
print(answer)'''


def binarySearch(ar, low, high, value):
    if low > high:
        return -1  # value not found

    mid = low + (high - low) // 2

    if ar[mid] == value:
        return mid
    elif ar[mid] < value:
        return binarySearch(ar, mid + 1, high, value)
    else:
        return binarySearch(ar, low, mid - 1, value)


# Example usage:
ar = [1, 3, 5, 7, 9, 11]
value = 7
low = 0
high = len(ar) - 1

answer = binarySearch(ar, low, high, value)
print(answer)




