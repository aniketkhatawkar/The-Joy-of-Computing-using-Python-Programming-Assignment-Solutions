def avglen(str):
  words = str.split(' ')
  avg = 0
  for w in words:
    avg += len(w)
  avg /= len(words)
  if avg > 4:
    return 1
  else :
    return 0
str = input()
print(avglen(str), end='')