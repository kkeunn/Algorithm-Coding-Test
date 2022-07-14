n = int(input())

def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))
    

f = [1] * 40
def fibonacci_iterative(n):
    for i in range(3, n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]

print(fibonacci_recursive(n))
count2 = n-2
print(count2)