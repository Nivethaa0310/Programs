n=int(input()) 
l=list(map(int,input().split())) 
for i in l: 
    if i%10%2==0: 
        if i%10 == 9: 
            i-=8 
        else: 
            i+=1 
    else: 
        if i//10%10 == 9: 
            i-=90 
        else: 
            i+=10 
    print(i,end=" ")

'''input: 4 
          124 25 66887 499 
          
   output: 125 35 66897 409'''