L = input().split(' ')
a = int(L[0])
b = int(L[1])
def recursive_product(a,b):
  if b == 0:
    return 0
  if b == 1:
    return a
  else:
    return a + recursive_product(a,b-1)
print(recursive_product(a,b), end='')