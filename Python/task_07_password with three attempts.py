#task_07 -> Password with 3 attempts.
"""
attempt=3
password = "Mouli"
print("you got 3 attempts only !")
while attempt > 0:
     user=input("enter your password :")
     if user == password :
          print("Access Granted ")
          break
     else :
         attempt-=1
         print(f"Try again. You have {attempt} attempts remaining !")
         if attempt == 0:
            print("Attempt exceeds. Please try again later")          
"""          


"""
chances=3
password="mouli"
print("you have got '3' attempts")
for i in range (3):
    give_password =input('enter your password : ')
    if give_password != password :
        print("your password is wrong")
        chances-=1
        print(f"you have got {chances} remaining")
    else :
        print("successfully logged in..")
        break

if chances==0:
    print("account locked ..!")        
"""   
