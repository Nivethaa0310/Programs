n,m=map(int,input().split())
k=max(n,m) 
f=[0,1]
for i in range(2,k): 
    f.append(f[i-1]+f[i-2]) 
print(*f[:f.index(k)+1][::-1]) 

''' 
input: 8 13 
output: 13 8 5 3 2 1 1 0 '''