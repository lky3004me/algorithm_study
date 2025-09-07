import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

word = input().strip().upper()
alphabet_count = [0] * 26  # A~Z
for ch in word:
    alphabet_count[ord(ch) - ord('A')] += 1

max_count = max(alphabet_count)
if alphabet_count.count(max_count) > 1:
    print('?')
else:
    print(chr(alphabet_count.index(max_count) + ord('A')))


