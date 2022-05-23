print("Welcome to love calculator")
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
n1 = name1.lower()
n2 = name2.lower()
true1 = n1.count("t") + n1.count("r") + n1.count("u") + n1.count("e")
love1 = n1.count("l") + n1.count("o") + n1.count("v") + n1.count("e")
true2 = n2.count("t") + n2.count("r") + n2.count("u") + n2.count("e")
love2 = n2.count("l") + n2.count("o") + n2.count("v") + n2.count("e")
truelove = str(int(true1) + int(true2))  +  str(int(love1) + int(love2))
true_love = int(truelove)
if true_love < 40 or true_love > 90:
    print(f"Your love percentage is {true_love}%, you go together like coke and mentos")
elif true_love >= 40 and true_love <= 50:
    print(f"Your love percentage is {true_love}%,  you are alright together")
else:
    print(f"Your love percentage is {true_love}%.")        
