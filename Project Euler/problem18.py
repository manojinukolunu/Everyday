
'''
We start from the bottom of the trianlge and work upto the top
'''


table = [[int(n) for n in s.split()] for s in open('problem18.txt').readlines()]
for row in range(len(table)-1,0,-1):
    print row
    for col in range(0,row):
        table[row-1][col]+=max(table[row][col],table[row][col+1])

print table[0][0]
