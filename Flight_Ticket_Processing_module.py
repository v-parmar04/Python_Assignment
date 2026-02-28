
flight_no = "AI203" 
base_fare = "4500.75" 
tax_percent = "5" 
seat_numbers = "12A,12B,14C,15D" 
is_international = "True" 

base_fare = float(base_fare) # Convert to float
tax_percent = float(tax_percent) # Convert to float

final_fare = base_fare + (base_fare*tax_percent/100)
print(final_fare)

seat_list = seat_numbers.split(',') # Convert in list and using split 
print(seat_list)

seat_set = set(seat_list) # Convert to list in set
print(seat_set)

is_bool = bool(is_international) # Convert to str to bool
print(is_bool)

flight_summary = {          # Convert in Dic in Key : Value 
    "flight_no": flight_no,
    "final_fare": int(final_fare),        # Convert to integer
    "seat_numbers": tuple(seat_list)      # Convert list to tuple
                 }
print(flight_summary) 





