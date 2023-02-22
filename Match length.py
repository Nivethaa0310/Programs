n=int(input()) 
l=[]; p=[] 
for i in range(n): 
    s,k=input().split() 
    k=int(k) 
    l.append(s) 
    p.append(k) 
for i in l: 
    print(i,p.index(len(i))+1) 

''' 
input : 4 
        watch 3 
        bottle 5 
        car 4 
        lion 6 

output: watch 2 
        bottle 4 
        car 1 
        lion 3 
'''
