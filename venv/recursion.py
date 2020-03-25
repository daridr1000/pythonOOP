def binary_maxmin(S,start,stop):
    if start >=stop:
        return 0
    elif start==stop-1:
        return S[start]
    else:
        mid=(start+stop)//2
        return max(binary_maxmin(S,mid,stop),binary_maxmin(S,start,mid))

def recursive_maxmin(S,i):
    if i==0:
        return S[i]
    else:
        return max(S[i],recursive_maxmin(S,i-1))

def product(m,n):
    if n==0:
        return 0
    return m+product(m,n-1)

print(product(-8,-2))
print(recursive_maxmin([1,2,8,9,10,11,3,4,12],8))
