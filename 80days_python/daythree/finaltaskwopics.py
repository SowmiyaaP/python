print("Welcome to treasure hunt")
print("Find the treasure")
task1 = input("select left or right")
task_1 = task1.lower()
if task_1 == 'left':
    print ("you have been defeated by the demon")
    print ("***********************************")
    print("GAME OVER")
    
else:
    print("you have reached the lake")
    print("*************************")
    task2 = input("Select swim or wait for a boat:")
    task_2 = task2.lower()
    if task_2 == "swim":
       print("you have become the lunch for this small guy")
       print("********************************************")
       print("GAME OVER") 
    else:
      print("a boat has arrived huhu!!")
      print("*************************")
      task3 = print("select a door: red or blue")
      task_3 = task3.lower()
      if task_3 == "red":
        print("you have been killed by the devil")
        print("*********************************")
        print(" GAME OVER")
      else:
        print("congratulations you have completed the mission")
        print("**********************************************")
        
        print(" SPECIAL CHOCOLATE DONUT FOR YOU")
        print(" ******************************* ")
