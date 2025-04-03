import random
'''
1 for snake 
-1 for water 
0 for gun
'''

computer=random.choice([-1,0,1])

youstr=input("Enter your choice:")
youDict =  {"snake":1, "water":-1, "gun":0}
reverseDict={1:"snake", -1:"water", 0:"gun" }

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer==you):
   print("It's Draw!")
   
else:

 if(computer==-1  and  you==1):
    print("you won!")

 elif(computer==-1  and  you==0):
    print("you Loss!")

 elif(computer==1  and  you==-1):
    print("you Loss!")

 elif(computer==1  and  you==0):
    print("you won!")

 elif(computer==0  and  you==-1):
    print("you won!")

 elif(computer==0  and  you==1):
    print("you Loss!")

 else:
    print("Something went wrong!")

    
    
