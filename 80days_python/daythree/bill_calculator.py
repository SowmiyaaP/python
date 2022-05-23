print("Welcome to Pizza deliveries")
size = input("Select the size of the pizza. S, M or L: ")
pep = input("want pepperoni toppings? Y or N: ")
cheese= input("want extra cheese? Y or N:")
bill= 0
if size == 'S':
    bill += 15    
elif size == 'M':
    bill +=20   
elif size == 'L':
    bill += 25

if pep == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3     
           
if cheese == 'Y':
    bill += 1        
print(f"Your final bill is {bill}")
