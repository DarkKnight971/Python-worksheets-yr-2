#1.	Python program to check whether the string is Symmetrical or Palindrome

def checkPalindrome(str) :
  for i in range(0, int(len(str)/2)) :
    if str[i] != str[len(str) - i - 1] :
      return False
  return True

s = input("Enter a string : ")
check = checkPalinrome(s)

if check :
  print(f"{s} is a Palindrome")
else :
  print(f"{s} is not a Palindrome")
