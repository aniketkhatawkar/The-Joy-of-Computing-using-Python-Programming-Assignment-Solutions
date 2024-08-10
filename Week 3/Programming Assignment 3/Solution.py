L = input().split(' ')
L = [int(num) for num in L]
l = []
for i in range(len(L)):
  if i % 2:
    l += [L[i] + L[-(i+1)]]
  else:
    l += [L[i]]
print(' '.join(map(str,l)), end='')