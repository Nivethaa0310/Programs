n=int(input()) 
a='abcdefghijklmnopqrstuvwxyz' 
i=0;j=1;l=[] 
while i<n: 
    r=a[:n]+j*'*'+a[:n][::-1] 
    n-=1 
    j+=2
    l.append(r) 
for i in l: 
    print(' '.join(i)) 

''' 
input: 3 
output:  a b c * c b a
         a b * * * b a 
         a * * * * * a 
         
'''