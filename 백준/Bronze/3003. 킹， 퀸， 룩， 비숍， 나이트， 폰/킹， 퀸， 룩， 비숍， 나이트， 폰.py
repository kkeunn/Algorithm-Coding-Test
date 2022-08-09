import sys

white_pieces = [1, 1, 2, 2, 2, 8]
find = list(map(int,sys.stdin.readline().split()))

print(*map(lambda x, y: x-y, white_pieces, find))