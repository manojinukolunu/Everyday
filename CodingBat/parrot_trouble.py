def parrot_trouble(talking, hour):
  return talking and(hour<7 or hour>20)
  
print parrot_trouble(False,6)
