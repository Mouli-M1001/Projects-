# task_08 -> collecting info and store in in dict data type if they pass few conditions.
"""
dataset = {"name" :"", "age" :"", "email" :""}
while True :
 for_name = input("enter your name : ").strip().lower()#.values()
 if any(char.isdigit() for char in for_name):
  print("your input contains number. try again ")
  continue 
 else :
     dataset["name"]=for_name
     print(dataset)
     for_age = int(input("enter your age : "))
     if for_age <=18:
         print("enter vaild age above 18 years")
         continue
     else:
          dataset["age"]=for_age
          print(dataset)
          for_email=input("enter your email id : ")
          if "@"not in for_email or "." not in for_email :
              print("enter valid email. must have '@' and '.'")
              continue
          else :
              dataset["email"]=for_email
              print("your information stored .",dataset)
              break

"""
"""
dataset = {"name" :"", "age" :"", "email" :""}
data_count=int(input("enter how many data you are updating now : "))
while data_count >0 :
#for i in range (data_count):               
 for_name = input("enter your name : ").strip().lower()#.values()
 if any(char.isdigit() for char in for_name):
  print("your input contains number. try again ")
  continue 
 else :
     dataset["name"]=for_name
     print(dataset)
     for_age = int(input("enter your age : "))
     if for_age <=18:
         print("enter vaild age above 18 years")
         continue
     else:
          dataset["age"]=for_age
          print(dataset)
          for_email=input("enter your email id : ")
          if "@"not in for_email or "." not in for_email :
              print("enter valid email. must have '@' and '.'")
              continue
          else :
              dataset["email"]=for_email
              print("your information stored .",dataset)
              data_count=data_count-1
"""
"""
dataset = {}
data_count=int(input("enter how many data you are updating now : "))
while data_count >0 :

 for_name = input("enter your name : ").strip().lower()#.values()
 if any(char.isdigit() for char in for_name):
  print("your input contains number. try again ")
  continue

 else :
     dataset.update({"name":for_name})
     print(dataset)
     for_age = int(input("enter your age : "))
     if for_age <=18:
         print("enter vaild age above 18 years")
         continue
        
     else:
          dataset.update({"age":for_age})
          print(dataset)
          for_email=input("enter your email id : ")
          if "@"not in for_email or "." not in for_email :
              print("enter valid email. must have '@' and '.'")
              continue
            
          else :
              dataset.update({"email":for_email})
              print("your information stored .",dataset)
              data_count=data_count-1



"""
#to store continuous data
dataset={}
while True:
    name = input('enter your name or type exit to stop : ').lower()
    if name =="exit":
        break
    age=int(input('enter your age : '))
    email=input('enter your email')
    dataset[name]={'age':age,'email':email}
    print('\ncurrent dataset:')
    for key,value in dataset.items():
            print(f"{key}:{value}")
          




