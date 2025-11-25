# discount on travel ticket.
fixed_price=50

def discount(x):
    if x >= 18 and x<= 60:
        price=fixed_price
        print(f"${price} for Adult")
    if x>60 :
        price= (fixed_price - (fixed_price)*0.2)
        print(f"${price} for Senior Citizen")
    if x<18 :
        price= (fixed_price - (fixed_price)*0.3)
        print(f"${price} for Teens and Children")   


a=int(input("Enter your age : "))
discount(a)
