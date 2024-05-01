import random
user_choice=int(input("Enter youe choice:rock 0,paper 2,scisoors 3"))
computer_choice=random.randint(0,2)
print("computer choice")
print(computer_choice)
if computer_choice==user_choice:
    print("draw")
elif computer_choice == 0 and user_choice == 2 :
    print("lose")
elif  user_choice == 0  and computer_choice == 2 :  
    print("you win")
elif computer_choice > user_choice:
    print("lose")
elif  user_choice > computer_choice:
    print("win")
elif computer_choice == 0 and user_choice == 2 :
    print("lose")
elif  user_choice == 0  and computer_choice == 2 :  
    print("you win")