import sys

N = int(input())

D = {}

for i in range(1,51):
  D[i] = set()

for _ in range(N):
  word = input()
  D[len(word)].add(word)

for i in range(1,51):
  dl = list(D[i])
  dl.sort()
  for l in dl:
    print(l)