from queue import PriorityQueue
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()
sum = 0

for i in range(n):
    date = int(input())
    pq.put(date)

data1 = 0
data2 = 0

while pq.qsize() >1:
    data1 = pq.get()
    data2 = pq.get()
    tmp = data1 + data2
    sum += tmp
    pq.put(tmp)

print(sum)