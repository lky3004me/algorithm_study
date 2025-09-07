import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
siteDict = dict()
for i in range(n):
    key, value = input().split()

    siteDict[key] = value

for i in range(m):
    print(siteDict.get(input().strip()))