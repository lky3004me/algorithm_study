import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

for i in range(1, 10):
    print(str(n) + " * " + str(i) + " = " + str(n*i))