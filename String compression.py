s=input().strip() 
r='' 
for i in range(len(s)-1): 
    if s[i]!=s[i+1]: 
        r+=s[i]+' ' 
    else: 
        r+=s[i] 
r+=s[len(s)-1]
l=r.split(" ")
for i in l: 
    print(i[0],end="")
    print(len(i),end="")

'''input: aaabbbbcc
   output: a3b4c2'''