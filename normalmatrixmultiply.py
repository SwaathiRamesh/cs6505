A=[[0 for x in range(5)] for x in range(5)]
B=[[0 for x in range(5)] for x in range(5)]
for i in range(5):
    for j in range(5):
        A[i][j]=2*i+j
        B[i][j]=2*j-i

print "Matrix A is"
print A
print "Matrix B is"
print B
