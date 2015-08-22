A=[[0 for x in range(3)] for x in range(3)]
B=[[0 for x in range(3)] for x in range(3)]
for i in range(3):
    for j in range(3):
        A[i][j]=2*i+j
        B[j][i]=j-2*i

print "Matrix A is"
print A
print "Matrix B is"
print B

Result=[[0 for x in range(3)] for x in range(3)]

for i in range(3):
    for j in range(3):
        Result[i][j]=0
        for k in range(3):
            Result[i][j]+=A[i][k]*B[k][j]
print "Multiplied Result is: "
print Result
