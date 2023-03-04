s=0 
while True: 
    a,b= map(int,input().strip().split()) 
    if a==b: 
        s+= a+b 
    else: 
        s+=a+b 
        break 
print(s) 

'''
input: 4 4
       3 3 
       2 5
'''