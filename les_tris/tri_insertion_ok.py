def TriParInsertion(L):
    c=0
    for j in range(1,len(L)):
        cle=L[j]
        i=j-1
        while i>=0 and L[i]>cle:
            L[i+1]=L[i]
            i=i-1
            c=c+1
        L[i+1]=cle
    return(L,c)
L1=[9,0,8,1,7,2,6,3,5,4]
print(TriParInsertion(L1))
