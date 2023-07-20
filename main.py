def findFibbonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return findFibbonacci(n-1)+findFibbonacci(n-2)

print(findFibbonacci(int(input())))