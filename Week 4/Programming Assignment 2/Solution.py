r = int(input())
c = int(input())
 
A = [ ]
for i in range(r):
  row = [ ]
  for x in input().split(' '):
    row.append(int(x))
  A.append(row)
 
s = int(input())
 
T = [ ]
for j in range(c):
  row = [ ]
  for i in range(r):
    row.append(A[i][j])
  T.append(row)
 
for i in range(c):
  for j in range(r):
    if j == r-1:
      print(T[i][j]*s, end="")
    else :
      print(T[i][j]*s, end=" ")
  if (i,j)!=(c-1,r-1):
    print()