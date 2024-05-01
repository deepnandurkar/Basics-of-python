import random

name=input("Enter name:")
name_list=name.split(",")
#print(name_list)
length=len(name_list)
random_choice=random.randint(0,length-1)
print(name_list[random_choice])