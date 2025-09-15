arr = [1,3,5,7,9,11]

def binary1(arr, target):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid+1
    return -1
def binary2(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid -1
def binary3(arr, target):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start + end)//2

        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid +1
        else:
            end = mid - 1
def binary4(arr, target):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start + end)//2

        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid +1
        else:
            end = mid - 1
def binary5(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary(arr, target, start, mid - 1)
    else:
        return binary(arr, target, mid +1, end)
def binary(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid]>target:
        return binary(arr, target, mid +1, end)
    else:
        return binary(arr, target, start, mid-1)

print(binary(arr, 7, 0, len(arr)-1))