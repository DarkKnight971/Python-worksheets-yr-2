def checkPalindrome(s) :
  for i in range(0, int(len(str)/2)) :
    if s[i] != str[len(str) - i - 1] :
      return False
  return True

s = input("Enter a string : ")

if (checkPAlindrome(s)) :
  print(f"{s} is a Palindrome")
else :
  print(f"{s} is not a Palindrome")
