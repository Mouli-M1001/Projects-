# Taxi price estimator
"""
def calculate_price(distance_km,time_minutes):
     #declare prices
     base_price=5.0
     long_dist_surcharge= 10.0
     per_first_5kms= 2.0
     per_km_after_5kms= 1.5
     per_min_first_10min = 0.5
     per_min_after_10min= 0.3

     if distance_km <= 5:
      distance_charge = distance_km * per_first_5kms
     else:
      distance_charge = (5 * per_first_5kms) + ((distance_km - 5) * per_km_after_5kms)
# Calculate time charge
     if time_minutes <= 10:
      time_charge = time_minutes * per_min_first_10min
     else:
      time_charge = (10 * per_min_first_10min) + ((time_minutes - 10) * per_min_after_10min)
# Apply long distance surcharge if applicable
     if distance_km > 20:
          surcharge = long_dist_surcharge
     else:
          surcharge = 0
# Total fare
     total = base_price + distance_charge + time_charge + surcharge
     total = round(total)
# Fare breakdown
     print("Price Breakdown:")
     print(f"Base price: ${base_price}")
     print(f"Long Distance Charge: ${round(distance_charge, 2)}")
     print(f"Time Charge: ${round(time_charge, 2)}")
     print(f"Long Distance Surcharge: ${surcharge}")
     print(f"Total Fare: ${total}")

    
A=int(round(float(input("Enter km : "))))
B=int(input("enter time (minutes): "))
calculate_price(A,B)

"""
"""
a=123.345#123.556
b=round(a,1)#round(a)
print(b)
"""
