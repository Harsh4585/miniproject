
'''#basic calculator
n1=float(input("enter number 1:"))
n2=float(input("enter number 2:"))
choice=input("enter your choice:")
if(choice=="sum"):
    print(n1+n2)
elif(choice=="subtract"):
    print(n1-n2)
elif(choice=="quotient"):
    print(n1/n2)
elif(choice=="reminder"):
    print(n1%n2)
elif(choice=="multiply"):
    print(n1*n2)
else:
    print("invalid choice") 


 

















#NUMBER SYSTEM
n=int(input("enter value till u want to print"))
print("1 for forward and 0 for reverse")
c=int(input("enter c:"))
if(c==1):
    print("2 for vertical and 3 for horizontal")
    d=int(input("enter d:"))
    if(d==2):
        for i in range(1,n+1,1):
            print(i)
    elif(d==3):
        for i in range(1,n+1,1):
            print(i,end=',')
    else:
        print("invalid choice")
elif(c==0):
    print("2 for vertical and 3 for horizontal")
    d=int(input("enter d:"))
    if(d==2):
        for i in range(n,0,-1):
            print(i)
    elif(d==3):
        for i in range(n,0,-1):
            print(i,end=',')
    else:
        print("invalid choice")
else:
    print("invalid choice")  



 




#voting system
b=0;c=0;a=0;s=0;r=0
while True:
    name=input("enter your name:")
    n=int(input("enter your age:"))
    if(n>=18):
        print("eligble to vote")
        print("bjp==1;INC==2;AAP==3;BSP==4;RLD==5")
        p=int(input("enter the party u want to vote"))
        if(p==1):
            b+=1
            print("BJP total votes:",b)
        elif(p==2):
            c+=1
            print("INC total votes:",c)
        elif(p==3):
            a+=1
            print("AAP total votes:",a)
        elif(p==4):
            s+=1
            print("BSP total votes:",s)
        elif(p==5):
            r+=1
            print("RLD total votes:",r)
        else:
            print("invalid")
        ch=int(input("you want to continue:"))
        if(ch==10):
            continue;
        else:
            break;
    else:
        print("no eligble to vote")
    print("voting is ended")    
    

 


        


#stone paper and scissor

import random

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        play_game()
    computer_choice = random.choice(choices)
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
play_game()     



 







#roll the dice

import random
user=0;comp=0
while True:
    c=random.randint(1,7)
    n=c
    comp+=1
    i=int(input("enter the value:"))
    if(1<=i<=6):
        user+=i
    else:
        print("value out of range")
    k=int(input("enter  to continue"))
    if(k==9):
        continue;
    else:
        break;
print("user total",user)
print("computer total",comp)
if(user>comp):
    print("win",user)
elif(comp>user):
    print("loss",comp)
else:
    print("its a tie") 



 







#grading system
f=open('record file','w')
while True:
    name=input("enter the student name:")
    marks=int(input("enter student total marks:"))
    k=500
    p=(marks/k)*100
    if(95<=p<=100):
        print("student got A+ grade",p)
    elif(90<=p<95):
         print("student got A grade",p)
    elif(80<=p<90):
         print("student got B grade",p)
    elif(70<=p<80):
         print("student got C grade",p)
    elif(60<=p<70):
         print("student got D grade",p)
    elif(0<=p<60):
         print("student got F grade",p)
    else:
        print("H")
    f.write("name:-(name)percentage:-(p)")
    choice=int(input("1 to continue "))
    if(choice==1):
        continue;
    else:
        break;   



 








#guessing number
import random
x=int(input("range till u want"))
while True:
    c=random.randint(1,x)
    n=c
    user=int(input("entr the number user want"))
    if(user==n):
        print("right guess")
        break;
    else:
        print("better luck next time")
    choice=int(input("1 to continue"))
    if(choice==1):
        continue;
    else:
        break;


 










#inventory management
l={"apple":80,"banana":60}
totalamount=0
print(l)
name=input("enter customer name:")
cardamount=int(input("enter card balance:"))
while True:
    cart=input("items purchased:")
    quantity=int(input("enter the quantity:"))
    s=l[cart]
    a=quantity*s
    print(a)
    choice=int(input("1 to continue:"))
    totalamount+=a
    if(choice==1):
        continue;
    else:
        break;
#totalamount+=a
if(cardamount<totalamount):
    print("insufficient balance")
    r=int(input("0 to recharge"))
    if(r==0):
        k=int(input("enter recharge amount"))
        cardamount+=k
        amountleft=cardamount-totalamount
        print("card balance",amountleft)
    else:
        print("no rechgarge")
elif(cardamount>totalamount):
    amountleft=cardamount-totalamount
    print("card balance",amountleft)
else:
    print()




with open('user_input.txt', 'w') as file:
    name = input("Enter your name: ")
    uni_roll= input("Enter your university roll no.: ")

    marks=int(input("Enter total marks of 5 Subject"))
    res=(marks*100)/500
    file.write(f"Name: {name}\n")
    file.write(f"University roll no.: {uni_roll}\n")
    if res<=40:
        file.write(f"Result:{"Fail"}\n")
    else:
        file.write(f"Result:{"Pass"}\n")    
with open ('user_input.txt','r') as file:
    print(file.read())

 '''

