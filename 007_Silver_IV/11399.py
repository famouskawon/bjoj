N = int(input())
P = list(map(int,input().split()))

P.sort()

res = 0
for _ in range(N):
  res += sum(P)
  P.pop()
    
print(res)