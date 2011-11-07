def make_bricks(small,big,goal):
  for x in range(1,big+1):
    for y in range(1,small+1):
      if y+5*x==goal:
        return True

  return False
print make_bricks(1000000,1000,1000100)
