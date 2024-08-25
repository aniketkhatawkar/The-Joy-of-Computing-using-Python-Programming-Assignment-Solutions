a = int(input())
def log2(a):
  if a == 1:
    return 0
  else:
    return 1 + log2(a/2)
print(log2(a), end='')