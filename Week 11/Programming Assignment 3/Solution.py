L = input()
mapper = [ 'a', 'k', 'x', 'y', 's', 'm', 'b', 'd', 'p', 'z' ]
date = ''
for x in L:
  if x == '-':
    date += '-'
  else:
    date += str(mapper.index(x))
print(date, end='')