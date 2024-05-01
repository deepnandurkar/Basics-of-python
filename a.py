n = (input())
m = (input())
sum1 = 0
sum2 = 0
n=int(n)
m=int(m)
for i in range (1,m+1):
  
    if i % n == 0:
        sum1+=i
    else:
        sum2+=i
print(abs(sum2-sum1))