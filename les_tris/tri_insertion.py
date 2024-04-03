def TriParInsertion(L):
    a=0
    for j in range(1,len(L)):
        clé=L[j]
        i=j-1
        while i>=0 and L[i]>clé:
            L[i+1]=L[i]
            i=i-1
            a=a+1
        L[i+1]=clé
    return(L,a)
L1=[5,9,0,8,7,4,1,2,6,3]
print(TriParInsertion(L1))
