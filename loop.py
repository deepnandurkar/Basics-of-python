number=[]
a=int (input("Enter numbers of size"))
print(a)
for i in range(0,a):
 
    print("Enter number at index", i)
    item = int(input())
    number.append(item)
print("User list is ", number)

x= max(number)
number.remove(x)
y=max(number)
print(x)
print(y)
 
