import sys

stack =[]

def Push(X):
  stack.append(X)

def Pop():
  if stack == []:
    print(-1)
  else :
    print(stack.pop(len(stack)-1))

def Size():
  print(len(stack))

def Empty():
  if stack == []:
    print(1)
  else :
    print(0)

def Top():
  if stack == [] :
    print(-1)
  else :
    print(stack[-1])

N = int(sys.stdin.readline())
for _ in range(N):
  c = sys.stdin.readline()
  C = c.split()[0]
  if C == "push":
    Push(c.split()[1])
  elif C == "pop":
    Pop()
  elif C == "size":
    Size()
  elif C == 'empty' :
    Empty()
  else :
    Top()