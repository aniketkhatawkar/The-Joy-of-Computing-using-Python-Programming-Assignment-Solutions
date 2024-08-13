r = int(input())
c = int(input())
 
A = [ ]
for i in range(r):
  row = [ ]
  for x in input().split(' '):
    row.append(int(x))
  A.append(row)
 
flag = 0
for i in range(r):
  if flag:
    break
  for j in range(c):
    element = A[i][j]
    if element == min(A[i]):
      if A[i].count(element) > 1:
        continue
      col = []
      for m in range(r):
        col += [A[m][j]]
      if element == max(col):
        flag = 1
        break
 
print(flag, end='')