def SelfNumber(n):
    result = n
    for i in str(n):
        result += int(i)
    return result

numberList = list(range(1,10001))

for i in numberList:
    j = SelfNumber(i)
    while j < 10001 :
        if j in numberList:
            numberList.remove(j)
        j = SelfNumber(j)

for k in numberList:
    print(k)