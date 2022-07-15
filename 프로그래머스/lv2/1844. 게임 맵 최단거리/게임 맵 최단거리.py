from collections import deque

def solution(maps):
    
    # 동서남북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    def bfs(x, y):
        queue = deque()
        # 처음 서있는 칸
        queue.append((x, y))
        # 큐가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()
            # 현재 위치에서 네 방향으로의 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 맵안에 있으면
                if 0<= nx < len(maps) and 0<= ny < len(maps[0]):
                    # 길이라면
                    if maps[nx][ny] == 1:
                        # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                        if maps[nx][ny] == 1:
                            maps[nx][ny] = maps[x][y] + 1
                            # 큐에 넣어 이 칸에서 네 방향 확인할 수 있도록 함
                            queue.append((nx, ny))
        #가장 오른쪽 아래까지의 최단 거리 반환
        return maps[-1][-1]
    answer = bfs(0, 0)
    return -1 if answer == 1 else answer

