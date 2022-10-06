import sys
import heapq

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    min_heap = []
    max_heap = []
    visited = [False] * 1000001
    
    for i in range(k):
        op, n = map(str, sys.stdin.readline().split())
        if op == "I":
            heapq.heappush(min_heap,(int(n),i))
            heapq.heappush(max_heap, (-int(n), i))
            visited[i] = True

        else: # D인 경우
            #최소힙구현
            if n == "-1":
                #큐에 있고 visited False처리된 것 -> max_heap에서 삭제되었던 것
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap: # 위를 제외하고 큐에 있는 것
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    
            if n == "1":
                #큐에 있고 visited False처리된 것 -> min_heap에서 삭제되었던 것
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap: # 위를 제외하고 큐에 있는 것
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and visited[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
    while max_heap and visited[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])

    else:
        print("EMPTY")