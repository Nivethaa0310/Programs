s=input().strip() 
l=[] 
for i in s: 
    if i.isalpha() and i.lower() in s and i.upper() in s: 
        l.append(i) 
print("".join(l)) 

'''
input: aeroRadeOnoWe

output: roROo'''