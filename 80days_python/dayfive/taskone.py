#import random
#student = input("Enter the list of students:")
#for n in random(0, len(student)):
  #student[n] = int(student[n])
#print(student)    
student = [23,45, 98,77]
highest = 0
for score in student:
    if score > highest:
        highest = score

print(f"The highest score is: {highest} ")