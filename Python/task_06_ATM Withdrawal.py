#task_06 -> ATM withdrawal
"""
balanc e = 5000
while balance > 0 :
     withdraw = int(input("enter amount : "))
     if withdraw ==0 or withdraw < 0 :
      print("the amount cannot be transactioned . try again")       
     elif withdraw > balance :
          print("insufficient balance.please try again")
          print("your current balance is : ", balance)
     else :
          check = input( "do you want to continue?(yes/no) : ")
          if check == "yes" :
           balance -= withdraw          
           print("withdrawal successful")
           print(f"remaining balance is {balance}.","transaction ended")
           check_1 = input("do you want to withdraw again ? (yes/no) :")
           if check_1 =="no":
                print("thank you")
                break
           else :
               if check_1=="yes" and balance == 0 :
                break
                print("sorry you cannot enter again . current balance touches 0") 
            
print(f"current balance is {balance}")               

"""
"""
balance = 5000
while balance > 0 :
     withdraw = int(input("enter amount : "))
     if withdraw ==0 or withdraw < 0 :
      print("the amount cannot be transactioned . try again")       
     elif withdraw > balance :
          print("insufficient balance.please try again")
          print("your current balance is : ", balance)
     else :
          check = input( "do you want to continue?(yes/no) : ")
          if check == "yes" :
           balance -= withdraw          
           print("withdrawal successful")
           print(f"remaining balance is {balance}.","transaction ended")
           check_1 = input("do you want to withdraw again ? (yes/no) :")
           if check_1 =="no":
                print("thank you")
                break
           else :
               if check_1=="yes" and balance == 0 :
                break
                print("sorry you cannot enter again . current balance touches 0") 
            
print(f"current balance is {balance}")               

"""













#roughwork
"""
balance = 5000
while balance > 0 :
     withdraw = int(input("enter amount : "))
     if withdraw ==0 or withdraw < 0 :
      print("the amount cannot be transactioned . try again")       
     elif withdraw > balance :
          print("insufficient balance.please try again")
          print("your current balance is : ", balance)
     else :
          check = input( "do you want to continue?(yes/no) : ")
          if check == "yes" :
           balance -= withdraw          
           print("withdrawal successful")
           print(f"remaining balance is {balance}.","transaction ended")
           check_1 = input("do you want to withdraw again ? (yes/no) :")
           if check_1 =="no":
                print("thank you")
                break
           elif check_1 =="yes":
               print("sorry, you cannot with withdraw again.")
print("current balance drown to zero")               
"""
