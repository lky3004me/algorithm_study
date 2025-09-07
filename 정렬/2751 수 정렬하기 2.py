# import sys
# sys.stdin = open("input.txt", "r")
#
# n = int(input())
# arr =[0 for _ in range(n)]
# for i in range(n):
#     arr[i] = int(input())
#
# def quick_sort(arr):
#     if len(arr) < 1:
#         return []
#
#     pivot = arr[0]
#     less = [x for x in arr[1:] if x <= pivot]
#     greater = [x for x in arr[1:] if x > pivot]
#
#     return quick_sort(less) + [pivot] + quick_sort(greater)
#
# arr = quick_sort(arr)
# for ele in arr:
#     print(ele)
import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())

import random

def quick_sort_inplace(a):
    stack = [(0, len(a) - 1)]
    while stack:
        l, r = stack.pop()
        while l < r:
            # randomized pivot
            p = random.randint(l, r)
            a[l], a[p] = a[p], a[l]
            pivot = a[l]

            # Hoare partition
            i, j = l - 1, r + 1
            while True:
                i += 1
                while a[i] < pivot: i += 1
                j -= 1
                while a[j] > pivot: j -= 1
                if i >= j:
                    m = j
                    break
                a[i], a[j] = a[j], a[i]

            # tail-call elimination: 큰 쪽을 스택에, 작은 쪽은 루프로
            if (m - l) < (r - (m + 1)):
                stack.append((m + 1, r))
                r = m
            else:
                stack.append((l, m))
                l = m + 1

quick_sort_inplace(arr)
for ele in arr:
    print(ele)