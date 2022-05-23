import random
print("welcome to stone-paper-scissors game")
c = int(input("type 0 for stone, 1 for paper and 2 for scissors: "))
print(f"your choice is {c}")

if c == 0:
    print("stone")
elif c == 1:
    print("paper")
elif c == 2:
    print("scissors")

c1 = random.randint(0,2)
print(f"computer's choice is {c1}")

if c1 == 0:
    print("stone")
elif c1 == 1:
    print("paper")
elif c1 == 2:
    print("scissors")

if c == 0 and c1 == 1:
    print("YOU LOST")
elif c == 1 and c1 == 2:
    print("YOU LOST")  
elif c == 2 and c1 ==0:
    print("YOU LOST")
elif c == 0 and c1 == 0:
    print("DRAW")    
elif c == 1 and c1 == 1:
    print("DRAW") 
elif c == 2 and c1 == 2:
    print("DRAW")           
else:
    print("YOU WON")              
