x, y, w, h = map(int, input().split())
leftLine = x
rightLine = w-x
upperLine = h-y
lowerLine = y
print(min(leftLine, rightLine, upperLine, lowerLine))