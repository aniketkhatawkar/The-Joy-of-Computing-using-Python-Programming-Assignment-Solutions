L1 = input().split(' ')
L1 = [int(num) for num in L1]
L2 = input().split(' ')
L2 = [int(num) for num in L2]
L = []
c1,c2 = 0,0
while(1):
  if c1 < len(L1) and L1[c1] <= L2[c2]:
    L += [L1[c1]]
    c1+=1
    if c1 == len(L1):
      L += L2[c2:]
      break
  elif c2 < len(L2) and L2[c2] <= L1[c1]:
    L += [L2[c2]]
    c2+=1
    if c2 == len(L2):
      L += L1[c1:]
      break
print(' '.join(map(str,L)), end='')