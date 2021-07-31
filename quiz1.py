
print ( "                             ------------------------ ////quiz test////------------------------              ")
Name=input('Enter your Name:')
password=int(input('Enter password:'))
if password ==1234 :
    print('         :::::::::::::::::::::::::::::WELCOME',Name,'::::::::::::::::::::::::::::::::        ')
else:
    print('        _/______/______________/_____________/_______ ACCESS DENIED__________________/___________///_________                     ')
    exit()
from datetime import datetime
# returns current date and time
now = datetime.now()
print( now)
A1=input("Q1)what is 2+2=")
if A1=='4':
    print("you are right")
else:
    print("wrong Answer")

A2=input("Q2)what is 2*2=")
if A2=='4':
    print("you are right")
else:
    print("wrong Answer")

A3=input("Q3)what is 10/5=")
if A3=='2':
    print("you are right")
else:
    print("wrong Answer")


A4=input("Q4)what is 12*3=")
if A4=='36':
    print("you are right")
else:
    print("wrong Answer")



A5=input("Q5)when did India get its Independence?=")
if A5=='1947':
    print("you are right")
else:
    print("wrong Answer")

print('             BONUS QUESTION                                        ')
print('Do you want to play the Bonus Question?')
print(' 1.YES')
print('2. NO')
m1=input('PLEASE ENTER YOUR CHOICE:')
if(m1=='n' or m1=='no' or m1=='2'):
    print('####### GAME OVER #######')
elif (m1=='y' or m1=='yes' or m1=='1'):
    A6=input("Q6)wich is Indias Pink city?")
    if(A6=='jaipur' or A6=='JAIPUR' or A6=='Jaipur'):
        print("you are right")
else:
    print("wrong Answer")
    
print('              --------------------------------------THANK YOU FOR PLAYING ------------------------------                        '    )

    
