s=input().strip() 
k=0 
for i in range(len(s)): 
    p = ord(s[i])-ord('a')+1 
    k = k*26 + p 
print(k) 


'''

input: ac 
output: 29 

input: all 
output: 1000'''