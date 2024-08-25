L = input().split(' ')
L = [int(num) for num in L]
def non_decreasing(L):
  if len(L) == 1:
    return True
  else:
    return L[1]-L[0] >=0 and non_decreasing(L[1:])
print(non_decreasing(L),end='')