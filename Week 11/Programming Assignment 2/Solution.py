L = input().split(':')
L = [int(num) for num in L]
common_factors = []
for i in range(1, min(L)+1):
  flag = True
  for n in L:
    if n % i == 0:
      continue
    else:
      flag = False
      break
  if flag == True:
    common_factors += [i]
print(' '.join(map(str,common_factors)), end='')
