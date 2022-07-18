import sys

k = int(sys.stdin.readline())

# 동: 1, 서: 2, 남: 3, 북: 4
height = []
width = []
total = []

for i in range(6):
    dir, dist = map(int, sys.stdin.readline().split())
    if dir == 1 or dir ==2:
        width.append(dist)
        total.append(dist)
    else:
        height.append(dist)
        total.append(dist)

bigbox = max(height) * max(width)

max_height = total.index(max(height)) 
max_width = total.index(max(width))

small1 = abs(total[max_height-1] - total[(max_height-5 if max_height == 5 else max_height +1)])

small2 = abs(total[max_width-1] - total[(max_width-5 if max_width == 5 else max_width +1)])
area = bigbox - (small1 * small2)
print(area*k)