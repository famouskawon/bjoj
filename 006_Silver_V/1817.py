N, M = map(int, input().split())



box = M
numbox  = 1
if N == 0:
  numbox = 0
else :
  books = list(map(int,input().split()))
  for i in range(N):
    book = books[N-i-1]
    if box >= book :
      box -= book
    else :
      numbox += 1
      box = M-book
      
print(numbox)