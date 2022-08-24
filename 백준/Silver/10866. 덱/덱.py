from collections import deque
import sys

N = int(sys.stdin.readline())
q = deque()

for i in range(N):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push_front':
        q.appendleft(command[1])

    elif command[0] == 'push_back':
        q.append(command[1])

    elif command[0] == 'pop_front':
        if not q:
            print("-1")
        else:
            temp = q.popleft()
            print(temp)

    elif command[0] == 'pop_back':
        if not q:
            print("-1")
        else:
            temp = q.pop()
            print(temp)

    elif command[0] == 'front':
        if not q:
            print("-1")
        else:
            print(q[0])

    elif command[0] == 'back':
        if not q:
            print("-1")
        else:
            print(q[-1])

    elif command[0] == 'size':
        print(len(q))

    elif command[0] == 'empty':
        print(0 if q else 1)