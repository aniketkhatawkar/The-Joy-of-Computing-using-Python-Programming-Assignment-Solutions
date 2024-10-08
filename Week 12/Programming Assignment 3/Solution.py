def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    total_sum = 0
    for i in range(1, n + 1):
        if is_prime(i):
            total_sum += i
    return total_sum

n = int(input())

result = sum_of_primes(n)
print(result, end="")
