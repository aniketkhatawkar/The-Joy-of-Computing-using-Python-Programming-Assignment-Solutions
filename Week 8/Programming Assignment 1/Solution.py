def fun():
  sum = 0
  n = int(input())
  for i in range(n):
    L = input().split(' ')
    L = [int(num) for num in L]
    sum += L[0]
  return(sum)
print(fun(), end='')