def dch(a,b):
  if a[0] > b[0] and a[1]>b[1]:
    return True
  else :
    return False

l = []


N = int(input())

for i in range(N):
  (x, y) = map(int,input().split())
  new = (x,y)
  l.append(new)

D = {}

for i, a in enumerate(l):
  D[i]=1
  for b in l:
    if dch(b,a):

      D[i] += 1

print(' '.join(map(str, D.values())))
