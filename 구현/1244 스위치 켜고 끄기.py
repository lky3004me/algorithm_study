# import sys
# # sys.stdin = open("input.txt", "r")  # 로컬 테스트 시 사용
# input = sys.stdin.readline
#
# n = int(input())
# status = list(map(int, input().split()))
# s = int(input())
#
# for _ in range(s):
#     sex, num = map(int, input().split())
#     if sex == 1:
#         # 남학생: num의 배수 인덱스(1-based)를 토글 → 0-based로 변환하면 num-1부터
#         for i in range(num-1, n, num):
#             status[i] ^= 1
#     else:
#         # 여학생: 중심에서 좌우 대칭으로 값이 같은 동안만 확장 후, 그 구간 전체 토글
#         idx = num - 1  # 0-based
#         l = r = idx
#         while l - 1 >= 0 and r + 1 < n and status[l - 1] == status[r + 1]:
#             l -= 1
#             r += 1
#         for i in range(l, r + 1):
#             status[i] ^= 1
#
# # 출력: 20개씩 줄바꿈
# for i in range(n):
#     end_char = '\n' if (i + 1) % 20 == 0 else ' '
#     print(status[i], end=end_char)
# # 마지막 줄이 20개로 딱 안 끊겼으면 개행 한 번
# if n % 20 != 0:
#     print()
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

switNum = int(input())
switStatus = list(map(int, input().split()))
studNum = int(input())
for _ in range(studNum):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(num-1, switNum, num):
            switStatus[i] ^= 1
    else:
        left, right = num-1, num-1

        while 0<= left-1 < switNum and 0<= right+1 < switNum:
            if switStatus[left-1] == switStatus[right+1]:
                left -=1
                right +=1
            else:
                break
        for i in range(left, right+1):
            switStatus[i] ^=1

# 출력: 20개씩 줄바꿈
for i in range(switNum):
    end_char = '\n' if (i + 1) % 20 == 0 else ' '
    print(switStatus[i], end=end_char)
# 마지막 줄이 20개로 딱 안 끊겼으면 개행 한 번
if switNum % 20 != 0:
    print()