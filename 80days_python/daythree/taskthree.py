leap= int(input("Enter the year:"))
if leap % 4 == 0:
    if leap % 100 != 0:
       print(f"{leap} is a leap year")
    elif leap % 400 == 0:
        print(f"{leap} is a leap year")
else:
    print(f"{leap} is not a leap year")

