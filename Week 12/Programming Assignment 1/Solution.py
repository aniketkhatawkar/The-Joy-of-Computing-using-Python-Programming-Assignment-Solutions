def collatz(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + collatz(n // 2)
    else:
        return 1 + collatz(n * 3 + 1)

n = int(input())
print(collatz(n), end="")
