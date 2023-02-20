m,n=map(int,input().split());co=0
for i in range(m):
    c=0
    s=input().strip()
    for j in s:
        if s.count(j)==1:
            c+=1
    if c<=n:
        co+=1
print(co) 

'''
input: 4 3
       onion
       radish
       cabbage
       yam'''