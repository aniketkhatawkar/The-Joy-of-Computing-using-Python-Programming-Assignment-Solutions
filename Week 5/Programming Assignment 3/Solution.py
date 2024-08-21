L = input().split(' ')
L = [int(num) for num in L]
k = int(input())
L.sort()
if L[k-1] == L[-k]:
  if k == len(L)//2+1:
    print('1',end = '')
  else:
    print('-1',end = '')
else:
  print('0',end = '')