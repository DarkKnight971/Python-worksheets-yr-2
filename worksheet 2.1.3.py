'''3.	Write a Python program to add 'ing' at the end of a given string
    (length should be at least 3). If the given string already ends
    with 'ing' then add 'ly' instead. If the string length of the
    given string is less than 3, leave it unchanged. Example:- Sample
    String : 'abc' Expected Result : 'abcing' Sample String : 'string'
    Expected Result : 'stringly'''

def string_box(str) :
  l = len(s)
  
  if (l >= 3) :
    if s[-3 : ] == 'ing' :
      s+"ly"
    else :
      s + "ing"
  
  return s

s_str = input("Enter a string : ")
t = s

e_str = string_box(s_str)

if e_str == t :
  print("No change")
else :
  print(f"Updated value : {e_str}")
