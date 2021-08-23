import random
print("Welcome to coin generator")
output=random.randint(0,1)
if output == 1:
    print("Heads")
else:
    print("Tails")    

print(output)