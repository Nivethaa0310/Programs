x,y=map(int,input().split())
list1=[i for i in range(1,x+1) if x%i==0] 
list2=[i for i in range(1,y+1) if y%i==0]
newlist = []
a1 = len(list1)
a2 = len(list2)

for i in range(max(a1, a2)):
    if i < a1:
        newlist.append(list1[i])
    if i < a2:
        newlist.append(list2[i])

print(*newlist) 

''' 
input: 100 24 

output: 1 1 2 2 4 3 5 4 10 6 20 8 25 12 50 24 100 

'''
