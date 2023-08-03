def product(a,b):
    n=2
    P=10**9+7
    c=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j]=(c[i][j]+a[i][k]*b[k][j])%P
    return c
def fibonacci(N):
    S=str(bin(N))[2:][::-1]
    M=len(S)
    L=[[[1,1],[1,0]]]
    for i in range(M-1):
        L.append(product(L[i],L[i]))
    R=[[1,0],[0,1]]
    for i in range(M):
        if S[i]=="1":
            R=product(R,L[i])
    return (R[0][1])