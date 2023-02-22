a =int(input())
x =list(input())
for i in range(len(x)):
    if(x[i].isalpha()):
        x[i] =','
for i in range(len(x)):
    print(x[i],end="") 


'''
input: 12a45n89d40
output: 12,45,89,40'''