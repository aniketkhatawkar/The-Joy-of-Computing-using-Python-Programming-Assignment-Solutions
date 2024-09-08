def are_anagrams(str1, str2):
  letters1 = ''
  letters2 = ''
  for i in str1:
    if i.isalpha():
      letters1 +=i.lower()
  for i in str2:
    if i.isalpha():
      letters2 +=i.lower()
  return(int(sorted(letters1) == sorted(letters2)))
str1 = input()
str2 = input()
print(are_anagrams(str1, str2), end='')