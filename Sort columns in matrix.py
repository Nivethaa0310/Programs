r,c=map(int,input().split()) 
l=[list(map(int,input().split())) for i in range(r)] 
k=list(zip(*l)) 
mat = sorted(range(c), key=lambda i: max(l[j][i] for j in range(r)), reverse=True) 
for i in range(r): 
    for j in mat: 
        print(l[i][j],end=" ") 
    print() 

'''input: 3 4
          
          45 18 38 36
          5 33 33 4
          40 30 24 42 
          
   output: 45 36 38 18
           5 4 33 33 
           40 42 24 30 '''