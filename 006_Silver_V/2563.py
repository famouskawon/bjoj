N = int(input())
# N = 3
background = [[1]*100 for _ in range(100)]

lists = []

for _ in range(N):
    # temp_list = [3,7]
    temp_list = [int(x) for x in (input().split())]
    # print(temp_list[0]-1)
    # print(temp_list[0]+10)
    # print(temp_list[1]-1)
    # print(temp_list[1]+10)
    for i in range(temp_list[0]-1,temp_list[0]+9):
        for j in range(temp_list[1]-1,temp_list[1]+9):
            background[i][j] *=0


print(100*100-sum([r.count(1) for r in background]))