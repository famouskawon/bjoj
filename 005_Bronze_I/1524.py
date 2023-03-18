T = int(input())
for _ in range(T):
    input()
    N, M = map(int,input().split())
    Npowers = list(map(int,input().split()))
    Mpowers = list(map(int,input().split()))
    NMpowers = Npowers + Mpowers

    if max(Npowers) < max(Mpowers):
        print("B")
    else :
        print("S")