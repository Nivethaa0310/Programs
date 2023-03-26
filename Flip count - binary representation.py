n=int(input())
b=bin(n)[2:] 
r=sorted(b) 
i=j=0 
t=[]
while i<len(b) and j<len(r): 
    k=b[i]+r[j]
    i+=1 
    j+=1 
    t.append(k) 
p=[i for i in t if len(list(set(i)))==2] 
print(len(p))
    

''' input: 73 
    output: 4 
    
    input: 15 
    output: 0'''