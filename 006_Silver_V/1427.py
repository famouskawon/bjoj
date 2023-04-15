import sys

N = sys.stdin.readline()

sorted_num = sorted(N, reverse = True)

sorted_num_str = "".join(sorted_num)

print(sorted_num_str)
