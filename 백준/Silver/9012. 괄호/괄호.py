import sys
t = int(sys.stdin.readline().rstrip())


for _ in range(t):
    string = sys.stdin.readline().rstrip()
    stack = []
    dict = {')': '('}
    for s in string:
        no_vps = 0
        if stack and s in dict.keys():
            stack.pop()
        elif not stack and s in dict.keys():
            no_vps = 1
            break
        else:
            stack.append(s)

    if stack or no_vps == 1:
        print("NO")
    else:
        print("YES")
