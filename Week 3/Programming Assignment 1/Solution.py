L = input().split(' ')
L = [int(num) for num in L]
max1 = L[0]
for x in L:
  if x > max1:
    max1 = x
for x in L:
  if x != max1:
    max2 = x
for x in L:
  if x > max2 and x != max1:
    max2 = x
print(max2, end='')