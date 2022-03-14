import random

def printSpiralOrder(A, M, N):
 

    if not A:
        return []
 
    top = left = 0
    bottom = M - 1
    right = N - 1
 

    mat = [[0 for x in range(N)] for y in range(M)]
 
    index = 0
 
    while True:
 
        if left > right:
            break
 
 
        for i in range(left, right + 1):
            mat[top][i] = A[index]
            index = index + 1
        top = top + 1
 
        if top > bottom:
            break

        for i in range(top, bottom + 1):
            mat[i][right] = A[index]
            index = index + 1
        right = right - 1
 
        if left > right:
            break

        for i in range(right, left - 1, -1):
            mat[bottom][i] = A[index]
            index = index + 1
        bottom = bottom - 1
 
        if top > bottom:
            break

        for i in range(bottom, top - 1, -1):
            mat[i][left] = A[index]
            index = index + 1
        left = left + 1
 
    for r in mat:
        print(r)
 
 
if __name__ == '__main__':
 

    M = N = 5
    A = []
    for i in range(0,25):
        n = range(1,30)[i]**2
        A.append(n)
        
printSpiralOrder(A, M, N)  
