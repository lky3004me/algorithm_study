def quick_sort_inplace(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left +=1
        while right > start and arr[right] >= arr[pivot]:
            right -=1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort_inplace(arr, start, right - 1)
    quick_sort_inplace(arr, right + 1, end)

data = [5, 3, 8, 4, 2, 7, 1, 10]
