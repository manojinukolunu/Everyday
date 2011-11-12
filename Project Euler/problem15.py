def genGrid(n):
  grid=[[x for x in range(n)]for x in range(n)]
  return grid
grid=genGrid(2)
print grid
startState=grid[0][0]
previousmoves=[]
previousmoves.append(startState)
state=startState
goal=grid[2][2]
routes=[]
while True:
  nextMoves=generateNextMoves(State,grid)
  for i in nextMoves:
    if i not in previousmoves:
      previousmoves.append(i)
      state=i
      if state==goal and previousmoves not in routes:
        routes.add(previousmoves)
        route=route+1
        print route
  if state==goal:
    break



