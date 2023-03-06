n=input().strip() 
v=['a','e','i','o','u'] 
k=0
for i in n: 
    if i in v: 
      print(v[k%5],end="") 
      k+=1 
    else: 
        print(i,end="") 

'''
input: kingkong 
output:kangkeng
'''