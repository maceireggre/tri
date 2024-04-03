def TriParSelection(L):

    for i in range(len(L)):
        mini=i
        for j in range(i+1,len(L)):
            if L[j]<L[mini]:
                mini=j
        L[mini],L[i]=L[i],L[mini]

    return(L)
L=[0,1,8,5,4,3,6]
print(TriParSelection(L))


#def TriParInsertion(L):
def TriParInsertion(L):
    for j in range(1,len(L)):
        cle=L[j]
        i=j-1
        while i>=0 and L[i]>cle:
            L[i+1]=L[i]
            i=i-1
        L[i+1]=cle
    return(L)
L1=[9,0,8,1,7,2,6,3,5,4]
print(TriParInsertion(L1))

print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
def TriParFusion(L):
    pass

