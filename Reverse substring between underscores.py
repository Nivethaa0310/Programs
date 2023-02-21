s=input()
l=[i for i in range(len(s)) if s[i]=='_'] 
print(s[:l[0]]+'_',end="") 
for i in range(len(l)-1): 
    print(s[l[i]+1:l[i+1]][::-1]+'_',end="") 
print(s[l[-1]+1:])

'''
input: abcd_efgh_ijke_mnl

output: abcd_hgfe_ekji_mnl'''