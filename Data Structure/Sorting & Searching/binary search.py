def binarySearch(alist,item):
    first = 0
    last = len(alist) - 1
    found = False

    while first < last and not found:
        mid =  (first + last)//2
        if alist[mid] == item:
            found = True
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


test = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(binarySearch(test, 3))
print(binarySearch(test, 13))
