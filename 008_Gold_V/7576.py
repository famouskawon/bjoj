M, N = map(int,input().split())

Map = []
numz = 0

one_s = []
for n in range(N):
    temp_l = list(map(int,input().split()))
    Map.append(temp_l)
    for m, x in enumerate(temp_l):
        if x == 0 :
            numz += 1
        elif x == 1 :
            one_s.append((n,m))
            
result = 0
dn = [-1,0,1,0]
dm = [0,1,0,-1]

while True:
    if numz == 0:
        break
    result += 1
    one_s_len = len(one_s)
    for t in range(one_s_len):
        n, m = one_s[t]
        for i in range(4):
            if n+dn[i] in range(N) and m+dm[i] in range(M) and Map[n+dn[i]][m+dm[i]] == 0:
                numz-=1
                Map[n+dn[i]][m+dm[i]] = 1
                one_s.append((n+dn[i],m+dm[i]))

    one_s = one_s[one_s_len:]

    if not one_s and numz != 0:
        result =-1
        break
                
print(result)
