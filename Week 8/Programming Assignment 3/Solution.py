def fun(L,k):
  for i in range(len(L)):
    L[i] *= k
  return(max(L))
L = input().split(' ')
L = [int(num) for num in L]
k = int(input())
print(fun(L,k), end='')