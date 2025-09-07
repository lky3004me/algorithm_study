import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

word = list(input().strip())
alphabet = [-1] * 26

for i in range(len(word)):
    ch = word[i]
    ch_idx = ord(ch) - ord('a')

    if alphabet[ch_idx] == -1:
        alphabet[ch_idx] = i

for i in alphabet:
    print(i, end=" ")