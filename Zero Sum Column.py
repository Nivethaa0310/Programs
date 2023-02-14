n=int(input()) 
l=[list(map(int,input().split())) for i in range(n)] 
for j in range(n): 
    col_sum = sum(l[i][j] for i in range(n)) 
    if col_sum!=0: 
        print("no") 
        break 
else: 
    print("yes") 


'''
input: 3 
       2 -1 3
       -2 3 -1 
       0 -2 -2'''