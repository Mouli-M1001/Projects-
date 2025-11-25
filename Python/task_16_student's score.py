# task 16 --> student's scores

data={}
while True:
    operation = input("Enter operation (add/update/display/exit) : ").lower().strip()
    if operation == "exit":
        print("exiting... Final Data : ",data)
        break
    elif operation  =="add":
        name = input("Enter student name : ").strip().lower()
        score = int(input("Enter student score : "))
        try:
            if name =="" :
                raise AttributeError
            if score <0 or score >100:
                raise ValueError
            if operation == "add":
                data[name]=data.get(name,0)+ score
                print("successfully added...",data)
        except ValueError:
            print("Score must between 0 to 100.Try again")
        except AttributeError as A:
            print(f"Error:{A}")
    elif operation =="update":
        u_name=input("Enter name : ")
        u_score=int(input("Enter updated score : "))
        try:
            if u_name not in data:
                    raise KeyError
            if u_score <0 or u_score >100:
                    raise ValueError
            else:
                data.update({u_name:u_score})
                print(f"updated..{data}")
        except KeyError:
            print(f"{u_name} not found in the data...check again")
        except ValueError:
            print("Score must between 0 to 100.Try again")

    elif operation == "display":
        print("displaying data : \n" , data)



        
"""
error=dir(locals()['__builtins__'])
print(len(error))
print(error)
"""
