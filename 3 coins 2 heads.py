n=int(input()) 
l=[list(input().split()) for i in range(n)] 
r=[]
for i in l: 
    if i.count('H')>=2: 
        r.append(i) 
print(len(r))
        
        
'''input: 3 
       H H T 
       H T H 
       T T H 
       
output: 2 '''