r = int(input())
 
A = [ ]
for i in range(r):
  row = [ ]
  for x in input().split(' '):
    row.append(int(x))
  A.append(row)
 
T = [ ]
for j in range(r):
  row = [ ]
  for i in range(r):
    row.append(A[i][j])
  T.append(row)
 
flag = 0
for i in range(r):
  for j in range(r):
    if A[i][j] == -1 * T[i][j]:
      continue
    else :
      print(0, end='')
      flag = 1
      break
  if flag :
    break
else:
  print(1, end='')