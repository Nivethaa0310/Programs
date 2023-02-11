r,c=map(int,input().split()) 
l=[list(map(int,input().split())) for i in range(r)] 
for i in range(len(l)): 
    if i%2==0: 
        l[i]=sorted(l[i]) 
    else: 
        l[i]=sorted(l[i])[::-1] 
for i in l: 
    print(*i) 

''' 
input: 4 4 
       1 0 1 0 
       1 1 0 0 
       0 1 0 1 
       1 0 0 1 


output: 0 0 1 1 
        1 1 0 0 
        0 0 1 1 
        1 1 0 0
'''