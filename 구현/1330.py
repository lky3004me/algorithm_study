import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a, b = map(int, input().split())

if a > b :
    print(">")
elif a < b:
    print("<")
else:
    print("==")