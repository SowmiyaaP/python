h= input("Enter your height:")
w= input("Enter your weight:")
bmis=(float(w)/(float(h)**2))
bmi= int(bmis)
if  bmi <= 18.5:
    print(f"your bmi is {bmi}, you are under weight \n")
elif  bmi > 18.5 or bmi <= 25:
    print(f"your bmi is {bmi}, your weight is normal \n")
elif bmi > 25 or bmi <= 30:
    print(f"your bmi is {bmi}, you are slightly overweight \n") 
elif bmi > 30 or bmi <= 35:
    print(f"your bmi is {bmi}, you are obese")
elif bmi > 35:
    print(f" your bmi is {bmi}, you are clinically obese")    
