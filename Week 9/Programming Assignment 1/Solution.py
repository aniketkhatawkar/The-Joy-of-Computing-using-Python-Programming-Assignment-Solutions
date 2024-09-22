def vowels(str):
  count = 0
  v = ['a','e','i','o','u','A','E','I','O','U']
  for l in str:
    if l in v:
      count += 1
  return count
str = input()
print(vowels(str), end='')