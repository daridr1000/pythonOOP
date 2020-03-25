def vale(S):
    l=1
    ok=0
    while(S[l]<=S[l-1]):
        ok=1
        l+=1
        if l==len(S):
            break
    if l==len(S):
        return False
    while(S[l]>=S[l-1]):
        l+=1
        if l==len(S):
            if ok==1:
                return True
            return False
    return False
S=[1,2,3,4,2,1,0,3,4,1,2,3,1,0,2]
A=[]
m=max(S)
n=len(S)
for i in range(0,n):
    a=[]
    a+=[0]*(m-S[i])
    a+=[1]*S[i]
    A.append(a)
for i in range(0,m):
    j=0
    while(A[j][i]==0):
        A[j][i]=None
        j+=1
    j=n-1
    while(A[j][i]==0):
        A[j][i]=None
        j-=1
trap_water=0
for i in range(0,n):
    trap_water+=A[i].count(0)
print(trap_water)

########as

