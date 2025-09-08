# import sys
# from collections import deque
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
#
# # 트럭 수, 다리 길이, 다리 최대 하중
# n, w, L = map(int, input().split())
# # 트럭 무게 리스트
# trucks = list(map(int, input().split()))
#
# bridge = deque([0] * w)
# curr_weight = 0
# time = 0
# # 다음에 올릴 트럭 idx
# idx = 0
#
# while idx < n or curr_weight > 0:
#     time +=1
#
#     left = bridge.popleft()
#     curr_weight -= left
#
#     if idx < n and curr_weight + trucks[idx] <= L:
#         bridge.append(trucks[idx])
#         curr_weight += trucks[idx]
#         idx +=1
#     else:
#         bridge.append(0)
#
# print(time)
import sys
from collections import deque
sys.stdin= open("input.txt", "r")
input = sys.stdin.readline

# 트럭의 수, 다리의 길이, 다리의 최대 하중
n,w,L = map(int, input().split())
# 트럭 무게 리스트
weightList = list(map(int, input().split()))
current_weight = 0
queue = deque([0] * w)
idx = 0
time = 0

while current_weight > 0 or idx < n:
    time +=1

    left = queue.popleft()
    current_weight -= left

    if idx < n and current_weight + weightList[idx] <= L:
        queue.append(weightList[idx])
        current_weight += weightList[idx]
        idx +=1
    else:
        queue.append(0)

print(time)