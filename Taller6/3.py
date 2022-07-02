n=int(input())
A=list(map(int, input().split()))
cont=0
for i in range(n):
    for j in range(n):
        if A[i]==A[j] and j>i:
            cont+=1
print(cont)