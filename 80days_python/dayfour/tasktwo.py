import random
name_string = input("enter the names(use commas): ")
names = name_string.split(",")
list = len(names)
rand = random.randint(0, list - 1)
clown = names[rand]
print(f"{clown} is going to pay the bills!!!")