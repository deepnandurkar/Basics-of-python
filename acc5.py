



x = list(map(int, input("value").split()))
a=[]
count=0
for i in range(1,15):
    b=i*i
    a.append(b)
 
    for p in x:
      for j in a:
        if(p==j):  
         count+=1
             
            
print(count)