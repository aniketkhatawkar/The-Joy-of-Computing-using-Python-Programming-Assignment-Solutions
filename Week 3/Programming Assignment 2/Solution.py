L = input().split(' ')
for x in L:
  if x in L[L.index(x)+1:]:
    del L[L.index(x, L.index(x)+1)]
print(' '.join( L), end='')