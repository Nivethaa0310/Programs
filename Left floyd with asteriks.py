n=int(input()) 
k=1 
for i in range(n): 
    for j in range((n-i),1,-1): 
        print("*",end=" ")  
    
    for j in range(0,i+1): 
        print(k,end=" ")
        k+=1 
    print() 

'''input: 3 
    
output:  **1
         *23
         456 
         
         '''