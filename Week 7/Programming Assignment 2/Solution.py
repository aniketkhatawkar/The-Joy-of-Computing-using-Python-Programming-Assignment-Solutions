s = input()
def is_palindrome(s):
  if len(s) == 0:
    return 1
  elif len(s) == 1:
    return 1
  else:
    return s[0] == s[-1] and is_palindrome(s[1:-1])
print(int(is_palindrome(s)) , end='')