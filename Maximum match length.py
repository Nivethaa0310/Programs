s1=input()
s = s1.split(" ")
l={} 
for i in s: 
    l1 = len(i) 
    if l1 in l: 
        l[l1].append(i) 
    else: 
        l[l1] = [i] 

mc = max([len(i) for i in l.values()]) 
mw = [] 
for i in l.values(): 
    if len(i)==mc: 
        mw+=l 

for j in s: 
    if j in mw: 
        print(j,end=' ') 

'''
input: pass on the plate to him 
output: on the to him'''