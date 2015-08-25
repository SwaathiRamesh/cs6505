print "Longest Increasing Subsequence"
M=[ 10, 22, 9, 33, 21, 50, 41, 60, 80 ]
print M
T =[ 0,0,0,0,0,0,0,0,0]
for i in range(9):
    T[i]=1
    for j in range ( i):
        if M[j]<M[i]:
            T[i]=max(T[j]+1, T[i])
Max=1
print "Calculated Max"
for i in range(1,9):
    if T[i]> Max:
        Max=T[i]
print Max
