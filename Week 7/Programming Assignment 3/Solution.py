r = int(input())
c = int(input())
A = [ ]
for i in range(r):
  row = [ ]
  for x in input().split(' '):
    row.append(int(x))
  A.append(row)
T = [ ]
for j in range(c):
  row = [ ]
  for i in range(r):
    row.append(A[i][j])
  T.append(row)
b_flag = True
for i in range(c):
  for j in range(r):
    if A[i][j] != 0 and A[i][j] != 1:
      b_flag = False
      break
if b_flag == True:
  print('1' , end='')
else:
  print('0' , end='')
if T == A:
  print('1' , end='')
else:
  print('0' , end='')