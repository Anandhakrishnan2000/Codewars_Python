
def rotate(mat):
    size = len(mat)
    orderlst = []
    rotatedMatrix = []
    for j in range(size-1,-1,-1):
        for i in range(0,size):
            orderlst.append(mat[i][j])
    print(orderlst)
    while orderlst!=[]:
        rotatedMatrix.append(orderlst[:size])
        orderlst = orderlst[size:]
    print(rotatedMatrix)


matrixlst=[]
matrix=[]
n = int(input("Enter the size of the matrix"))
print("Enter the matrix:")
for i in range(n):
    for j in range(n):
            matrixlst.append(int(input()))

while matrixlst!=[]:
    matrix.append(matrixlst[:n])
    matrixlst=matrixlst[n:]
print(matrix)

rotate(matrix)