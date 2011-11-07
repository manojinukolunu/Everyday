def double_char(str2):
  str1=""
  for i in range(len(str2)):
    str1=str1+2*str2[i]
  return str1


print double_char("Hi-There")
