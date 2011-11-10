def calcsum(n):
    return n*(n+1)/2
def calcsumSquares(n):
    return n*(n+1)*(2*n+1)/6
n1=calcsum(100)
print n1*n1-calcsumSquares(100)
