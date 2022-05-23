print("Welcome to tip calculator")
total= input("enter the total bill: ")
perc= input("What percentage tip you like to give? 12, 15 or 10:  ")
ppl= input("total number of people: ")

bill= (float(total)*float((int(perc)/100)))

totalbill= float(total) + float(bill)
tip= round(totalbill/int(ppl) ,2)
print("each person should pay:", tip)

