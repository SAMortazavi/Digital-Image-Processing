from typeguard import typechecked
import numpy as np
@typechecked #limit input type
def matrix(seed:int,dims:tuple):
    (rows, cols) =dims 
    matrix2D = [([0]*cols) for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if i==0 and j==0:
                matrix2D[i][j]=seed
            elif i==0:
                matrix2D[i][j]=matrix2D[i][j-1]
            elif j==0:
                matrix2D[i][j]=matrix2D[i-1][j]
            else:
                matrix2D[i][j]=matrix2D[i-1][j]+matrix2D[i][j-1]+matrix2D[i-1][j-1]
    matrix2D=np.array(matrix2D)
    matrix2D=matrix2D.reshape(rows,cols) 
    return matrix2D
print(matrix(2,(3,4)))