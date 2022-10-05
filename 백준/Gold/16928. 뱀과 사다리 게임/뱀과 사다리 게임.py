import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [i for i in range(101)]
visited = [0] * 101

# bfs 탐색
def bfs(x):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([x])
    #방문처리
    visited[x] = 1

    # 큐가 빌 때까지 반복
    while queue:
        a = queue.popleft()

        # 주사위 눈 범위 확인
        for i in range(1, 7):
            b = a + i

            # 100칸이 넘어가면 무시
            if b > 100:
                continue

            nx = graph[b]

            # 방문하지 않은 칸
            if visited[nx] == 0:
                queue.append(nx)
                visited[nx] = visited[a] + 1

                # 100번째 칸까지 가면
                if nx == 100:
                    return


for _ in range(n + m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x] = y


bfs(1)
print(visited[100] - 1)