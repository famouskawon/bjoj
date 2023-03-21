def VPS(ps):
  stacks = []
  for i, s in enumerate(ps) :
    if i == 0 and s == ")":
      return False
    elif s == "(" :
      stacks.append(s)
    elif s == ")" :
      if len(stacks) == 0:
        return False
      elif stacks[-1]=="(":
        stacks.pop()
  if len(stacks) == 0 :
    return True
  else :
    return False

T = int(input())
for _ in range(T):
  ps = input()
  if VPS(ps) :
    print("YES")
  else :
    print("NO")
  