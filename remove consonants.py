s=input().strip() 
v='aeiouAEIOU' 
l=[i+1 for i in range(len(s)) if s[i] not in v] 
r=s[::-1]
for i in range(len(r)): 
    if i+1 not in l: 
        print(r[i],end="") 


'''
input: baggage 
output: ggb '''