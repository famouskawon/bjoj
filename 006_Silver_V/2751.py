import sys 

N = int(sys.stdin.readline().rstrip())
L = []

for _ in range(N):
    s = int(sys.stdin.readline().rstrip())
    L.append(s)


L.sort()
for i in S:
    print(i)